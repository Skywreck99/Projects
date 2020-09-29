.text
.global  set_tod_from_secs

## ENTRY POINT FOR REQUIRED FUNCTION
set_tod_from_secs:

  cmpl  $0,     %edi                         # If the time is negative
  jl    .ERROR

  cmpl  $86400, %edi                         # If the time is more than 24 hours
  jg    .ERROR

  movl        %edi,   %eax                   # %eax = TIME_OF_DAY_SEC
  movl        $3600,  %ecx                   # %ecx = 3600
  cqto
  idivl       %ecx                           # %eax = %eax / $3600
  movl        %eax,   %r8d                   # %r8d = %eax / $3600 (for future use)
  movl        %edx,   %r9d                   # %r9d = %eax % $3600 (for future use)

  cmpl  $43199, %edi                         # If the time is in the evening
  jg    .EVENING_HOURS
                                             # If the time is in the morning
  cmpl   $0,    %eax                         # time_of_day_sec / 3600 == 0
  je     .MIDNIGHT

  movw   %ax,  0(%rsi)                       # tod->hours = time_of_day_sec / 3600
  movb   $0,   6(%rsi)                       # tod->ispm = 0;
  jmp    .MIN_AND_SEC

.EVENING_HOURS:
  movl        $12,    %ecx                   # %ecx = 12
  cqto
  idivl       %ecx                           # %eax = %eax / %ecx
  cmpl        $0,     %edx                   # %edx = (time_of_day_sec / 3600) % 12
  je          .NOON

  movl        %r8d,   %eax
  subl        $12,    %eax                   # %eax = %eax - 12
  movw        %ax,    0(%rsi)                # tod->hours = (time_of_day_sec / 3600) - 12
  movb        $1,     6(%rsi)                # tod->ispm = 1;
  jmp         .MIN_AND_SEC

.ERROR:                                      # return 1 when Error
  movl        $1,     %eax
  ret

.NOON:                                       # Change hours to 12 when at noon
  movw        $12,    0(%rsi)                # tod->hours = 12
  movb        $1,     6(%rsi)                # tod->ispm = 1;
  jmp         .MIN_AND_SEC

.MIDNIGHT:                                   # Change hours to 12 when midnight
  movw        $12,    0(%rsi)                # tod->hours = 12
  movb        $0,     6(%rsi)                # tod->ispm = 0;
  jmp         .MIN_AND_SEC

.MIN_AND_SEC:                                # CALCULATING FOR TOD->MINUTES AND TOD->SECONDS
  movl        %r9d,   %eax                   # %eax = %eax % 3600
  cqto
  movl        $60,    %ecx                   # %ecx = 60
  idivl       %ecx                           # %eax = %eax / %ecx
  movw        %ax,   2(%rsi)                 # tod->minutes = (time_of_day_sec % 3600) / 60
  movw        %dx,   4(%rsi)                 # tod->seconds = (time_of_day_sec % 3600) % 60
  movl        $0,     %eax                   # return 0 when successful
  movl        $0,     %r8d
  ret

### Data area associated with the next function
.data
masks:
  .int 0b0111111                # 0 digit
  .int 0b0000110                # 1 digit
  .int 0b1011011                # 2 digit
  .int 0b1001111                # 3 digit
  .int 0b1100110                # 4 digit
  .int 0b1101101                # 5 digit
  .int 0b1111101                # 6 digit
  .int 0b0000111                # 7 digit
  .int 0b1111111                # 8 digit
  .int 0b1101111                # 9 digit
  .int 0b0000000                # Blank digit

.text
.global  set_display_bits_from_tod

## ENTRY POINT FOR REQUIRED FUNCTION
set_display_bits_from_tod:

        leaq      masks(%rip),%r11           # int masks[10]

        movq      %rdi,       %r8            # tod.seconds
        shrq      $32,        %r8
        andq      $0xFFFF,    %r8
        cmpl      $0,         %r8d
        jl        .ERROR
        cmpl      $59,        %r8d
        jg        .ERROR

        movq      $0,         %r8
        movq      %rdi,       %r8            # tod.minutes
        shrq      $16,        %r8
        andq      $0xFFFF,    %r8
        cmpl      $0,         %r8d
        jl        .ERROR
        cmpl      $59,        %r8d
        jg        .ERROR
                                             # SETTING UP THE DIGITS
        movl      $10,        %ecx
        movl      %r8d,       %eax
        cqto
        idivl     %ecx

        movl      (%r11,%rdx,4), %edx       # masks[min_ones]
        movl      %edx,         (%rsi)      # *display = masks[min_ones]
        movl      (%r11,%rax,4), %eax        # masks[min_tens]
        shll      $7,            %eax
        orl       %eax,       (%rsi)         # *display = (masks[min_tens] << 7) | *display

        movq      $0,         %r8
        movq      %rdi,       %r8            # tod.hours
        andq      $0xFFFF,    %r8
        cmpl      $0,         %r8d
        jl        .ERROR
        cmpl      $12,        %r8d
        jg        .ERROR

        movl      %r8d,       %eax
        cqto
        idivl     %ecx

        movl      (%r11,%rdx,4), %edx
        shll      $14,         %edx
        orl       %edx,       (%rsi)        # *display = (masks[hour_ones] << 14) | *display
        cmpl      $0,         %eax
        je        .BLANK
        movl      (%r11,%rax,4),  %eax
        shll      $21,        %eax
        orl       %eax,       (%rsi)         # *display = (masks[hour_tens] << 21) | *display

.ISPM:
  movq      %rdi,       %r8
  shrq      $48,        %r8
  andq      $0xFF,    %r8
  cmpl      $1,         %r8d
  je        .PM
  movl  $1,             %eax
  shll  $28,            %eax
  orl   %eax,           (%rsi)               # *display = (0b01 << 28) | *display

.END:
  movl  $0,       %eax
  ret

.PM:
  movl  $2,       %eax
  shll  $28,      %eax
  orl   %eax,     (%rsi)                     # *display = (0b10 << 28) | *display
  jmp   .END

.BLANK:                                      # triggered in the morning before 10 am
  movl  $0,       %eax
  shll  $21,      %eax
  orl   %eax,     (%rsi)
  jmp   .ISPM

.text
.global clock_update

## ENTRY POINT FOR REQUIRED FUNCTION
clock_update:
	## assembly instructions here
  pushq $0                                    # initializes the value of %rsp for be used later
  movl  TIME_OF_DAY_SEC(%rip),  %edi          # %edi = TIME_OF_DAY_SEC
  movq  %rsp, %rsi                            # %rsi = %rsp (address allocated for tod)
  call  set_tod_from_secs

  cmpl  $1,   %eax                            # if result is 1 then return 1
  je    .OOB

  movq  (%rsi), %rdi                          # %rdi = (%rsi) (packed address for tod)
  movq  %rsp,  %rsi                           # %rsi = %rsp (address allocated for CLOCK_DISPLAY_PORT)
  call  set_display_bits_from_tod

  cmpl  $1,   %eax                            # if result is 1 then return 1
  je    .OOB

  popq  %rdx                                  # %rdx holds the value of modified CLOCK_DISPLAY_PORT
  movl  %edx, CLOCK_DISPLAY_PORT(%rip)        # Modify the old value of CLOCK_DISPLAY_PORT with a new one

  movl  $0, %eax
  ret

.OOB:
  movl  $1, %eax
  popq  %rdx
  ret
