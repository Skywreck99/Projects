const FPS = 30                      // frames per second
const FRICTION = 0.7                // friction coefficient of space
const GAME_LIVES = 3                // Starting number of lives
const LAZER_DIST = 0.6              // maximum distance lazer can travel as fraction of screen width
const LAZER_EXPLODE_DUR = 0.1       // duration of the lazers' explosion in seconds
const LAZER_MAX = 10                // maximum number of lazers on screen at once
const LAZER_SPD = 500               // speed of lazers in pixels per second
const MUSIC_ON = true               // activate the background music
const ROIDSJAG = 0.4                // jaggedness of the asteroids
const ROIDSNUM = 3                  // starting number of asteroids
const ROID_PTS_LGE = 20             // points scored for a large asteroid
const ROID_PTS_MED = 50             // points scored for a medium asteroid
const ROID_PTS_SML = 100            // points scored for a small asteroid
const ROIDSSIZE = 100               // starting size of asteroids in pixels
const ROIDSSPD = 50                 // max tarting speed of asteroids in pixels per second
const ROIDSVERT = 10                // average number of vertices of each asteroid
const SAVE_KEY_SCORE = "highscore"  // save key for local storage of high score
const SHIP_BLINK_DUR = 0.1          // duration of the ship's blink during invisibility in seconds
const SHIP_EXPLODE_DUR = 0.3        // duration of the ship's explosion
const SHIP_INV_DUR = 3              // duration of the ship's invisibility in seconds
const SHIPSIZE = 30                 // ship height in pixels
const SHIPTHRUST = 5                // accelation of the ship in pixels per second
const TURNSPEED = 360               // turn speed in degrees per second
const SHOWBOUNDING = false          // show or hide collision bounding
const SHOWCENTERDOT = false         // show or hide the ship's center dot
const SOUND_ON = true               // activate the sound
const TEXT_FADE_TIME = 2.5          // text fade time in seconds
const TEXT_SIZE = 40                // text font height in pixels

/** @type {HTMLCanvasElement} */
var canv = document.getElementById("gameCanvas")
var ctx = canv.getContext("2d")
canv.width = innerWidth - 4
canv.height = innerHeight - 4

// Set up sound effects
var fxExplode = new Sound("sounds/explode.m4a")
var fxHit = new Sound("sounds/hit.m4a", 5)
var fxLazer = new Sound("sounds/laser.m4a", 5, 0.5)
var fxThrust = new Sound("sounds/thrust.m4a")

// Set up background music
var music = new Music("sounds/music-low.m4a", "sounds/music-high.m4a")
var roidsLeft, roidsTotal

// Set up game parameters
var level, lives, roids, score, scoreHigh, ship, text, textAlpha
newGame()

// Set up Event Handlers when the key is being pushed and 
// when the key is being released
document.addEventListener("keydown", keyDown)
document.addEventListener("keyup", keyUp)

// Set the game loop
setInterval(update, 1000 / FPS)

// Create Asteroid Belt
function createAsteroidBelt() {
    roids = []
    roidsTotal = (ROIDSNUM + level) * 7
    roidsLeft = roidsTotal
    for (var i = 0; i < ROIDSNUM + level + 2; i++) {
        // Place the asteroids far from the ship initially
        do {
            x = Math.floor(Math.random() * canv.width)
            y = Math.floor(Math.random() * canv.height)
        } while (distBetweenPoints(ship.x, ship.y, x, y) < ROIDSSIZE * 2 + ship.r)
        roids.push(newAsteroid(x, y, Math.ceil(ROIDSSIZE / 2)))
    }

}

// Create the destruction of the astroid
function destroyAsteroid(index) {
    var x = roids[index].x
    var y = roids[index].y
    var r = roids[index].r
    
    // Split the asteroid in two if necessary
    if (r == Math.ceil(ROIDSSIZE / 2)) {                            // large asteroid
        roids.push(newAsteroid(x, y, Math.ceil(ROIDSSIZE / 4)))
        roids.push(newAsteroid(x, y, Math.ceil(ROIDSSIZE / 4)))
        score += ROID_PTS_LGE

    } else if (r == Math.ceil(ROIDSSIZE / 4)) {                     // medium asteroid
        roids.push(newAsteroid(x, y, Math.ceil(ROIDSSIZE / 8)))
        roids.push(newAsteroid(x, y, Math.ceil(ROIDSSIZE / 8)))
        score += ROID_PTS_MED
    } else {                                                         // small asteroid
        score += ROID_PTS_SML
    }

    // Check high score
    if (score > scoreHigh) {
        scoreHigh = score
        // Save the score locally
        localStorage.setItem(SAVE_KEY_SCORE, scoreHigh)
    }

    // Remove the asteroid on the screen
    roids.splice(index, 1)
    fxHit.play()

    // Calculate the ratio of remaining asteroids to determine music tempo
    roidsLeft--
    music.setAsteroidRatio(roidsLeft == 0 ? 1: roidsLeft / roidsTotal)

    // New level when no more asteroids
    if (roids.length == 0) {
        level++
        newLevel()
    }
}

function distBetweenPoints(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
}

function drawShip(x, y, a, color = "white") {
    ctx.strokeStyle = color
    ctx.lineWidth = SHIPSIZE / 20
    ctx.beginPath()

    // Draw the nose of the ship
    ctx.moveTo(
        x + 4 / 3 * ship.r * Math.cos(a),
        y - 4 / 3 * ship.r * Math.sin(a)
    )

    // Draw the left rear
    ctx.lineTo(
        x - ship.r * (2 / 3 * Math.cos(a) + Math.sin(a)),
        y + ship.r * (2 / 3 * Math.sin(a) - Math.cos(a))
    )
    
    // Draw the right rear
    ctx.lineTo(
        x - ship.r * (2 / 3 * Math.cos(a) - Math.sin(a)),
        y + ship.r * (2 / 3 * Math.sin(a) + Math.cos(a))
    )
    ctx.closePath()
    ctx.stroke()
}

function explodeShip() {
    ship.explodeTime = Math.ceil(SHIP_EXPLODE_DUR * FPS)
    fxExplode.play()
}

function gameOver() {
    ship.dead = true
    text = "Game Over"
    textAlpha = 1.0
}

function keyDown(/** @type {keyboardEvent} */ ev) {
    if (ship.dead) {
        return
    }

    switch(ev.keyCode) {
        case 32: // space bar to shoot lazer
            shootLazer()
            break
        case 37: // rotate the ship to the left
            ship.rot = TURNSPEED / 180 * Math.PI / FPS
            break
        case 38: // move the ship forward
            ship.thrusting = true
            break
        case 39: // rotate the ship to the right
            ship.rot = -TURNSPEED / 180 * Math.PI / FPS
            break
    }
}

function keyUp(/** @type {keyboardEvent} */ ev) {
    if (ship.dead) {
        return
    }
    switch(ev.keyCode) {
        case 32: // space bar to shoot lazer
            ship.canShoot = true
            break
        case 37: // stop rotating left
            ship.rot = 0
            break
        case 38: // stop moving forward
            ship.thrusting = false
            break
        case 39: // stop rotating right
            ship.rot = 0
            break
    }
}

function newAsteroid(x, y, r) {
    var lvlMult = 1 + 0.1 * level
    var roid = {
        x: x,
        y: y,
        xv: Math.random() * ROIDSSPD * lvlMult / FPS * (Math.random() < 0.5 ? 1 : -1),
        yv: Math.random() * ROIDSSPD * lvlMult / FPS * (Math.random() < 0.5 ? 1 : -1),
        r: r,
        a: Math.random() * Math.PI * 2, // in radians
        vert: Math.floor(Math.random() * (ROIDSVERT + 1) + ROIDSVERT / 2),
        offs: []
    }

    //create the vertex offsets array
    for (var i = 0; i < roid.vert; i++) {
        roid.offs.push(Math.random() * ROIDSJAG * 2 + 1 - ROIDSJAG)
    }

    return roid
}

function newGame() {
    level = 0
    lives = GAME_LIVES
    score = 0
    ship = newShip()

    // Get the high score from the local storage
    var scoreStr = scoreHigh = localStorage.getItem(SAVE_KEY_SCORE)
    if (scoreStr == null) {
        scoreHigh = 0
    } else {
        scoreHigh = parseInt(scoreStr)
    }
    newLevel()
}

function newLevel() {
    text = "level " + (level + 1)   // Set up the text for the level
    textAlpha = 1.0                 // Color of the text
    createAsteroidBelt()            // Set up asteriod belt
}

function newShip() {
    return {
        x: canv.width / 2,
        y: canv.height / 2,
        r: SHIPSIZE / 2,
        a: 90 / 180 * Math.PI, // convert to radians
        blinkNum: Math.ceil(SHIP_INV_DUR / SHIP_BLINK_DUR),
        blinkTime: Math.ceil(SHIP_BLINK_DUR * FPS),
        canShoot: true,
        dead: false,
        lazers: [],
        explodeTime: 0,
        rot: 0,
        thrusting: false,
        thrust: {
            x: 0,
            y: 0
        }
    }
}

function shootLazer() {
    // Create the Lazer Object
    if (ship.canShoot && ship.lazers.length < LAZER_MAX) {

        // From the nose of the ship
        ship.lazers.push({                              
            x: ship.x + 4 / 3 * ship.r * Math.cos(ship.a),
            y: ship.y - 4 / 3 * ship.r * Math.sin(ship.a),
            xv: LAZER_SPD * Math.cos(ship.a) / FPS,
            yv: -LAZER_SPD * Math.sin(ship.a) / FPS,
            dist: 0,
            explodeTime: 0
        })
        fxLazer.play()  // play the lazer sound
    }

    // Prevent further shooting
    ship.canShoot = false
}

function Music(srcLow, srcHigh) {
    this.soundLow = new Audio(srcLow)
    this.soundHigh = new Audio(srcHigh)
    this.low = true
    this.tempo = 1.0    // seconds per beat
    this.beatTime = 0   // frames left until next beat

    this.play = function() {
        if (MUSIC_ON) {
            if (this.low) {
                this.soundLow.play()
            } else {
                this.soundHigh.play()
            }

            if (!ship.dead) {
                this.low = !this.low
            } else {
                this.low = true
            }
        }    
    }

    this.setAsteroidRatio = function(ratio) {
        this.tempo = 1.0 - 0.75 * (1.0 - ratio)
    }

    this.tick = function() {
        if (!ship.dead) {
            if (this.beatTime == 0) {
                this.play()
                this.beatTime = Math.ceil(this.tempo * FPS)
            } else {
                this.beatTime--
            }
        } else {
            this.beatTime = 0
            this.tempo = 1.0
        }
        
    }
}

// Manage the sound especially 
// when the sound is required to play simultaneously
function Sound(src, maxStreams = 1, vol = 1.0) {
    this.streamNum = 0
    this.streams = []
    for (var i = 0; i < maxStreams; i++) {
        this.streams.push(new Audio(src))
        this.streams[i].volume = vol
    }

    this.play = function() {
        if (SOUND_ON) {
            this.streamNum = (this.streamNum + 1) % maxStreams
            this.streams[this.streamNum].play()
        }
    }

    this.stop = function() {
        this.streams[this.streamNum].pause()
        this.streams[this.streamNum].currentTime = 0
    }
}

// Updates the screen
function update() {
    var blinkOn = ship.blinkNum % 2 == 0
    var exploding = ship.explodeTime > 0

    // Tick the music
    music.tick()

    // Draw the space
    ctx.fillStyle = "black"
    ctx.fillRect(0, 0, canv.width, canv.height)
    
    // Move the ship forward
    if (ship.thrusting && !ship.dead) {
        ship.thrust.x += SHIPTHRUST * Math.cos(ship.a) / FPS
        ship.thrust.y -= SHIPTHRUST * Math.sin(ship.a) / FPS
        fxThrust.play()

        // Check if the ship is exploding
        if (!exploding && blinkOn) {

            // Draw the Thruster
            ctx.fillStyle = "red"
            ctx.strokeStyle = "yellow"
            ctx.lineWidth = SHIPSIZE / 10
            ctx.beginPath()

            // Draw the nose of the ship
            ctx.moveTo( // rear left
                ship.x - ship.r * (2 / 3 * Math.cos(ship.a) + 0.5 * Math.sin(ship.a)),
                ship.y + ship.r * (2 / 3 * Math.sin(ship.a) - 0.5 * Math.cos(ship.a))
            )

            // Draw the left rear
            ctx.lineTo( // rear center behind the ship
                ship.x - ship.r * 6 / 3 * Math.cos(ship.a),
                ship.y + ship.r * 6 / 3 * Math.sin(ship.a)
            )
            
            ctx.lineTo( // rear right
                ship.x - ship.r * (2 / 3 * Math.cos(ship.a) - 0.5 * Math.sin(ship.a)),
                ship.y + ship.r * (2 / 3 * Math.sin(ship.a) + 0.5 * Math.cos(ship.a))
            )
            ctx.closePath()
            ctx.fill()
            ctx.stroke()
        }
        
    } else {
        // Apply the friction to slow down the ship
        ship.thrust.x -= FRICTION * ship.thrust.x / FPS
        ship.thrust.y -= FRICTION * ship.thrust.y / FPS
        fxThrust.stop()
    }

    // Draw a triangular ship
    if (!exploding) {
        if (blinkOn && !ship.dead) {
            drawShip(ship.x, ship.y, ship.a)
        }

        // Handle Blinking
        if (ship.blinkNum > 0) {
            ship.blinkTime--    // reduce the blink time
            
            if (ship.blinkTime == 0) {
                ship.blinkTime = Math.ceil(SHIP_BLINK_DUR * FPS)
                ship.blinkNum--
            }
        }
        
    } else {
        ctx.fillStyle = "darkred"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r, 1.7, Math.PI * 2, false)
        ctx.fill()
        
        ctx.fillStyle = "red"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r * 1.4, 0, Math.PI * 2, false)
        ctx.fill()

        ctx.fillStyle = "orange"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r * 1.1, 0, Math.PI * 2, false)
        ctx.fill()

        ctx.fillStyle = "yellow"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r * 0.8, 0, Math.PI * 2, false)
        ctx.fill()

        ctx.fillStyle = "white"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r*  0.5, 0, Math.PI * 2, false)
        ctx.fill()
    }

    if (SHOWBOUNDING) {
        ctx.strokeStyle = "lime"
        ctx.beginPath()
        ctx.arc(ship.x, ship.y, ship.r, 0, Math.PI * 2, false)
        ctx.stroke()
    }
    
    // Draw the asteroids
    var x, y, r, a, vert, offs
    for (var i = 0; i < roids.length; i++) {
        ctx.strokeStyle = "slategrey"
        ctx.lineWidth = SHIPSIZE / 20

        // Get the asteroid properties
        x = roids[i].x
        y = roids[i].y
        r = roids[i].r
        a = roids[i].a
        vert = roids[i].vert
        offs = roids[i].offs

        // Draw a path
        ctx.beginPath();
        ctx.moveTo(
            x + r * offs[0] * Math.cos(a),
            y + r * offs[0] * Math.sin(a)
        )

        // Draw the polygon
        for (var j = 1; j < vert; j++) {
            ctx.lineTo(
                x + r * offs[j] * Math.cos(a + j * Math.PI * 2 / vert),
                y + r * offs[j] * Math.sin(a + j * Math.PI * 2 / vert)
            )
        }
        ctx.closePath()
        ctx.stroke()
        
        // Show Collision Bounding
        if (SHOWBOUNDING) {
            ctx.strokeStyle = "lime"
            ctx.beginPath()
            ctx.arc(x, y, r, 0, Math.PI * 2, false)
            ctx.stroke()
        }
    }

    // Show Center Dot
    if (SHOWCENTERDOT) {
        ctx.fillStyle = "red"
        ctx.fillRect(ship.x - 1, ship.y - 1, 2, 2)
    }

    // Draw the lazers
    for (var i = 0; i < ship.lazers.length; i++) {
        if (ship.lazers[i].explodeTime == 0) {
            ctx.fillStyle = "salmon"
            ctx.beginPath()
            ctx.arc(ship.lazers[i].x, ship.lazers[i].y, SHIPSIZE / 15, 0, Math.PI * 2, false)
            ctx.fill()
        } else {
            // Draw the explosion
            ctx.fillStyle = "orangered"
            ctx.beginPath()
            ctx.arc(ship.lazers[i].x, ship.lazers[i].y, ship.r * 0.75, 0, Math.PI * 2, false)
            ctx.fill()

            ctx.fillStyle = "salmon"
            ctx.beginPath()
            ctx.arc(ship.lazers[i].x, ship.lazers[i].y, ship.r * 0.5, 0, Math.PI * 2, false)
            ctx.fill()

            ctx.fillStyle = "pink"
            ctx.beginPath()
            ctx.arc(ship.lazers[i].x, ship.lazers[i].y, ship.r * 0.25, 0, Math.PI * 2, false)
            ctx.fill()
        }
        

    }

    // Draw the game text
    if (textAlpha >= 0) {
        ctx. textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillStyle = "rgba(255, 255, 255, " + textAlpha + ")"
        ctx.font = "small-caps " + TEXT_SIZE + "px dejavu sans mono"
        ctx.fillText(text, canv.width / 2, canv.height * 0.75)
        textAlpha -= (1.0 / TEXT_FADE_TIME / FPS)
    } else if (ship.dead) {
        newGame()
    }

    // Draw the lives
    var lifeColor
    for (var i = 0; i < lives; i++) {
        lifeColor = exploding && i == lives - 1 ? "red" : "white"
        drawShip(SHIPSIZE + i * SHIPSIZE * 1.2, SHIPSIZE, 0.5 * Math.PI, lifeColor)
    }

    // Draw the score
    ctx. textAlign = "right"
    ctx.textBaseline = "middle"
    ctx.fillStyle = "white"
    ctx.font = TEXT_SIZE + "px dejavu sans mono"
    ctx.fillText(score, canv.width - SHIPSIZE / 2, SHIPSIZE)

    // Draw the high score
    ctx. textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillStyle = "white"
    ctx.font = (TEXT_SIZE * 0.5) + "px dejavu sans mono"
    ctx.fillText("Best Score: " + scoreHigh, canv.width / 2, SHIPSIZE)

    // Detect lazer hits on asteroids
    var ax, ay, ar, lx, ly
    for (var i = roids.length-1; i >= 0; i--) {
        ax = roids[i].x
        ay = roids[i].y
        ar = roids[i].r

        // Loop over the lazers
        for (var j = ship.lazers.length-1; j >= 0; j--) {
            lx = ship.lazers[j].x
            ly = ship.lazers[j].y

            // Detect hits
            if (ship.lazers[j].explodeTime == 0 && distBetweenPoints(ax, ay, lx, ly) < ar) {
                destroyAsteroid(i)          // destroy the Asteroid and activate the lazer explosion
                ship.lazers[j].explodeTime = 
                    Math.ceil(LAZER_EXPLODE_DUR * FPS)
            }
        }
    }

    // Check for asteroid collisions
    if (!exploding) {

        // Makes the ship invulnerable while blinking
        if (ship.blinkNum == 0 && !ship.dead) {
            for (var i = 0; i < roids.length; i++) {
                if (distBetweenPoints(ship.x, ship.y, roids[i].x, roids[i].y) < ship.r + roids[i].r) {
                    explodeShip()
                    destroyAsteroid(i)
                    break
                }
            }
        }
        
        // Rotate the ship
        ship.a += ship.rot

        // Move ship
        ship.x += ship.thrust.x
        ship.y += ship.thrust.y

    } else {
        ship.explodeTime--              // Reduce explode time
        if (ship.explodeTime == 0) {    // Reset the ship after the explosion has finished
            lives--
            if (lives == 0) {
                gameOver()
            } else {
                ship = newShip()
            }     
        }
    }

    // Handle the edge of the screen
    if (ship.x < 0 - ship.r) {
        ship.x = canv.width + ship.r
    } else if (ship.x > canv.width + ship.r) {
        ship.x = 0 - ship.r
    }

    if (ship.y < 0 - ship.r) {
        ship.y = canv.height + ship.r
    } else if (ship.y > canv.height + ship.r) {
        ship.y = 0 - ship.r
    }

    // Move the lazers
    for (var i = ship.lazers.length-1; i >= 0; i--) {
        // Check the distance travelled
        if (ship.lazers[i].dist > LAZER_DIST * canv.width) {
            ship.lazers.splice(i, 1)
            continue
        }

        // Handle the explosion 
        if (ship.lazers[i].explodeTime > 0) {
            ship.lazers[i].explodeTime--

            // Destroy the lazer after the duration is up
            if (ship.lazers[i].explodeTime == 0) {
                ship.lazers.splice(i, 1)
                continue
            }

        } else {
            
            // Move the lazer
            ship.lazers[i].x += ship.lazers[i].xv
            ship.lazers[i].y += ship.lazers[i].yv
            
            // Calculate the distance travelled
            ship.lazers[i].dist += Math.sqrt(Math.pow(ship.lazers[i].xv, 2) + Math.pow(ship.lazers[i].yv, 2))

        }

        // Activate this to make the lazers loop around
        /*
        // Handle the edge of the screen
        if (ship.lazers[i].x < 0) {
            ship.lazers[i].x = canv.width
        } else if (ship.lazers[i].x > canv.width) {
            ship.lazers[i].x = 0
        }
        if (ship.lazers[i].y < 0) {
            ship.lazers[i].y = canv.height
        } else if (ship.lazers[i].y > canv.height) {
            ship.lazers[i].y = 0
        }
        */
    }

    // Move the asteroids
    for (var i = 0; i < roids.length; i++) {
        roids[i].x += roids[i].xv;
        roids[i].y += roids[i].yv;

        // Handle the edge of the screen
        if (roids[i].x < 0 - roids[i].r) {
            roids[i].x = canv.width + roids[i].r 
        } else if (roids[i].x > canv.width + roids[i].r) {
            roids[i].x = 0 - roids[i].r
        }
        if (roids[i].y < 0 - roids[i].r) {
            roids[i].y = canv.height + roids[i].r 
        } else if (roids[i].y > canv.height + roids[i].r) {
            roids[i].y = 0 - roids[i].r
        }
    }
    
    // Center Dot
    ctx.fillStyle = "red"

}