const canvas = document.querySelector('canvas')
const cont = canvas.getContext('2d')

// Make canvas cover the entire web page
canvas.width = innerWidth
canvas.height = innerHeight

const scoreEl = document.querySelector('#scoreEl')
const startGameBtn = document.querySelector('#startGameBtn')
const modelEl = document.querySelector('#modelEl')
const bigScoreEl = document.querySelector('#bigScoreEl')

// Place the player at the center of the screen
const x = canvas.width / 2
const y = canvas.height / 2

// Friction for the particles' velocities to decelerate over time
const friction = 0.99

// Create a player class with needed attributes
class Player {
    constructor (x, y, rad, color) {
        this.x = x
        this.y = y
        this.rad = rad
        this.color = color
    }

    // draw function to draw the circle
    draw() {
        cont.beginPath()
        cont.arc(this.x, this.y, this.rad, 
                0, Math.PI * 2, false)
        cont.fillStyle = this.color
        cont.fill()
    }
}

class Projectile {
    constructor (x, y, rad, color, velocity) {
        this.x = x
        this.y = y
        this.rad = rad
        this.color = color
        this.velocity = velocity
    }

    // draw function to draw the circle
    draw() {
        cont.beginPath()
        cont.arc(this.x, this.y, this.rad, 
                0, Math.PI * 2, false)
        cont.fillStyle = this.color
        cont.fill()
    }

    // update the property of the class
    update() {
        this.draw()
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

class Opponent {
    constructor (x, y, rad, color, velocity) {
        this.x = x
        this.y = y
        this.rad = rad
        this.color = color
        this.velocity = velocity
    }
    
    // draw function to draw the circle
    draw() {
        cont.beginPath()
        cont.arc(this.x, this.y, this.rad, 
                0, Math.PI * 2, false)
        cont.fillStyle = this.color
        cont.fill()
    }

    // update the property of the class
    update () {
        this.draw()
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

class Particle {
    constructor (x, y, rad, color, velocity) {
        this.x = x
        this.y = y
        this.rad = rad
        this.color = color
        this.velocity = velocity
        this.alpha = 1
    }
    
    // Draws the particles in faded manner
    draw() {
        cont.save()
        cont.globalAlpha = this.alpha
        cont.beginPath()
        cont.arc(this.x, this.y, this.rad, 
                0, Math.PI * 2, false)
        cont.fillStyle = this.color
        cont.fill()
        cont.restore()
    }

    // Updates the property of the particles
    update () {
        this.draw()
        this.velocity.x *= friction
        this.velocity.y *= friction
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
        this.alpha -= 0.01
    }
}

let player = new Player(x, y, 10, 'white')
let project_arr = []
let opp_arr = []
let particle_arr = []

function init() {
    player = new Player(x, y, 10, 'white')
    project_arr = []
    opp_arr = []
    particle_arr = []
    score = 0
    scoreEl.innerHTML = score
    bigScoreEl.innerHTML = score
}

function spawnOpponents() {
    setInterval(() => {

        // Radius' size is from 4 to 30 randomly
        const rad = Math.random() * (30 - 4) + 4
        let x
        let y
        
        // Calculates the spawn position of projectiles randomly and off the screen
        if (Math.random() < 0.5) {
            x = Math.random() < 0.5 ? 0 - rad : canvas.width + rad
            y = Math.random() * canvas.height
        } else {
            x = Math.random() * canvas.width
            y = Math.random() < 0.5 ? 0 - rad : canvas.height + rad
        }
        
        // Randomize the color of the opponents using Hue, Saturation, and Lighting function (hsl)
        const color = `hsl(${Math.random() * 360}, 50%, 50%)`

        // Create an angle variable to determiunt the angle of the projectile dynamically
        const angle = Math.atan2(canvas.height / 2 - y,
                                canvas.width / 2 - x)

        // Creates a velocity variable to calculate 
        // the velocity of each projectile using the angle dynamically
        const velocity = {
        x: Math.cos(angle),
        y: Math.sin(angle)
        }
        
        // Add the Opponent instances inside the opponents array
        opp_arr.push(new Opponent(x, y, rad, color, velocity))

    }, 1000)

    
}

let animationId
let score = 0

// Loop function to loop when animate is being called
function animate() {
    animationId = requestAnimationFrame(animate)

    // Set the color of the screen black, 
    // while giving the moving objects the fade effect
    cont.fillStyle = 'rgba(0, 0, 0, 0.1)'

    // Clear the canvas 
    cont.fillRect(0, 0, canvas.width, canvas.height)
    player.draw()

    particle_arr.forEach((particle, index) => {

        // Checks if a particle is to be removed from the screen
        if (particle.alpha <= 0) {
            particle_arr.splice(index, 1)
        } else {
            particle.update()
        }
        
    })

    // Loop through the array of projectiles and update each one
    project_arr.forEach((projectile, index) => {
        projectile.update()

        // Removes the projectile when it goes off the screen
        if (projectile.x - projectile.rad < 0 ||
            projectile.x - projectile.rad > canvas.width ||
            projectile.y + projectile.rad < 0 ||
            projectile.y - projectile.rad > canvas.height) {
                
            // Sets the Timeout to remove the flash effect when an event takes place 
            setTimeout(() => {
                // Remove the projectile on the screen
                project_arr.splice(index, 1)
            }, 0)
        }
    })
    
    // Loop through the array of opponents and update each one
    opp_arr.forEach((opponent, index) => {
        opponent.update()
        const dist = Math.hypot(player.x - opponent.x, player.y - opponent.y)

        // End Game
        if (dist - opponent.rad - player.rad < 0) {
            cancelAnimationFrame(animationId)
            modelEl.style.display = 'flex'
            bigScoreEl.innerHTML = score
        }

        // Loop through each projectile to calculate the distance between opponents
        project_arr.forEach((projectile, projIndex) => {
            const dist = Math.hypot(projectile.x - opponent.x, projectile.y - opponent.y)

            // Checks collision between each projectile and the opponent
            if (dist - opponent.rad - projectile.rad < 0) {

                // create explosions
                for (let i = 0; i < opponent.rad * 2; i++) {
                    particle_arr.push(new Particle(projectile.x, 
                                        projectile.y, 
                                        Math.random() * 2, 
                                        opponent.color,
                                        {
                                            x: (Math.random() - 0.5) * (Math.random() * 6),
                                            y: Math.random() - 0.5 * (Math.random() * 6)
                                        }))
                }

                // Checks whether to shrink the opponent when hit
                if (opponent.rad - 10 > 5) {
                    // Increase score and modify the score on the screen
                    score += 100
                    scoreEl.innerHTML = score
                    opponent.rad -= 10

                    /* Uses gsap to have a smooth transition between two frames
                       @ERROR: This does not work for some reason
                    gsap.to(opponent, {
                        radius: opponent.rad - 10
                    }) 
                    */

                    // Sets the Timeout to remove the flash effect when a collision takes place 
                    setTimeout(() => {
                        // Remove the projectile on the screen
                        project_arr.splice(projIndex, 1)
                    }, 0)

                } else {
                    // Increase score drastically
                    // when the opponent is completely destroyed
                    score += 250
                    scoreEl.innerHTML = score
                    setTimeout(() => {

                        // Remove the opponent and the projectile on the screen
                        opp_arr.splice(index, 1)
                        project_arr.splice(projIndex, 1)
                    }, 0)
                }
            }
        })
    })
}

// Listens to a click command
addEventListener('click', (event) => {
    
    // Create an angle variable to determine the angle of the projectile dynamically
    const angle = Math.atan2(event.clientY - canvas.height / 2,
                            event.clientX - canvas.width / 2)
    
    // Creates a velocity variable to calculate 
    // the velocity of each projectile using the angle dynamically
    const velocity = {
        x: Math.cos(angle) * 5,
        y: Math.sin(angle) * 5
    }

    // Adds a new Projectile instance inside the array of projectiles
    project_arr.push(
        new Projectile(
            canvas.width / 2, 
            canvas.height / 2, 
            5, 
            'white', 
            velocity)
    )
})

startGameBtn.addEventListener('click', () => {
    init()
    animate()
    spawnOpponents()
    modelEl.style.display = 'none'
})
