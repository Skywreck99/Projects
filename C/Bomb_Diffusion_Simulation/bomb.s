
bomb:     file format elf64-x86-64


Disassembly of section .init:

0000000000001b90 <_init>:
    1b90:	48 83 ec 08          	sub    $0x8,%rsp
    1b94:	48 8b 05 4d 44 20 00 	mov    0x20444d(%rip),%rax        # 205fe8 <__gmon_start__>
    1b9b:	48 85 c0             	test   %rax,%rax
    1b9e:	74 02                	je     1ba2 <_init+0x12>
    1ba0:	ff d0                	callq  *%rax
    1ba2:	48 83 c4 08          	add    $0x8,%rsp
    1ba6:	c3                   	retq   

Disassembly of section .plt:

0000000000001bb0 <.plt>:
    1bb0:	ff 35 32 43 20 00    	pushq  0x204332(%rip)        # 205ee8 <_GLOBAL_OFFSET_TABLE_+0x8>
    1bb6:	ff 25 34 43 20 00    	jmpq   *0x204334(%rip)        # 205ef0 <_GLOBAL_OFFSET_TABLE_+0x10>
    1bbc:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000001bc0 <getenv@plt>:
    1bc0:	ff 25 32 43 20 00    	jmpq   *0x204332(%rip)        # 205ef8 <getenv@GLIBC_2.2.5>
    1bc6:	68 00 00 00 00       	pushq  $0x0
    1bcb:	e9 e0 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001bd0 <__snprintf_chk@plt>:
    1bd0:	ff 25 2a 43 20 00    	jmpq   *0x20432a(%rip)        # 205f00 <__snprintf_chk@GLIBC_2.3.4>
    1bd6:	68 01 00 00 00       	pushq  $0x1
    1bdb:	e9 d0 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001be0 <strcasecmp@plt>:
    1be0:	ff 25 22 43 20 00    	jmpq   *0x204322(%rip)        # 205f08 <strcasecmp@GLIBC_2.2.5>
    1be6:	68 02 00 00 00       	pushq  $0x2
    1beb:	e9 c0 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001bf0 <__errno_location@plt>:
    1bf0:	ff 25 1a 43 20 00    	jmpq   *0x20431a(%rip)        # 205f10 <__errno_location@GLIBC_2.2.5>
    1bf6:	68 03 00 00 00       	pushq  $0x3
    1bfb:	e9 b0 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c00 <strcpy@plt>:
    1c00:	ff 25 12 43 20 00    	jmpq   *0x204312(%rip)        # 205f18 <strcpy@GLIBC_2.2.5>
    1c06:	68 04 00 00 00       	pushq  $0x4
    1c0b:	e9 a0 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c10 <puts@plt>:
    1c10:	ff 25 0a 43 20 00    	jmpq   *0x20430a(%rip)        # 205f20 <puts@GLIBC_2.2.5>
    1c16:	68 05 00 00 00       	pushq  $0x5
    1c1b:	e9 90 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c20 <write@plt>:
    1c20:	ff 25 02 43 20 00    	jmpq   *0x204302(%rip)        # 205f28 <write@GLIBC_2.2.5>
    1c26:	68 06 00 00 00       	pushq  $0x6
    1c2b:	e9 80 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c30 <__stack_chk_fail@plt>:
    1c30:	ff 25 fa 42 20 00    	jmpq   *0x2042fa(%rip)        # 205f30 <__stack_chk_fail@GLIBC_2.4>
    1c36:	68 07 00 00 00       	pushq  $0x7
    1c3b:	e9 70 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c40 <alarm@plt>:
    1c40:	ff 25 f2 42 20 00    	jmpq   *0x2042f2(%rip)        # 205f38 <alarm@GLIBC_2.2.5>
    1c46:	68 08 00 00 00       	pushq  $0x8
    1c4b:	e9 60 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c50 <close@plt>:
    1c50:	ff 25 ea 42 20 00    	jmpq   *0x2042ea(%rip)        # 205f40 <close@GLIBC_2.2.5>
    1c56:	68 09 00 00 00       	pushq  $0x9
    1c5b:	e9 50 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c60 <read@plt>:
    1c60:	ff 25 e2 42 20 00    	jmpq   *0x2042e2(%rip)        # 205f48 <read@GLIBC_2.2.5>
    1c66:	68 0a 00 00 00       	pushq  $0xa
    1c6b:	e9 40 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c70 <fgets@plt>:
    1c70:	ff 25 da 42 20 00    	jmpq   *0x2042da(%rip)        # 205f50 <fgets@GLIBC_2.2.5>
    1c76:	68 0b 00 00 00       	pushq  $0xb
    1c7b:	e9 30 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c80 <signal@plt>:
    1c80:	ff 25 d2 42 20 00    	jmpq   *0x2042d2(%rip)        # 205f58 <signal@GLIBC_2.2.5>
    1c86:	68 0c 00 00 00       	pushq  $0xc
    1c8b:	e9 20 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001c90 <gethostbyname@plt>:
    1c90:	ff 25 ca 42 20 00    	jmpq   *0x2042ca(%rip)        # 205f60 <gethostbyname@GLIBC_2.2.5>
    1c96:	68 0d 00 00 00       	pushq  $0xd
    1c9b:	e9 10 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001ca0 <__memmove_chk@plt>:
    1ca0:	ff 25 c2 42 20 00    	jmpq   *0x2042c2(%rip)        # 205f68 <__memmove_chk@GLIBC_2.3.4>
    1ca6:	68 0e 00 00 00       	pushq  $0xe
    1cab:	e9 00 ff ff ff       	jmpq   1bb0 <.plt>

0000000000001cb0 <strtol@plt>:
    1cb0:	ff 25 ba 42 20 00    	jmpq   *0x2042ba(%rip)        # 205f70 <strtol@GLIBC_2.2.5>
    1cb6:	68 0f 00 00 00       	pushq  $0xf
    1cbb:	e9 f0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001cc0 <fflush@plt>:
    1cc0:	ff 25 b2 42 20 00    	jmpq   *0x2042b2(%rip)        # 205f78 <fflush@GLIBC_2.2.5>
    1cc6:	68 10 00 00 00       	pushq  $0x10
    1ccb:	e9 e0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001cd0 <__isoc99_sscanf@plt>:
    1cd0:	ff 25 aa 42 20 00    	jmpq   *0x2042aa(%rip)        # 205f80 <__isoc99_sscanf@GLIBC_2.7>
    1cd6:	68 11 00 00 00       	pushq  $0x11
    1cdb:	e9 d0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001ce0 <__printf_chk@plt>:
    1ce0:	ff 25 a2 42 20 00    	jmpq   *0x2042a2(%rip)        # 205f88 <__printf_chk@GLIBC_2.3.4>
    1ce6:	68 12 00 00 00       	pushq  $0x12
    1ceb:	e9 c0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001cf0 <fopen@plt>:
    1cf0:	ff 25 9a 42 20 00    	jmpq   *0x20429a(%rip)        # 205f90 <fopen@GLIBC_2.2.5>
    1cf6:	68 13 00 00 00       	pushq  $0x13
    1cfb:	e9 b0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d00 <gethostname@plt>:
    1d00:	ff 25 92 42 20 00    	jmpq   *0x204292(%rip)        # 205f98 <gethostname@GLIBC_2.2.5>
    1d06:	68 14 00 00 00       	pushq  $0x14
    1d0b:	e9 a0 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d10 <exit@plt>:
    1d10:	ff 25 8a 42 20 00    	jmpq   *0x20428a(%rip)        # 205fa0 <exit@GLIBC_2.2.5>
    1d16:	68 15 00 00 00       	pushq  $0x15
    1d1b:	e9 90 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d20 <connect@plt>:
    1d20:	ff 25 82 42 20 00    	jmpq   *0x204282(%rip)        # 205fa8 <connect@GLIBC_2.2.5>
    1d26:	68 16 00 00 00       	pushq  $0x16
    1d2b:	e9 80 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d30 <__fprintf_chk@plt>:
    1d30:	ff 25 7a 42 20 00    	jmpq   *0x20427a(%rip)        # 205fb0 <__fprintf_chk@GLIBC_2.3.4>
    1d36:	68 17 00 00 00       	pushq  $0x17
    1d3b:	e9 70 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d40 <sleep@plt>:
    1d40:	ff 25 72 42 20 00    	jmpq   *0x204272(%rip)        # 205fb8 <sleep@GLIBC_2.2.5>
    1d46:	68 18 00 00 00       	pushq  $0x18
    1d4b:	e9 60 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d50 <__ctype_b_loc@plt>:
    1d50:	ff 25 6a 42 20 00    	jmpq   *0x20426a(%rip)        # 205fc0 <__ctype_b_loc@GLIBC_2.3>
    1d56:	68 19 00 00 00       	pushq  $0x19
    1d5b:	e9 50 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d60 <__sprintf_chk@plt>:
    1d60:	ff 25 62 42 20 00    	jmpq   *0x204262(%rip)        # 205fc8 <__sprintf_chk@GLIBC_2.3.4>
    1d66:	68 1a 00 00 00       	pushq  $0x1a
    1d6b:	e9 40 fe ff ff       	jmpq   1bb0 <.plt>

0000000000001d70 <socket@plt>:
    1d70:	ff 25 5a 42 20 00    	jmpq   *0x20425a(%rip)        # 205fd0 <socket@GLIBC_2.2.5>
    1d76:	68 1b 00 00 00       	pushq  $0x1b
    1d7b:	e9 30 fe ff ff       	jmpq   1bb0 <.plt>

Disassembly of section .plt.got:

0000000000001d80 <__cxa_finalize@plt>:
    1d80:	ff 25 72 42 20 00    	jmpq   *0x204272(%rip)        # 205ff8 <__cxa_finalize@GLIBC_2.2.5>
    1d86:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

0000000000001d90 <_start>:
    1d90:	31 ed                	xor    %ebp,%ebp
    1d92:	49 89 d1             	mov    %rdx,%r9
    1d95:	5e                   	pop    %rsi
    1d96:	48 89 e2             	mov    %rsp,%rdx
    1d99:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    1d9d:	50                   	push   %rax
    1d9e:	54                   	push   %rsp
    1d9f:	4c 8d 05 ba 1a 00 00 	lea    0x1aba(%rip),%r8        # 3860 <__libc_csu_fini>
    1da6:	48 8d 0d 43 1a 00 00 	lea    0x1a43(%rip),%rcx        # 37f0 <__libc_csu_init>
    1dad:	48 8d 3d e6 00 00 00 	lea    0xe6(%rip),%rdi        # 1e9a <main>
    1db4:	ff 15 26 42 20 00    	callq  *0x204226(%rip)        # 205fe0 <__libc_start_main@GLIBC_2.2.5>
    1dba:	f4                   	hlt    
    1dbb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001dc0 <deregister_tm_clones>:
    1dc0:	48 8d 3d b9 4c 20 00 	lea    0x204cb9(%rip),%rdi        # 206a80 <stdout@@GLIBC_2.2.5>
    1dc7:	55                   	push   %rbp
    1dc8:	48 8d 05 b1 4c 20 00 	lea    0x204cb1(%rip),%rax        # 206a80 <stdout@@GLIBC_2.2.5>
    1dcf:	48 39 f8             	cmp    %rdi,%rax
    1dd2:	48 89 e5             	mov    %rsp,%rbp
    1dd5:	74 19                	je     1df0 <deregister_tm_clones+0x30>
    1dd7:	48 8b 05 fa 41 20 00 	mov    0x2041fa(%rip),%rax        # 205fd8 <_ITM_deregisterTMCloneTable>
    1dde:	48 85 c0             	test   %rax,%rax
    1de1:	74 0d                	je     1df0 <deregister_tm_clones+0x30>
    1de3:	5d                   	pop    %rbp
    1de4:	ff e0                	jmpq   *%rax
    1de6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    1ded:	00 00 00 
    1df0:	5d                   	pop    %rbp
    1df1:	c3                   	retq   
    1df2:	0f 1f 40 00          	nopl   0x0(%rax)
    1df6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    1dfd:	00 00 00 

0000000000001e00 <register_tm_clones>:
    1e00:	48 8d 3d 79 4c 20 00 	lea    0x204c79(%rip),%rdi        # 206a80 <stdout@@GLIBC_2.2.5>
    1e07:	48 8d 35 72 4c 20 00 	lea    0x204c72(%rip),%rsi        # 206a80 <stdout@@GLIBC_2.2.5>
    1e0e:	55                   	push   %rbp
    1e0f:	48 29 fe             	sub    %rdi,%rsi
    1e12:	48 89 e5             	mov    %rsp,%rbp
    1e15:	48 c1 fe 03          	sar    $0x3,%rsi
    1e19:	48 89 f0             	mov    %rsi,%rax
    1e1c:	48 c1 e8 3f          	shr    $0x3f,%rax
    1e20:	48 01 c6             	add    %rax,%rsi
    1e23:	48 d1 fe             	sar    %rsi
    1e26:	74 18                	je     1e40 <register_tm_clones+0x40>
    1e28:	48 8b 05 c1 41 20 00 	mov    0x2041c1(%rip),%rax        # 205ff0 <_ITM_registerTMCloneTable>
    1e2f:	48 85 c0             	test   %rax,%rax
    1e32:	74 0c                	je     1e40 <register_tm_clones+0x40>
    1e34:	5d                   	pop    %rbp
    1e35:	ff e0                	jmpq   *%rax
    1e37:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    1e3e:	00 00 
    1e40:	5d                   	pop    %rbp
    1e41:	c3                   	retq   
    1e42:	0f 1f 40 00          	nopl   0x0(%rax)
    1e46:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    1e4d:	00 00 00 

0000000000001e50 <__do_global_dtors_aux>:
    1e50:	80 3d 51 4c 20 00 00 	cmpb   $0x0,0x204c51(%rip)        # 206aa8 <completed.7697>
    1e57:	75 2f                	jne    1e88 <__do_global_dtors_aux+0x38>
    1e59:	48 83 3d 97 41 20 00 	cmpq   $0x0,0x204197(%rip)        # 205ff8 <__cxa_finalize@GLIBC_2.2.5>
    1e60:	00 
    1e61:	55                   	push   %rbp
    1e62:	48 89 e5             	mov    %rsp,%rbp
    1e65:	74 0c                	je     1e73 <__do_global_dtors_aux+0x23>
    1e67:	48 8b 3d 9a 41 20 00 	mov    0x20419a(%rip),%rdi        # 206008 <__dso_handle>
    1e6e:	e8 0d ff ff ff       	callq  1d80 <__cxa_finalize@plt>
    1e73:	e8 48 ff ff ff       	callq  1dc0 <deregister_tm_clones>
    1e78:	c6 05 29 4c 20 00 01 	movb   $0x1,0x204c29(%rip)        # 206aa8 <completed.7697>
    1e7f:	5d                   	pop    %rbp
    1e80:	c3                   	retq   
    1e81:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1e88:	f3 c3                	repz retq 
    1e8a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000001e90 <frame_dummy>:
    1e90:	55                   	push   %rbp
    1e91:	48 89 e5             	mov    %rsp,%rbp
    1e94:	5d                   	pop    %rbp
    1e95:	e9 66 ff ff ff       	jmpq   1e00 <register_tm_clones>

0000000000001e9a <main>:
    1e9a:	53                   	push   %rbx
    1e9b:	83 ff 01             	cmp    $0x1,%edi
    1e9e:	0f 84 f8 00 00 00    	je     1f9c <main+0x102>
    1ea4:	48 89 f3             	mov    %rsi,%rbx
    1ea7:	83 ff 02             	cmp    $0x2,%edi
    1eaa:	0f 85 21 01 00 00    	jne    1fd1 <main+0x137>
    1eb0:	48 8b 7e 08          	mov    0x8(%rsi),%rdi
    1eb4:	48 8d 35 c9 19 00 00 	lea    0x19c9(%rip),%rsi        # 3884 <_IO_stdin_used+0x4>
    1ebb:	e8 30 fe ff ff       	callq  1cf0 <fopen@plt>
    1ec0:	48 89 05 e9 4b 20 00 	mov    %rax,0x204be9(%rip)        # 206ab0 <infile>
    1ec7:	48 85 c0             	test   %rax,%rax
    1eca:	0f 84 df 00 00 00    	je     1faf <main+0x115>
    1ed0:	e8 5b 06 00 00       	callq  2530 <initialize_bomb>
    1ed5:	48 8d 3d 2c 1a 00 00 	lea    0x1a2c(%rip),%rdi        # 3908 <_IO_stdin_used+0x88>
    1edc:	e8 2f fd ff ff       	callq  1c10 <puts@plt>
    1ee1:	48 8d 3d 60 1a 00 00 	lea    0x1a60(%rip),%rdi        # 3948 <_IO_stdin_used+0xc8>
    1ee8:	e8 23 fd ff ff       	callq  1c10 <puts@plt>
    1eed:	e8 b2 09 00 00       	callq  28a4 <read_line>
    1ef2:	48 89 c7             	mov    %rax,%rdi
    1ef5:	e8 fa 00 00 00       	callq  1ff4 <phase_1>
    1efa:	e8 e9 0a 00 00       	callq  29e8 <phase_defused>
    1eff:	48 8d 3d 72 1a 00 00 	lea    0x1a72(%rip),%rdi        # 3978 <_IO_stdin_used+0xf8>
    1f06:	e8 05 fd ff ff       	callq  1c10 <puts@plt>
    1f0b:	e8 94 09 00 00       	callq  28a4 <read_line>
    1f10:	48 89 c7             	mov    %rax,%rdi
    1f13:	e8 fc 00 00 00       	callq  2014 <phase_2>
    1f18:	e8 cb 0a 00 00       	callq  29e8 <phase_defused>
    1f1d:	48 8d 3d 99 19 00 00 	lea    0x1999(%rip),%rdi        # 38bd <_IO_stdin_used+0x3d>
    1f24:	e8 e7 fc ff ff       	callq  1c10 <puts@plt>
    1f29:	e8 76 09 00 00       	callq  28a4 <read_line>
    1f2e:	48 89 c7             	mov    %rax,%rdi
    1f31:	e8 4c 01 00 00       	callq  2082 <phase_3>
    1f36:	e8 ad 0a 00 00       	callq  29e8 <phase_defused>
    1f3b:	48 8d 3d 99 19 00 00 	lea    0x1999(%rip),%rdi        # 38db <_IO_stdin_used+0x5b>
    1f42:	e8 c9 fc ff ff       	callq  1c10 <puts@plt>
    1f47:	e8 58 09 00 00       	callq  28a4 <read_line>
    1f4c:	48 89 c7             	mov    %rax,%rdi
    1f4f:	e8 1b 02 00 00       	callq  216f <phase_4>
    1f54:	e8 8f 0a 00 00       	callq  29e8 <phase_defused>
    1f59:	48 8d 3d 48 1a 00 00 	lea    0x1a48(%rip),%rdi        # 39a8 <_IO_stdin_used+0x128>
    1f60:	e8 ab fc ff ff       	callq  1c10 <puts@plt>
    1f65:	e8 3a 09 00 00       	callq  28a4 <read_line>
    1f6a:	48 89 c7             	mov    %rax,%rdi
    1f6d:	e8 6c 02 00 00       	callq  21de <phase_5>
    1f72:	e8 71 0a 00 00       	callq  29e8 <phase_defused>
    1f77:	48 8d 3d 6c 19 00 00 	lea    0x196c(%rip),%rdi        # 38ea <_IO_stdin_used+0x6a>
    1f7e:	e8 8d fc ff ff       	callq  1c10 <puts@plt>
    1f83:	e8 1c 09 00 00       	callq  28a4 <read_line>
    1f88:	48 89 c7             	mov    %rax,%rdi
    1f8b:	e8 e1 02 00 00       	callq  2271 <phase_6>
    1f90:	e8 53 0a 00 00       	callq  29e8 <phase_defused>
    1f95:	b8 00 00 00 00       	mov    $0x0,%eax
    1f9a:	5b                   	pop    %rbx
    1f9b:	c3                   	retq   
    1f9c:	48 8b 05 ed 4a 20 00 	mov    0x204aed(%rip),%rax        # 206a90 <stdin@@GLIBC_2.2.5>
    1fa3:	48 89 05 06 4b 20 00 	mov    %rax,0x204b06(%rip)        # 206ab0 <infile>
    1faa:	e9 21 ff ff ff       	jmpq   1ed0 <main+0x36>
    1faf:	48 8b 4b 08          	mov    0x8(%rbx),%rcx
    1fb3:	48 8b 13             	mov    (%rbx),%rdx
    1fb6:	48 8d 35 c9 18 00 00 	lea    0x18c9(%rip),%rsi        # 3886 <_IO_stdin_used+0x6>
    1fbd:	bf 01 00 00 00       	mov    $0x1,%edi
    1fc2:	e8 19 fd ff ff       	callq  1ce0 <__printf_chk@plt>
    1fc7:	bf 08 00 00 00       	mov    $0x8,%edi
    1fcc:	e8 3f fd ff ff       	callq  1d10 <exit@plt>
    1fd1:	48 8b 16             	mov    (%rsi),%rdx
    1fd4:	48 8d 35 c8 18 00 00 	lea    0x18c8(%rip),%rsi        # 38a3 <_IO_stdin_used+0x23>
    1fdb:	bf 01 00 00 00       	mov    $0x1,%edi
    1fe0:	b8 00 00 00 00       	mov    $0x0,%eax
    1fe5:	e8 f6 fc ff ff       	callq  1ce0 <__printf_chk@plt>
    1fea:	bf 08 00 00 00       	mov    $0x8,%edi
    1fef:	e8 1c fd ff ff       	callq  1d10 <exit@plt>

0000000000001ff4 <phase_1>:
    1ff4:	48 83 ec 08          	sub    $0x8,%rsp
    1ff8:	48 8d 35 cd 19 00 00 	lea    0x19cd(%rip),%rsi        # 39cc <_IO_stdin_used+0x14c>
    1fff:	e8 c5 04 00 00       	callq  24c9 <strings_not_equal>
    2004:	85 c0                	test   %eax,%eax
    2006:	75 05                	jne    200d <phase_1+0x19>
    2008:	48 83 c4 08          	add    $0x8,%rsp
    200c:	c3                   	retq   
    200d:	e8 15 08 00 00       	callq  2827 <explode_bomb>
    2012:	eb f4                	jmp    2008 <phase_1+0x14>

0000000000002014 <phase_2>:
    2014:	55                   	push   %rbp
    2015:	53                   	push   %rbx
    2016:	48 83 ec 28          	sub    $0x28,%rsp
    201a:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2021:	00 00 
    2023:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    2028:	31 c0                	xor    %eax,%eax
    202a:	48 89 e6             	mov    %rsp,%rsi
    202d:	e8 31 08 00 00       	callq  2863 <read_six_numbers>
    2032:	83 3c 24 00          	cmpl   $0x0,(%rsp)
    2036:	78 0a                	js     2042 <phase_2+0x2e>
    2038:	bb 01 00 00 00       	mov    $0x1,%ebx
    203d:	48 89 e5             	mov    %rsp,%rbp
    2040:	eb 11                	jmp    2053 <phase_2+0x3f>
    2042:	e8 e0 07 00 00       	callq  2827 <explode_bomb>
    2047:	eb ef                	jmp    2038 <phase_2+0x24>
    2049:	48 83 c3 01          	add    $0x1,%rbx
    204d:	48 83 fb 06          	cmp    $0x6,%rbx
    2051:	74 13                	je     2066 <phase_2+0x52>
    2053:	89 d8                	mov    %ebx,%eax
    2055:	03 44 9d fc          	add    -0x4(%rbp,%rbx,4),%eax
    2059:	39 44 9d 00          	cmp    %eax,0x0(%rbp,%rbx,4)
    205d:	74 ea                	je     2049 <phase_2+0x35>
    205f:	e8 c3 07 00 00       	callq  2827 <explode_bomb>
    2064:	eb e3                	jmp    2049 <phase_2+0x35>
    2066:	48 8b 44 24 18       	mov    0x18(%rsp),%rax
    206b:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    2072:	00 00 
    2074:	75 07                	jne    207d <phase_2+0x69>
    2076:	48 83 c4 28          	add    $0x28,%rsp
    207a:	5b                   	pop    %rbx
    207b:	5d                   	pop    %rbp
    207c:	c3                   	retq   
    207d:	e8 ae fb ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002082 <phase_3>:
    2082:	48 83 ec 18          	sub    $0x18,%rsp
    2086:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    208d:	00 00 
    208f:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    2094:	31 c0                	xor    %eax,%eax
    2096:	48 8d 4c 24 04       	lea    0x4(%rsp),%rcx
    209b:	48 89 e2             	mov    %rsp,%rdx
    209e:	48 8d 35 cf 1c 00 00 	lea    0x1ccf(%rip),%rsi        # 3d74 <array.3425+0x354>
    20a5:	e8 26 fc ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    20aa:	83 f8 01             	cmp    $0x1,%eax
    20ad:	7e 19                	jle    20c8 <phase_3+0x46>
    20af:	83 3c 24 07          	cmpl   $0x7,(%rsp)
    20b3:	77 4b                	ja     2100 <phase_3+0x7e>
    20b5:	8b 04 24             	mov    (%rsp),%eax
    20b8:	48 8d 15 41 19 00 00 	lea    0x1941(%rip),%rdx        # 3a00 <_IO_stdin_used+0x180>
    20bf:	48 63 04 82          	movslq (%rdx,%rax,4),%rax
    20c3:	48 01 d0             	add    %rdx,%rax
    20c6:	ff e0                	jmpq   *%rax
    20c8:	e8 5a 07 00 00       	callq  2827 <explode_bomb>
    20cd:	eb e0                	jmp    20af <phase_3+0x2d>
    20cf:	b8 96 03 00 00       	mov    $0x396,%eax
    20d4:	eb 3b                	jmp    2111 <phase_3+0x8f>
    20d6:	b8 91 03 00 00       	mov    $0x391,%eax
    20db:	eb 34                	jmp    2111 <phase_3+0x8f>
    20dd:	b8 49 02 00 00       	mov    $0x249,%eax
    20e2:	eb 2d                	jmp    2111 <phase_3+0x8f>
    20e4:	b8 65 00 00 00       	mov    $0x65,%eax
    20e9:	eb 26                	jmp    2111 <phase_3+0x8f>
    20eb:	b8 35 00 00 00       	mov    $0x35,%eax
    20f0:	eb 1f                	jmp    2111 <phase_3+0x8f>
    20f2:	b8 83 00 00 00       	mov    $0x83,%eax
    20f7:	eb 18                	jmp    2111 <phase_3+0x8f>
    20f9:	b8 93 00 00 00       	mov    $0x93,%eax
    20fe:	eb 11                	jmp    2111 <phase_3+0x8f>
    2100:	e8 22 07 00 00       	callq  2827 <explode_bomb>
    2105:	b8 00 00 00 00       	mov    $0x0,%eax
    210a:	eb 05                	jmp    2111 <phase_3+0x8f>
    210c:	b8 34 02 00 00       	mov    $0x234,%eax
    2111:	39 44 24 04          	cmp    %eax,0x4(%rsp)
    2115:	74 05                	je     211c <phase_3+0x9a>
    2117:	e8 0b 07 00 00       	callq  2827 <explode_bomb>
    211c:	48 8b 44 24 08       	mov    0x8(%rsp),%rax
    2121:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    2128:	00 00 
    212a:	75 05                	jne    2131 <phase_3+0xaf>
    212c:	48 83 c4 18          	add    $0x18,%rsp
    2130:	c3                   	retq   
    2131:	e8 fa fa ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002136 <func4>:
    2136:	b8 00 00 00 00       	mov    $0x0,%eax
    213b:	85 ff                	test   %edi,%edi
    213d:	7e 07                	jle    2146 <func4+0x10>
    213f:	89 f0                	mov    %esi,%eax
    2141:	83 ff 01             	cmp    $0x1,%edi
    2144:	75 02                	jne    2148 <func4+0x12>
    2146:	f3 c3                	repz retq 
    2148:	41 54                	push   %r12
    214a:	55                   	push   %rbp
    214b:	53                   	push   %rbx
    214c:	41 89 f4             	mov    %esi,%r12d
    214f:	89 fb                	mov    %edi,%ebx
    2151:	8d 7f ff             	lea    -0x1(%rdi),%edi
    2154:	e8 dd ff ff ff       	callq  2136 <func4>
    2159:	42 8d 2c 20          	lea    (%rax,%r12,1),%ebp
    215d:	8d 7b fe             	lea    -0x2(%rbx),%edi
    2160:	44 89 e6             	mov    %r12d,%esi
    2163:	e8 ce ff ff ff       	callq  2136 <func4>
    2168:	01 e8                	add    %ebp,%eax
    216a:	5b                   	pop    %rbx
    216b:	5d                   	pop    %rbp
    216c:	41 5c                	pop    %r12
    216e:	c3                   	retq   

000000000000216f <phase_4>:
    216f:	48 83 ec 18          	sub    $0x18,%rsp
    2173:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    217a:	00 00 
    217c:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    2181:	31 c0                	xor    %eax,%eax
    2183:	48 89 e1             	mov    %rsp,%rcx
    2186:	48 8d 54 24 04       	lea    0x4(%rsp),%rdx
    218b:	48 8d 35 e2 1b 00 00 	lea    0x1be2(%rip),%rsi        # 3d74 <array.3425+0x354>
    2192:	e8 39 fb ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    2197:	83 f8 02             	cmp    $0x2,%eax
    219a:	75 0b                	jne    21a7 <phase_4+0x38>
    219c:	8b 04 24             	mov    (%rsp),%eax
    219f:	83 e8 02             	sub    $0x2,%eax
    21a2:	83 f8 02             	cmp    $0x2,%eax
    21a5:	76 05                	jbe    21ac <phase_4+0x3d>
    21a7:	e8 7b 06 00 00       	callq  2827 <explode_bomb>
    21ac:	8b 34 24             	mov    (%rsp),%esi
    21af:	bf 09 00 00 00       	mov    $0x9,%edi
    21b4:	e8 7d ff ff ff       	callq  2136 <func4>
    21b9:	39 44 24 04          	cmp    %eax,0x4(%rsp)
    21bd:	74 05                	je     21c4 <phase_4+0x55>
    21bf:	e8 63 06 00 00       	callq  2827 <explode_bomb>
    21c4:	48 8b 44 24 08       	mov    0x8(%rsp),%rax
    21c9:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    21d0:	00 00 
    21d2:	75 05                	jne    21d9 <phase_4+0x6a>
    21d4:	48 83 c4 18          	add    $0x18,%rsp
    21d8:	c3                   	retq   
    21d9:	e8 52 fa ff ff       	callq  1c30 <__stack_chk_fail@plt>

00000000000021de <phase_5>:
    21de:	48 83 ec 18          	sub    $0x18,%rsp
    21e2:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    21e9:	00 00 
    21eb:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    21f0:	31 c0                	xor    %eax,%eax
    21f2:	48 8d 4c 24 04       	lea    0x4(%rsp),%rcx
    21f7:	48 89 e2             	mov    %rsp,%rdx
    21fa:	48 8d 35 73 1b 00 00 	lea    0x1b73(%rip),%rsi        # 3d74 <array.3425+0x354>
    2201:	e8 ca fa ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    2206:	83 f8 01             	cmp    $0x1,%eax
    2209:	7e 5a                	jle    2265 <phase_5+0x87>
    220b:	8b 04 24             	mov    (%rsp),%eax
    220e:	83 e0 0f             	and    $0xf,%eax
    2211:	89 04 24             	mov    %eax,(%rsp)
    2214:	83 f8 0f             	cmp    $0xf,%eax
    2217:	74 32                	je     224b <phase_5+0x6d>
    2219:	b9 00 00 00 00       	mov    $0x0,%ecx
    221e:	ba 00 00 00 00       	mov    $0x0,%edx
    2223:	48 8d 35 f6 17 00 00 	lea    0x17f6(%rip),%rsi        # 3a20 <array.3425>
    222a:	83 c2 01             	add    $0x1,%edx
    222d:	48 98                	cltq   
    222f:	8b 04 86             	mov    (%rsi,%rax,4),%eax
    2232:	01 c1                	add    %eax,%ecx
    2234:	83 f8 0f             	cmp    $0xf,%eax
    2237:	75 f1                	jne    222a <phase_5+0x4c>
    2239:	c7 04 24 0f 00 00 00 	movl   $0xf,(%rsp)
    2240:	83 fa 0f             	cmp    $0xf,%edx
    2243:	75 06                	jne    224b <phase_5+0x6d>
    2245:	39 4c 24 04          	cmp    %ecx,0x4(%rsp)
    2249:	74 05                	je     2250 <phase_5+0x72>
    224b:	e8 d7 05 00 00       	callq  2827 <explode_bomb>
    2250:	48 8b 44 24 08       	mov    0x8(%rsp),%rax
    2255:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    225c:	00 00 
    225e:	75 0c                	jne    226c <phase_5+0x8e>
    2260:	48 83 c4 18          	add    $0x18,%rsp
    2264:	c3                   	retq   
    2265:	e8 bd 05 00 00       	callq  2827 <explode_bomb>
    226a:	eb 9f                	jmp    220b <phase_5+0x2d>
    226c:	e8 bf f9 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002271 <phase_6>:
    2271:	41 55                	push   %r13
    2273:	41 54                	push   %r12
    2275:	55                   	push   %rbp
    2276:	53                   	push   %rbx
    2277:	48 83 ec 68          	sub    $0x68,%rsp
    227b:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2282:	00 00 
    2284:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
    2289:	31 c0                	xor    %eax,%eax
    228b:	49 89 e4             	mov    %rsp,%r12
    228e:	4c 89 e6             	mov    %r12,%rsi
    2291:	e8 cd 05 00 00       	callq  2863 <read_six_numbers>
    2296:	41 bd 00 00 00 00    	mov    $0x0,%r13d
    229c:	eb 25                	jmp    22c3 <phase_6+0x52>
    229e:	e8 84 05 00 00       	callq  2827 <explode_bomb>
    22a3:	eb 2d                	jmp    22d2 <phase_6+0x61>
    22a5:	83 c3 01             	add    $0x1,%ebx
    22a8:	83 fb 05             	cmp    $0x5,%ebx
    22ab:	7f 12                	jg     22bf <phase_6+0x4e>
    22ad:	48 63 c3             	movslq %ebx,%rax
    22b0:	8b 04 84             	mov    (%rsp,%rax,4),%eax
    22b3:	39 45 00             	cmp    %eax,0x0(%rbp)
    22b6:	75 ed                	jne    22a5 <phase_6+0x34>
    22b8:	e8 6a 05 00 00       	callq  2827 <explode_bomb>
    22bd:	eb e6                	jmp    22a5 <phase_6+0x34>
    22bf:	49 83 c4 04          	add    $0x4,%r12
    22c3:	4c 89 e5             	mov    %r12,%rbp
    22c6:	41 8b 04 24          	mov    (%r12),%eax
    22ca:	83 e8 01             	sub    $0x1,%eax
    22cd:	83 f8 05             	cmp    $0x5,%eax
    22d0:	77 cc                	ja     229e <phase_6+0x2d>
    22d2:	41 83 c5 01          	add    $0x1,%r13d
    22d6:	41 83 fd 06          	cmp    $0x6,%r13d
    22da:	74 35                	je     2311 <phase_6+0xa0>
    22dc:	44 89 eb             	mov    %r13d,%ebx
    22df:	eb cc                	jmp    22ad <phase_6+0x3c>
    22e1:	48 8b 52 08          	mov    0x8(%rdx),%rdx
    22e5:	83 c0 01             	add    $0x1,%eax
    22e8:	39 c8                	cmp    %ecx,%eax
    22ea:	75 f5                	jne    22e1 <phase_6+0x70>
    22ec:	48 89 54 f4 20       	mov    %rdx,0x20(%rsp,%rsi,8)
    22f1:	48 83 c6 01          	add    $0x1,%rsi
    22f5:	48 83 fe 06          	cmp    $0x6,%rsi
    22f9:	74 1d                	je     2318 <phase_6+0xa7>
    22fb:	8b 0c b4             	mov    (%rsp,%rsi,4),%ecx
    22fe:	b8 01 00 00 00       	mov    $0x1,%eax
    2303:	48 8d 15 26 3f 20 00 	lea    0x203f26(%rip),%rdx        # 206230 <node1>
    230a:	83 f9 01             	cmp    $0x1,%ecx
    230d:	7f d2                	jg     22e1 <phase_6+0x70>
    230f:	eb db                	jmp    22ec <phase_6+0x7b>
    2311:	be 00 00 00 00       	mov    $0x0,%esi
    2316:	eb e3                	jmp    22fb <phase_6+0x8a>
    2318:	48 8b 5c 24 20       	mov    0x20(%rsp),%rbx
    231d:	48 8b 44 24 28       	mov    0x28(%rsp),%rax
    2322:	48 89 43 08          	mov    %rax,0x8(%rbx)
    2326:	48 8b 54 24 30       	mov    0x30(%rsp),%rdx
    232b:	48 89 50 08          	mov    %rdx,0x8(%rax)
    232f:	48 8b 44 24 38       	mov    0x38(%rsp),%rax
    2334:	48 89 42 08          	mov    %rax,0x8(%rdx)
    2338:	48 8b 54 24 40       	mov    0x40(%rsp),%rdx
    233d:	48 89 50 08          	mov    %rdx,0x8(%rax)
    2341:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
    2346:	48 89 42 08          	mov    %rax,0x8(%rdx)
    234a:	48 c7 40 08 00 00 00 	movq   $0x0,0x8(%rax)
    2351:	00 
    2352:	bd 05 00 00 00       	mov    $0x5,%ebp
    2357:	eb 09                	jmp    2362 <phase_6+0xf1>
    2359:	48 8b 5b 08          	mov    0x8(%rbx),%rbx
    235d:	83 ed 01             	sub    $0x1,%ebp
    2360:	74 11                	je     2373 <phase_6+0x102>
    2362:	48 8b 43 08          	mov    0x8(%rbx),%rax
    2366:	8b 00                	mov    (%rax),%eax
    2368:	39 03                	cmp    %eax,(%rbx)
    236a:	7e ed                	jle    2359 <phase_6+0xe8>
    236c:	e8 b6 04 00 00       	callq  2827 <explode_bomb>
    2371:	eb e6                	jmp    2359 <phase_6+0xe8>
    2373:	48 8b 44 24 58       	mov    0x58(%rsp),%rax
    2378:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    237f:	00 00 
    2381:	75 0b                	jne    238e <phase_6+0x11d>
    2383:	48 83 c4 68          	add    $0x68,%rsp
    2387:	5b                   	pop    %rbx
    2388:	5d                   	pop    %rbp
    2389:	41 5c                	pop    %r12
    238b:	41 5d                	pop    %r13
    238d:	c3                   	retq   
    238e:	e8 9d f8 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002393 <fun7>:
    2393:	48 85 ff             	test   %rdi,%rdi
    2396:	74 34                	je     23cc <fun7+0x39>
    2398:	48 83 ec 08          	sub    $0x8,%rsp
    239c:	8b 17                	mov    (%rdi),%edx
    239e:	39 f2                	cmp    %esi,%edx
    23a0:	7f 0e                	jg     23b0 <fun7+0x1d>
    23a2:	b8 00 00 00 00       	mov    $0x0,%eax
    23a7:	39 f2                	cmp    %esi,%edx
    23a9:	75 12                	jne    23bd <fun7+0x2a>
    23ab:	48 83 c4 08          	add    $0x8,%rsp
    23af:	c3                   	retq   
    23b0:	48 8b 7f 08          	mov    0x8(%rdi),%rdi
    23b4:	e8 da ff ff ff       	callq  2393 <fun7>
    23b9:	01 c0                	add    %eax,%eax
    23bb:	eb ee                	jmp    23ab <fun7+0x18>
    23bd:	48 8b 7f 10          	mov    0x10(%rdi),%rdi
    23c1:	e8 cd ff ff ff       	callq  2393 <fun7>
    23c6:	8d 44 00 01          	lea    0x1(%rax,%rax,1),%eax
    23ca:	eb df                	jmp    23ab <fun7+0x18>
    23cc:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    23d1:	c3                   	retq   

00000000000023d2 <secret_phase>:
    23d2:	53                   	push   %rbx
    23d3:	e8 cc 04 00 00       	callq  28a4 <read_line>
    23d8:	ba 0a 00 00 00       	mov    $0xa,%edx
    23dd:	be 00 00 00 00       	mov    $0x0,%esi
    23e2:	48 89 c7             	mov    %rax,%rdi
    23e5:	e8 c6 f8 ff ff       	callq  1cb0 <strtol@plt>
    23ea:	48 89 c3             	mov    %rax,%rbx
    23ed:	8d 40 ff             	lea    -0x1(%rax),%eax
    23f0:	3d e8 03 00 00       	cmp    $0x3e8,%eax
    23f5:	77 2b                	ja     2422 <secret_phase+0x50>
    23f7:	89 de                	mov    %ebx,%esi
    23f9:	48 8d 3d 50 3d 20 00 	lea    0x203d50(%rip),%rdi        # 206150 <n1>
    2400:	e8 8e ff ff ff       	callq  2393 <fun7>
    2405:	83 f8 03             	cmp    $0x3,%eax
    2408:	74 05                	je     240f <secret_phase+0x3d>
    240a:	e8 18 04 00 00       	callq  2827 <explode_bomb>
    240f:	48 8d 3d 4a 16 00 00 	lea    0x164a(%rip),%rdi        # 3a60 <array.3425+0x40>
    2416:	e8 f5 f7 ff ff       	callq  1c10 <puts@plt>
    241b:	e8 c8 05 00 00       	callq  29e8 <phase_defused>
    2420:	5b                   	pop    %rbx
    2421:	c3                   	retq   
    2422:	e8 00 04 00 00       	callq  2827 <explode_bomb>
    2427:	eb ce                	jmp    23f7 <secret_phase+0x25>

0000000000002429 <sig_handler>:
    2429:	48 83 ec 08          	sub    $0x8,%rsp
    242d:	48 8d 3d 54 16 00 00 	lea    0x1654(%rip),%rdi        # 3a88 <array.3425+0x68>
    2434:	e8 d7 f7 ff ff       	callq  1c10 <puts@plt>
    2439:	bf 03 00 00 00       	mov    $0x3,%edi
    243e:	e8 fd f8 ff ff       	callq  1d40 <sleep@plt>
    2443:	48 8d 35 84 18 00 00 	lea    0x1884(%rip),%rsi        # 3cce <array.3425+0x2ae>
    244a:	bf 01 00 00 00       	mov    $0x1,%edi
    244f:	b8 00 00 00 00       	mov    $0x0,%eax
    2454:	e8 87 f8 ff ff       	callq  1ce0 <__printf_chk@plt>
    2459:	48 8b 3d 20 46 20 00 	mov    0x204620(%rip),%rdi        # 206a80 <stdout@@GLIBC_2.2.5>
    2460:	e8 5b f8 ff ff       	callq  1cc0 <fflush@plt>
    2465:	bf 01 00 00 00       	mov    $0x1,%edi
    246a:	e8 d1 f8 ff ff       	callq  1d40 <sleep@plt>
    246f:	48 8d 3d 60 18 00 00 	lea    0x1860(%rip),%rdi        # 3cd6 <array.3425+0x2b6>
    2476:	e8 95 f7 ff ff       	callq  1c10 <puts@plt>
    247b:	bf 10 00 00 00       	mov    $0x10,%edi
    2480:	e8 8b f8 ff ff       	callq  1d10 <exit@plt>

0000000000002485 <invalid_phase>:
    2485:	48 83 ec 08          	sub    $0x8,%rsp
    2489:	48 89 fa             	mov    %rdi,%rdx
    248c:	48 8d 35 4b 18 00 00 	lea    0x184b(%rip),%rsi        # 3cde <array.3425+0x2be>
    2493:	bf 01 00 00 00       	mov    $0x1,%edi
    2498:	b8 00 00 00 00       	mov    $0x0,%eax
    249d:	e8 3e f8 ff ff       	callq  1ce0 <__printf_chk@plt>
    24a2:	bf 08 00 00 00       	mov    $0x8,%edi
    24a7:	e8 64 f8 ff ff       	callq  1d10 <exit@plt>

00000000000024ac <string_length>:
    24ac:	80 3f 00             	cmpb   $0x0,(%rdi)
    24af:	74 12                	je     24c3 <string_length+0x17>
    24b1:	48 89 fa             	mov    %rdi,%rdx
    24b4:	48 83 c2 01          	add    $0x1,%rdx
    24b8:	89 d0                	mov    %edx,%eax
    24ba:	29 f8                	sub    %edi,%eax
    24bc:	80 3a 00             	cmpb   $0x0,(%rdx)
    24bf:	75 f3                	jne    24b4 <string_length+0x8>
    24c1:	f3 c3                	repz retq 
    24c3:	b8 00 00 00 00       	mov    $0x0,%eax
    24c8:	c3                   	retq   

00000000000024c9 <strings_not_equal>:
    24c9:	41 54                	push   %r12
    24cb:	55                   	push   %rbp
    24cc:	53                   	push   %rbx
    24cd:	48 89 fb             	mov    %rdi,%rbx
    24d0:	48 89 f5             	mov    %rsi,%rbp
    24d3:	e8 d4 ff ff ff       	callq  24ac <string_length>
    24d8:	41 89 c4             	mov    %eax,%r12d
    24db:	48 89 ef             	mov    %rbp,%rdi
    24de:	e8 c9 ff ff ff       	callq  24ac <string_length>
    24e3:	ba 01 00 00 00       	mov    $0x1,%edx
    24e8:	41 39 c4             	cmp    %eax,%r12d
    24eb:	74 07                	je     24f4 <strings_not_equal+0x2b>
    24ed:	89 d0                	mov    %edx,%eax
    24ef:	5b                   	pop    %rbx
    24f0:	5d                   	pop    %rbp
    24f1:	41 5c                	pop    %r12
    24f3:	c3                   	retq   
    24f4:	0f b6 03             	movzbl (%rbx),%eax
    24f7:	84 c0                	test   %al,%al
    24f9:	74 27                	je     2522 <strings_not_equal+0x59>
    24fb:	3a 45 00             	cmp    0x0(%rbp),%al
    24fe:	75 29                	jne    2529 <strings_not_equal+0x60>
    2500:	48 83 c3 01          	add    $0x1,%rbx
    2504:	48 83 c5 01          	add    $0x1,%rbp
    2508:	0f b6 03             	movzbl (%rbx),%eax
    250b:	84 c0                	test   %al,%al
    250d:	74 0c                	je     251b <strings_not_equal+0x52>
    250f:	38 45 00             	cmp    %al,0x0(%rbp)
    2512:	74 ec                	je     2500 <strings_not_equal+0x37>
    2514:	ba 01 00 00 00       	mov    $0x1,%edx
    2519:	eb d2                	jmp    24ed <strings_not_equal+0x24>
    251b:	ba 00 00 00 00       	mov    $0x0,%edx
    2520:	eb cb                	jmp    24ed <strings_not_equal+0x24>
    2522:	ba 00 00 00 00       	mov    $0x0,%edx
    2527:	eb c4                	jmp    24ed <strings_not_equal+0x24>
    2529:	ba 01 00 00 00       	mov    $0x1,%edx
    252e:	eb bd                	jmp    24ed <strings_not_equal+0x24>

0000000000002530 <initialize_bomb>:
    2530:	55                   	push   %rbp
    2531:	53                   	push   %rbx
    2532:	48 81 ec 58 20 00 00 	sub    $0x2058,%rsp
    2539:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2540:	00 00 
    2542:	48 89 84 24 48 20 00 	mov    %rax,0x2048(%rsp)
    2549:	00 
    254a:	31 c0                	xor    %eax,%eax
    254c:	48 8d 35 d6 fe ff ff 	lea    -0x12a(%rip),%rsi        # 2429 <sig_handler>
    2553:	bf 02 00 00 00       	mov    $0x2,%edi
    2558:	e8 23 f7 ff ff       	callq  1c80 <signal@plt>
    255d:	48 89 e7             	mov    %rsp,%rdi
    2560:	be 40 00 00 00       	mov    $0x40,%esi
    2565:	e8 96 f7 ff ff       	callq  1d00 <gethostname@plt>
    256a:	85 c0                	test   %eax,%eax
    256c:	0f 85 9b 00 00 00    	jne    260d <initialize_bomb+0xdd>
    2572:	48 8b 3d 07 3d 20 00 	mov    0x203d07(%rip),%rdi        # 206280 <host_table>
    2579:	48 8d 1d 08 3d 20 00 	lea    0x203d08(%rip),%rbx        # 206288 <host_table+0x8>
    2580:	48 89 e5             	mov    %rsp,%rbp
    2583:	48 85 ff             	test   %rdi,%rdi
    2586:	74 1d                	je     25a5 <initialize_bomb+0x75>
    2588:	48 89 ee             	mov    %rbp,%rsi
    258b:	e8 50 f6 ff ff       	callq  1be0 <strcasecmp@plt>
    2590:	85 c0                	test   %eax,%eax
    2592:	0f 84 b0 00 00 00    	je     2648 <initialize_bomb+0x118>
    2598:	48 83 c3 08          	add    $0x8,%rbx
    259c:	48 8b 7b f8          	mov    -0x8(%rbx),%rdi
    25a0:	48 85 ff             	test   %rdi,%rdi
    25a3:	75 e3                	jne    2588 <initialize_bomb+0x58>
    25a5:	48 89 e2             	mov    %rsp,%rdx
    25a8:	48 8d 35 49 15 00 00 	lea    0x1549(%rip),%rsi        # 3af8 <array.3425+0xd8>
    25af:	bf 01 00 00 00       	mov    $0x1,%edi
    25b4:	b8 00 00 00 00       	mov    $0x0,%eax
    25b9:	e8 22 f7 ff ff       	callq  1ce0 <__printf_chk@plt>
    25be:	48 8d 3d 4a 17 00 00 	lea    0x174a(%rip),%rdi        # 3d0f <array.3425+0x2ef>
    25c5:	e8 46 f6 ff ff       	callq  1c10 <puts@plt>
    25ca:	48 8b 15 af 3c 20 00 	mov    0x203caf(%rip),%rdx        # 206280 <host_table>
    25d1:	48 8d 1d b0 3c 20 00 	lea    0x203cb0(%rip),%rbx        # 206288 <host_table+0x8>
    25d8:	48 8d 2d 10 17 00 00 	lea    0x1710(%rip),%rbp        # 3cef <array.3425+0x2cf>
    25df:	48 85 d2             	test   %rdx,%rdx
    25e2:	74 1f                	je     2603 <initialize_bomb+0xd3>
    25e4:	48 89 ee             	mov    %rbp,%rsi
    25e7:	bf 01 00 00 00       	mov    $0x1,%edi
    25ec:	b8 00 00 00 00       	mov    $0x0,%eax
    25f1:	e8 ea f6 ff ff       	callq  1ce0 <__printf_chk@plt>
    25f6:	48 83 c3 08          	add    $0x8,%rbx
    25fa:	48 8b 53 f8          	mov    -0x8(%rbx),%rdx
    25fe:	48 85 d2             	test   %rdx,%rdx
    2601:	75 e1                	jne    25e4 <initialize_bomb+0xb4>
    2603:	bf 08 00 00 00       	mov    $0x8,%edi
    2608:	e8 03 f7 ff ff       	callq  1d10 <exit@plt>
    260d:	48 8d 3d ac 14 00 00 	lea    0x14ac(%rip),%rdi        # 3ac0 <array.3425+0xa0>
    2614:	e8 f7 f5 ff ff       	callq  1c10 <puts@plt>
    2619:	bf 08 00 00 00       	mov    $0x8,%edi
    261e:	e8 ed f6 ff ff       	callq  1d10 <exit@plt>
    2623:	48 8d 54 24 40       	lea    0x40(%rsp),%rdx
    2628:	48 8d 35 c6 16 00 00 	lea    0x16c6(%rip),%rsi        # 3cf5 <array.3425+0x2d5>
    262f:	bf 01 00 00 00       	mov    $0x1,%edi
    2634:	b8 00 00 00 00       	mov    $0x0,%eax
    2639:	e8 a2 f6 ff ff       	callq  1ce0 <__printf_chk@plt>
    263e:	bf 08 00 00 00       	mov    $0x8,%edi
    2643:	e8 c8 f6 ff ff       	callq  1d10 <exit@plt>
    2648:	48 8d 7c 24 40       	lea    0x40(%rsp),%rdi
    264d:	e8 16 0f 00 00       	callq  3568 <init_driver>
    2652:	85 c0                	test   %eax,%eax
    2654:	78 cd                	js     2623 <initialize_bomb+0xf3>
    2656:	48 8b 84 24 48 20 00 	mov    0x2048(%rsp),%rax
    265d:	00 
    265e:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    2665:	00 00 
    2667:	75 0a                	jne    2673 <initialize_bomb+0x143>
    2669:	48 81 c4 58 20 00 00 	add    $0x2058,%rsp
    2670:	5b                   	pop    %rbx
    2671:	5d                   	pop    %rbp
    2672:	c3                   	retq   
    2673:	e8 b8 f5 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002678 <initialize_bomb_solve>:
    2678:	f3 c3                	repz retq 

000000000000267a <blank_line>:
    267a:	55                   	push   %rbp
    267b:	53                   	push   %rbx
    267c:	48 83 ec 08          	sub    $0x8,%rsp
    2680:	48 89 fd             	mov    %rdi,%rbp
    2683:	0f b6 5d 00          	movzbl 0x0(%rbp),%ebx
    2687:	84 db                	test   %bl,%bl
    2689:	74 1e                	je     26a9 <blank_line+0x2f>
    268b:	e8 c0 f6 ff ff       	callq  1d50 <__ctype_b_loc@plt>
    2690:	48 83 c5 01          	add    $0x1,%rbp
    2694:	48 0f be db          	movsbq %bl,%rbx
    2698:	48 8b 00             	mov    (%rax),%rax
    269b:	f6 44 58 01 20       	testb  $0x20,0x1(%rax,%rbx,2)
    26a0:	75 e1                	jne    2683 <blank_line+0x9>
    26a2:	b8 00 00 00 00       	mov    $0x0,%eax
    26a7:	eb 05                	jmp    26ae <blank_line+0x34>
    26a9:	b8 01 00 00 00       	mov    $0x1,%eax
    26ae:	48 83 c4 08          	add    $0x8,%rsp
    26b2:	5b                   	pop    %rbx
    26b3:	5d                   	pop    %rbp
    26b4:	c3                   	retq   

00000000000026b5 <skip>:
    26b5:	55                   	push   %rbp
    26b6:	53                   	push   %rbx
    26b7:	48 83 ec 08          	sub    $0x8,%rsp
    26bb:	48 8d 2d fe 43 20 00 	lea    0x2043fe(%rip),%rbp        # 206ac0 <input_strings>
    26c2:	48 63 05 e3 43 20 00 	movslq 0x2043e3(%rip),%rax        # 206aac <num_input_strings>
    26c9:	48 8d 3c 80          	lea    (%rax,%rax,4),%rdi
    26cd:	48 c1 e7 04          	shl    $0x4,%rdi
    26d1:	48 01 ef             	add    %rbp,%rdi
    26d4:	48 8b 15 d5 43 20 00 	mov    0x2043d5(%rip),%rdx        # 206ab0 <infile>
    26db:	be 50 00 00 00       	mov    $0x50,%esi
    26e0:	e8 8b f5 ff ff       	callq  1c70 <fgets@plt>
    26e5:	48 89 c3             	mov    %rax,%rbx
    26e8:	48 85 c0             	test   %rax,%rax
    26eb:	74 0c                	je     26f9 <skip+0x44>
    26ed:	48 89 c7             	mov    %rax,%rdi
    26f0:	e8 85 ff ff ff       	callq  267a <blank_line>
    26f5:	85 c0                	test   %eax,%eax
    26f7:	75 c9                	jne    26c2 <skip+0xd>
    26f9:	48 89 d8             	mov    %rbx,%rax
    26fc:	48 83 c4 08          	add    $0x8,%rsp
    2700:	5b                   	pop    %rbx
    2701:	5d                   	pop    %rbp
    2702:	c3                   	retq   

0000000000002703 <send_msg>:
    2703:	53                   	push   %rbx
    2704:	48 81 ec 10 40 00 00 	sub    $0x4010,%rsp
    270b:	41 89 f8             	mov    %edi,%r8d
    270e:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2715:	00 00 
    2717:	48 89 84 24 08 40 00 	mov    %rax,0x4008(%rsp)
    271e:	00 
    271f:	31 c0                	xor    %eax,%eax
    2721:	8b 35 85 43 20 00    	mov    0x204385(%rip),%esi        # 206aac <num_input_strings>
    2727:	8d 46 ff             	lea    -0x1(%rsi),%eax
    272a:	48 98                	cltq   
    272c:	48 8d 14 80          	lea    (%rax,%rax,4),%rdx
    2730:	48 c1 e2 04          	shl    $0x4,%rdx
    2734:	48 8d 05 85 43 20 00 	lea    0x204385(%rip),%rax        # 206ac0 <input_strings>
    273b:	48 01 c2             	add    %rax,%rdx
    273e:	48 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%rcx
    2745:	b8 00 00 00 00       	mov    $0x0,%eax
    274a:	48 89 d7             	mov    %rdx,%rdi
    274d:	f2 ae                	repnz scas %es:(%rdi),%al
    274f:	48 89 c8             	mov    %rcx,%rax
    2752:	48 f7 d0             	not    %rax
    2755:	48 83 c0 63          	add    $0x63,%rax
    2759:	48 3d 00 20 00 00    	cmp    $0x2000,%rax
    275f:	0f 87 86 00 00 00    	ja     27eb <send_msg+0xe8>
    2765:	45 85 c0             	test   %r8d,%r8d
    2768:	4c 8d 0d bc 15 00 00 	lea    0x15bc(%rip),%r9        # 3d2b <array.3425+0x30b>
    276f:	48 8d 05 bd 15 00 00 	lea    0x15bd(%rip),%rax        # 3d33 <array.3425+0x313>
    2776:	4c 0f 44 c8          	cmove  %rax,%r9
    277a:	48 89 e3             	mov    %rsp,%rbx
    277d:	52                   	push   %rdx
    277e:	56                   	push   %rsi
    277f:	44 8b 05 be 39 20 00 	mov    0x2039be(%rip),%r8d        # 206144 <bomb_id>
    2786:	48 8d 0d af 15 00 00 	lea    0x15af(%rip),%rcx        # 3d3c <array.3425+0x31c>
    278d:	ba 00 20 00 00       	mov    $0x2000,%edx
    2792:	be 01 00 00 00       	mov    $0x1,%esi
    2797:	48 89 df             	mov    %rbx,%rdi
    279a:	b8 00 00 00 00       	mov    $0x0,%eax
    279f:	e8 bc f5 ff ff       	callq  1d60 <__sprintf_chk@plt>
    27a4:	4c 8d 84 24 10 20 00 	lea    0x2010(%rsp),%r8
    27ab:	00 
    27ac:	b9 00 00 00 00       	mov    $0x0,%ecx
    27b1:	48 89 da             	mov    %rbx,%rdx
    27b4:	48 8d 35 65 39 20 00 	lea    0x203965(%rip),%rsi        # 206120 <user_password>
    27bb:	48 8d 3d 76 39 20 00 	lea    0x203976(%rip),%rdi        # 206138 <userid>
    27c2:	e8 aa 0f 00 00       	callq  3771 <driver_post>
    27c7:	48 83 c4 10          	add    $0x10,%rsp
    27cb:	85 c0                	test   %eax,%eax
    27cd:	78 3c                	js     280b <send_msg+0x108>
    27cf:	48 8b 84 24 08 40 00 	mov    0x4008(%rsp),%rax
    27d6:	00 
    27d7:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    27de:	00 00 
    27e0:	75 40                	jne    2822 <send_msg+0x11f>
    27e2:	48 81 c4 10 40 00 00 	add    $0x4010,%rsp
    27e9:	5b                   	pop    %rbx
    27ea:	c3                   	retq   
    27eb:	48 8d 35 36 13 00 00 	lea    0x1336(%rip),%rsi        # 3b28 <array.3425+0x108>
    27f2:	bf 01 00 00 00       	mov    $0x1,%edi
    27f7:	b8 00 00 00 00       	mov    $0x0,%eax
    27fc:	e8 df f4 ff ff       	callq  1ce0 <__printf_chk@plt>
    2801:	bf 08 00 00 00       	mov    $0x8,%edi
    2806:	e8 05 f5 ff ff       	callq  1d10 <exit@plt>
    280b:	48 8d bc 24 00 20 00 	lea    0x2000(%rsp),%rdi
    2812:	00 
    2813:	e8 f8 f3 ff ff       	callq  1c10 <puts@plt>
    2818:	bf 00 00 00 00       	mov    $0x0,%edi
    281d:	e8 ee f4 ff ff       	callq  1d10 <exit@plt>
    2822:	e8 09 f4 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002827 <explode_bomb>:
    2827:	48 83 ec 08          	sub    $0x8,%rsp
    282b:	48 8d 3d 16 15 00 00 	lea    0x1516(%rip),%rdi        # 3d48 <array.3425+0x328>
    2832:	e8 d9 f3 ff ff       	callq  1c10 <puts@plt>
    2837:	48 8d 3d 13 15 00 00 	lea    0x1513(%rip),%rdi        # 3d51 <array.3425+0x331>
    283e:	e8 cd f3 ff ff       	callq  1c10 <puts@plt>
    2843:	bf 00 00 00 00       	mov    $0x0,%edi
    2848:	e8 b6 fe ff ff       	callq  2703 <send_msg>
    284d:	48 8d 3d fc 12 00 00 	lea    0x12fc(%rip),%rdi        # 3b50 <array.3425+0x130>
    2854:	e8 b7 f3 ff ff       	callq  1c10 <puts@plt>
    2859:	bf 08 00 00 00       	mov    $0x8,%edi
    285e:	e8 ad f4 ff ff       	callq  1d10 <exit@plt>

0000000000002863 <read_six_numbers>:
    2863:	48 83 ec 08          	sub    $0x8,%rsp
    2867:	48 89 f2             	mov    %rsi,%rdx
    286a:	48 8d 4e 04          	lea    0x4(%rsi),%rcx
    286e:	48 8d 46 14          	lea    0x14(%rsi),%rax
    2872:	50                   	push   %rax
    2873:	48 8d 46 10          	lea    0x10(%rsi),%rax
    2877:	50                   	push   %rax
    2878:	4c 8d 4e 0c          	lea    0xc(%rsi),%r9
    287c:	4c 8d 46 08          	lea    0x8(%rsi),%r8
    2880:	48 8d 35 e1 14 00 00 	lea    0x14e1(%rip),%rsi        # 3d68 <array.3425+0x348>
    2887:	b8 00 00 00 00       	mov    $0x0,%eax
    288c:	e8 3f f4 ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    2891:	48 83 c4 10          	add    $0x10,%rsp
    2895:	83 f8 05             	cmp    $0x5,%eax
    2898:	7e 05                	jle    289f <read_six_numbers+0x3c>
    289a:	48 83 c4 08          	add    $0x8,%rsp
    289e:	c3                   	retq   
    289f:	e8 83 ff ff ff       	callq  2827 <explode_bomb>

00000000000028a4 <read_line>:
    28a4:	48 83 ec 08          	sub    $0x8,%rsp
    28a8:	b8 00 00 00 00       	mov    $0x0,%eax
    28ad:	e8 03 fe ff ff       	callq  26b5 <skip>
    28b2:	48 85 c0             	test   %rax,%rax
    28b5:	74 6f                	je     2926 <read_line+0x82>
    28b7:	8b 35 ef 41 20 00    	mov    0x2041ef(%rip),%esi        # 206aac <num_input_strings>
    28bd:	48 63 c6             	movslq %esi,%rax
    28c0:	48 8d 14 80          	lea    (%rax,%rax,4),%rdx
    28c4:	48 c1 e2 04          	shl    $0x4,%rdx
    28c8:	48 8d 05 f1 41 20 00 	lea    0x2041f1(%rip),%rax        # 206ac0 <input_strings>
    28cf:	48 01 c2             	add    %rax,%rdx
    28d2:	48 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%rcx
    28d9:	b8 00 00 00 00       	mov    $0x0,%eax
    28de:	48 89 d7             	mov    %rdx,%rdi
    28e1:	f2 ae                	repnz scas %es:(%rdi),%al
    28e3:	48 f7 d1             	not    %rcx
    28e6:	48 83 e9 01          	sub    $0x1,%rcx
    28ea:	83 f9 4e             	cmp    $0x4e,%ecx
    28ed:	0f 8f ab 00 00 00    	jg     299e <read_line+0xfa>
    28f3:	83 e9 01             	sub    $0x1,%ecx
    28f6:	48 63 c9             	movslq %ecx,%rcx
    28f9:	48 63 c6             	movslq %esi,%rax
    28fc:	48 8d 04 80          	lea    (%rax,%rax,4),%rax
    2900:	48 c1 e0 04          	shl    $0x4,%rax
    2904:	48 89 c7             	mov    %rax,%rdi
    2907:	48 8d 05 b2 41 20 00 	lea    0x2041b2(%rip),%rax        # 206ac0 <input_strings>
    290e:	48 01 f8             	add    %rdi,%rax
    2911:	c6 04 08 00          	movb   $0x0,(%rax,%rcx,1)
    2915:	83 c6 01             	add    $0x1,%esi
    2918:	89 35 8e 41 20 00    	mov    %esi,0x20418e(%rip)        # 206aac <num_input_strings>
    291e:	48 89 d0             	mov    %rdx,%rax
    2921:	48 83 c4 08          	add    $0x8,%rsp
    2925:	c3                   	retq   
    2926:	48 8b 05 63 41 20 00 	mov    0x204163(%rip),%rax        # 206a90 <stdin@@GLIBC_2.2.5>
    292d:	48 39 05 7c 41 20 00 	cmp    %rax,0x20417c(%rip)        # 206ab0 <infile>
    2934:	74 1b                	je     2951 <read_line+0xad>
    2936:	48 8d 3d 5b 14 00 00 	lea    0x145b(%rip),%rdi        # 3d98 <array.3425+0x378>
    293d:	e8 7e f2 ff ff       	callq  1bc0 <getenv@plt>
    2942:	48 85 c0             	test   %rax,%rax
    2945:	74 20                	je     2967 <read_line+0xc3>
    2947:	bf 00 00 00 00       	mov    $0x0,%edi
    294c:	e8 bf f3 ff ff       	callq  1d10 <exit@plt>
    2951:	48 8d 3d 22 14 00 00 	lea    0x1422(%rip),%rdi        # 3d7a <array.3425+0x35a>
    2958:	e8 b3 f2 ff ff       	callq  1c10 <puts@plt>
    295d:	bf 08 00 00 00       	mov    $0x8,%edi
    2962:	e8 a9 f3 ff ff       	callq  1d10 <exit@plt>
    2967:	48 8b 05 22 41 20 00 	mov    0x204122(%rip),%rax        # 206a90 <stdin@@GLIBC_2.2.5>
    296e:	48 89 05 3b 41 20 00 	mov    %rax,0x20413b(%rip)        # 206ab0 <infile>
    2975:	b8 00 00 00 00       	mov    $0x0,%eax
    297a:	e8 36 fd ff ff       	callq  26b5 <skip>
    297f:	48 85 c0             	test   %rax,%rax
    2982:	0f 85 2f ff ff ff    	jne    28b7 <read_line+0x13>
    2988:	48 8d 3d eb 13 00 00 	lea    0x13eb(%rip),%rdi        # 3d7a <array.3425+0x35a>
    298f:	e8 7c f2 ff ff       	callq  1c10 <puts@plt>
    2994:	bf 00 00 00 00       	mov    $0x0,%edi
    2999:	e8 72 f3 ff ff       	callq  1d10 <exit@plt>
    299e:	48 8d 3d fe 13 00 00 	lea    0x13fe(%rip),%rdi        # 3da3 <array.3425+0x383>
    29a5:	e8 66 f2 ff ff       	callq  1c10 <puts@plt>
    29aa:	8b 05 fc 40 20 00    	mov    0x2040fc(%rip),%eax        # 206aac <num_input_strings>
    29b0:	8d 50 01             	lea    0x1(%rax),%edx
    29b3:	89 15 f3 40 20 00    	mov    %edx,0x2040f3(%rip)        # 206aac <num_input_strings>
    29b9:	48 98                	cltq   
    29bb:	48 6b c0 50          	imul   $0x50,%rax,%rax
    29bf:	48 8d 15 fa 40 20 00 	lea    0x2040fa(%rip),%rdx        # 206ac0 <input_strings>
    29c6:	48 be 2a 2a 2a 74 72 	movabs $0x636e7572742a2a2a,%rsi
    29cd:	75 6e 63 
    29d0:	48 bf 61 74 65 64 2a 	movabs $0x2a2a2a64657461,%rdi
    29d7:	2a 2a 00 
    29da:	48 89 34 02          	mov    %rsi,(%rdx,%rax,1)
    29de:	48 89 7c 02 08       	mov    %rdi,0x8(%rdx,%rax,1)
    29e3:	e8 3f fe ff ff       	callq  2827 <explode_bomb>

00000000000029e8 <phase_defused>:
    29e8:	48 81 ec 98 00 00 00 	sub    $0x98,%rsp
    29ef:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    29f6:	00 00 
    29f8:	48 89 84 24 88 00 00 	mov    %rax,0x88(%rsp)
    29ff:	00 
    2a00:	31 c0                	xor    %eax,%eax
    2a02:	bf 01 00 00 00       	mov    $0x1,%edi
    2a07:	e8 f7 fc ff ff       	callq  2703 <send_msg>
    2a0c:	83 3d 99 40 20 00 06 	cmpl   $0x6,0x204099(%rip)        # 206aac <num_input_strings>
    2a13:	74 1f                	je     2a34 <phase_defused+0x4c>
    2a15:	48 8b 84 24 88 00 00 	mov    0x88(%rsp),%rax
    2a1c:	00 
    2a1d:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    2a24:	00 00 
    2a26:	0f 85 72 01 00 00    	jne    2b9e <phase_defused+0x1b6>
    2a2c:	48 81 c4 98 00 00 00 	add    $0x98,%rsp
    2a33:	c3                   	retq   
    2a34:	48 8d 54 24 10       	lea    0x10(%rsp),%rdx
    2a39:	48 8d 4a 04          	lea    0x4(%rdx),%rcx
    2a3d:	48 83 ec 08          	sub    $0x8,%rsp
    2a41:	48 8d 44 24 38       	lea    0x38(%rsp),%rax
    2a46:	50                   	push   %rax
    2a47:	48 8d 42 14          	lea    0x14(%rdx),%rax
    2a4b:	50                   	push   %rax
    2a4c:	48 8d 42 10          	lea    0x10(%rdx),%rax
    2a50:	50                   	push   %rax
    2a51:	4c 8d 4a 0c          	lea    0xc(%rdx),%r9
    2a55:	4c 8d 42 08          	lea    0x8(%rdx),%r8
    2a59:	48 8d 35 5e 13 00 00 	lea    0x135e(%rip),%rsi        # 3dbe <array.3425+0x39e>
    2a60:	48 8d 3d a9 40 20 00 	lea    0x2040a9(%rip),%rdi        # 206b10 <input_strings+0x50>
    2a67:	b8 00 00 00 00       	mov    $0x0,%eax
    2a6c:	e8 5f f2 ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    2a71:	48 83 c4 20          	add    $0x20,%rsp
    2a75:	83 f8 07             	cmp    $0x7,%eax
    2a78:	0f 84 e0 00 00 00    	je     2b5e <phase_defused+0x176>
    2a7e:	48 8d 3d 5b 11 00 00 	lea    0x115b(%rip),%rdi        # 3be0 <array.3425+0x1c0>
    2a85:	e8 86 f1 ff ff       	callq  1c10 <puts@plt>
    2a8a:	48 8d 3d 7f 11 00 00 	lea    0x117f(%rip),%rdi        # 3c10 <array.3425+0x1f0>
    2a91:	e8 7a f1 ff ff       	callq  1c10 <puts@plt>
    2a96:	48 8d 4c 24 0c       	lea    0xc(%rsp),%rcx
    2a9b:	48 8d 54 24 08       	lea    0x8(%rsp),%rdx
    2aa0:	4c 8d 44 24 30       	lea    0x30(%rsp),%r8
    2aa5:	48 8d 35 1e 13 00 00 	lea    0x131e(%rip),%rsi        # 3dca <array.3425+0x3aa>
    2aac:	48 8d 3d fd 40 20 00 	lea    0x2040fd(%rip),%rdi        # 206bb0 <input_strings+0xf0>
    2ab3:	b8 00 00 00 00       	mov    $0x0,%eax
    2ab8:	e8 13 f2 ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    2abd:	83 f8 03             	cmp    $0x3,%eax
    2ac0:	0f 85 4f ff ff ff    	jne    2a15 <phase_defused+0x2d>
    2ac6:	48 8d 7c 24 30       	lea    0x30(%rsp),%rdi
    2acb:	48 8d 35 10 13 00 00 	lea    0x1310(%rip),%rsi        # 3de2 <array.3425+0x3c2>
    2ad2:	e8 f2 f9 ff ff       	callq  24c9 <strings_not_equal>
    2ad7:	85 c0                	test   %eax,%eax
    2ad9:	0f 85 36 ff ff ff    	jne    2a15 <phase_defused+0x2d>
    2adf:	48 8d 3d 28 13 00 00 	lea    0x1328(%rip),%rdi        # 3e0e <array.3425+0x3ee>
    2ae6:	e8 25 f1 ff ff       	callq  1c10 <puts@plt>
    2aeb:	bf 02 00 00 00       	mov    $0x2,%edi
    2af0:	e8 4b f2 ff ff       	callq  1d40 <sleep@plt>
    2af5:	48 8d 3d ed 12 00 00 	lea    0x12ed(%rip),%rdi        # 3de9 <array.3425+0x3c9>
    2afc:	e8 0f f1 ff ff       	callq  1c10 <puts@plt>
    2b01:	bf 03 00 00 00       	mov    $0x3,%edi
    2b06:	e8 35 f2 ff ff       	callq  1d40 <sleep@plt>
    2b0b:	48 8d 3d ea 12 00 00 	lea    0x12ea(%rip),%rdi        # 3dfc <array.3425+0x3dc>
    2b12:	e8 f9 f0 ff ff       	callq  1c10 <puts@plt>
    2b17:	bf 04 00 00 00       	mov    $0x4,%edi
    2b1c:	e8 1f f2 ff ff       	callq  1d40 <sleep@plt>
    2b21:	48 8d 3d ea 12 00 00 	lea    0x12ea(%rip),%rdi        # 3e12 <array.3425+0x3f2>
    2b28:	e8 e3 f0 ff ff       	callq  1c10 <puts@plt>
    2b2d:	bf 05 00 00 00       	mov    $0x5,%edi
    2b32:	e8 09 f2 ff ff       	callq  1d40 <sleep@plt>
    2b37:	48 8d 3d 1a 11 00 00 	lea    0x111a(%rip),%rdi        # 3c58 <array.3425+0x238>
    2b3e:	e8 cd f0 ff ff       	callq  1c10 <puts@plt>
    2b43:	bf 05 00 00 00       	mov    $0x5,%edi
    2b48:	e8 f3 f1 ff ff       	callq  1d40 <sleep@plt>
    2b4d:	48 8d 3d 3c 11 00 00 	lea    0x113c(%rip),%rdi        # 3c90 <array.3425+0x270>
    2b54:	e8 b7 f0 ff ff       	callq  1c10 <puts@plt>
    2b59:	e9 b7 fe ff ff       	jmpq   2a15 <phase_defused+0x2d>
    2b5e:	48 8d 7c 24 30       	lea    0x30(%rsp),%rdi
    2b63:	48 8d 35 69 12 00 00 	lea    0x1269(%rip),%rsi        # 3dd3 <array.3425+0x3b3>
    2b6a:	e8 5a f9 ff ff       	callq  24c9 <strings_not_equal>
    2b6f:	85 c0                	test   %eax,%eax
    2b71:	0f 85 07 ff ff ff    	jne    2a7e <phase_defused+0x96>
    2b77:	48 8d 3d fa 0f 00 00 	lea    0xffa(%rip),%rdi        # 3b78 <array.3425+0x158>
    2b7e:	e8 8d f0 ff ff       	callq  1c10 <puts@plt>
    2b83:	48 8d 3d 1e 10 00 00 	lea    0x101e(%rip),%rdi        # 3ba8 <array.3425+0x188>
    2b8a:	e8 81 f0 ff ff       	callq  1c10 <puts@plt>
    2b8f:	b8 00 00 00 00       	mov    $0x0,%eax
    2b94:	e8 39 f8 ff ff       	callq  23d2 <secret_phase>
    2b99:	e9 e0 fe ff ff       	jmpq   2a7e <phase_defused+0x96>
    2b9e:	e8 8d f0 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000002ba3 <sigalrm_handler>:
    2ba3:	48 83 ec 08          	sub    $0x8,%rsp
    2ba7:	b9 00 00 00 00       	mov    $0x0,%ecx
    2bac:	48 8d 15 75 1a 00 00 	lea    0x1a75(%rip),%rdx        # 4628 <array.3425+0xc08>
    2bb3:	be 01 00 00 00       	mov    $0x1,%esi
    2bb8:	48 8b 3d e1 3e 20 00 	mov    0x203ee1(%rip),%rdi        # 206aa0 <stderr@@GLIBC_2.2.5>
    2bbf:	b8 00 00 00 00       	mov    $0x0,%eax
    2bc4:	e8 67 f1 ff ff       	callq  1d30 <__fprintf_chk@plt>
    2bc9:	bf 01 00 00 00       	mov    $0x1,%edi
    2bce:	e8 3d f1 ff ff       	callq  1d10 <exit@plt>

0000000000002bd3 <rio_readlineb>:
    2bd3:	41 56                	push   %r14
    2bd5:	41 55                	push   %r13
    2bd7:	41 54                	push   %r12
    2bd9:	55                   	push   %rbp
    2bda:	53                   	push   %rbx
    2bdb:	48 89 fb             	mov    %rdi,%rbx
    2bde:	49 89 f4             	mov    %rsi,%r12
    2be1:	49 89 d6             	mov    %rdx,%r14
    2be4:	41 bd 01 00 00 00    	mov    $0x1,%r13d
    2bea:	48 8d 6f 10          	lea    0x10(%rdi),%rbp
    2bee:	48 83 fa 01          	cmp    $0x1,%rdx
    2bf2:	77 0c                	ja     2c00 <rio_readlineb+0x2d>
    2bf4:	eb 60                	jmp    2c56 <rio_readlineb+0x83>
    2bf6:	e8 f5 ef ff ff       	callq  1bf0 <__errno_location@plt>
    2bfb:	83 38 04             	cmpl   $0x4,(%rax)
    2bfe:	75 67                	jne    2c67 <rio_readlineb+0x94>
    2c00:	8b 43 04             	mov    0x4(%rbx),%eax
    2c03:	85 c0                	test   %eax,%eax
    2c05:	7f 20                	jg     2c27 <rio_readlineb+0x54>
    2c07:	ba 00 20 00 00       	mov    $0x2000,%edx
    2c0c:	48 89 ee             	mov    %rbp,%rsi
    2c0f:	8b 3b                	mov    (%rbx),%edi
    2c11:	e8 4a f0 ff ff       	callq  1c60 <read@plt>
    2c16:	89 43 04             	mov    %eax,0x4(%rbx)
    2c19:	85 c0                	test   %eax,%eax
    2c1b:	78 d9                	js     2bf6 <rio_readlineb+0x23>
    2c1d:	85 c0                	test   %eax,%eax
    2c1f:	74 4f                	je     2c70 <rio_readlineb+0x9d>
    2c21:	48 89 6b 08          	mov    %rbp,0x8(%rbx)
    2c25:	eb d9                	jmp    2c00 <rio_readlineb+0x2d>
    2c27:	48 8b 53 08          	mov    0x8(%rbx),%rdx
    2c2b:	0f b6 0a             	movzbl (%rdx),%ecx
    2c2e:	48 83 c2 01          	add    $0x1,%rdx
    2c32:	48 89 53 08          	mov    %rdx,0x8(%rbx)
    2c36:	83 e8 01             	sub    $0x1,%eax
    2c39:	89 43 04             	mov    %eax,0x4(%rbx)
    2c3c:	49 83 c4 01          	add    $0x1,%r12
    2c40:	41 88 4c 24 ff       	mov    %cl,-0x1(%r12)
    2c45:	80 f9 0a             	cmp    $0xa,%cl
    2c48:	74 0c                	je     2c56 <rio_readlineb+0x83>
    2c4a:	41 83 c5 01          	add    $0x1,%r13d
    2c4e:	49 63 c5             	movslq %r13d,%rax
    2c51:	4c 39 f0             	cmp    %r14,%rax
    2c54:	72 aa                	jb     2c00 <rio_readlineb+0x2d>
    2c56:	41 c6 04 24 00       	movb   $0x0,(%r12)
    2c5b:	49 63 c5             	movslq %r13d,%rax
    2c5e:	5b                   	pop    %rbx
    2c5f:	5d                   	pop    %rbp
    2c60:	41 5c                	pop    %r12
    2c62:	41 5d                	pop    %r13
    2c64:	41 5e                	pop    %r14
    2c66:	c3                   	retq   
    2c67:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
    2c6e:	eb 05                	jmp    2c75 <rio_readlineb+0xa2>
    2c70:	b8 00 00 00 00       	mov    $0x0,%eax
    2c75:	85 c0                	test   %eax,%eax
    2c77:	75 0d                	jne    2c86 <rio_readlineb+0xb3>
    2c79:	b8 00 00 00 00       	mov    $0x0,%eax
    2c7e:	41 83 fd 01          	cmp    $0x1,%r13d
    2c82:	75 d2                	jne    2c56 <rio_readlineb+0x83>
    2c84:	eb d8                	jmp    2c5e <rio_readlineb+0x8b>
    2c86:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
    2c8d:	eb cf                	jmp    2c5e <rio_readlineb+0x8b>

0000000000002c8f <submitr>:
    2c8f:	41 57                	push   %r15
    2c91:	41 56                	push   %r14
    2c93:	41 55                	push   %r13
    2c95:	41 54                	push   %r12
    2c97:	55                   	push   %rbp
    2c98:	53                   	push   %rbx
    2c99:	48 81 ec 78 a0 00 00 	sub    $0xa078,%rsp
    2ca0:	49 89 fd             	mov    %rdi,%r13
    2ca3:	89 f5                	mov    %esi,%ebp
    2ca5:	48 89 54 24 08       	mov    %rdx,0x8(%rsp)
    2caa:	48 89 4c 24 10       	mov    %rcx,0x10(%rsp)
    2caf:	4c 89 44 24 20       	mov    %r8,0x20(%rsp)
    2cb4:	4c 89 4c 24 18       	mov    %r9,0x18(%rsp)
    2cb9:	48 8b 9c 24 b0 a0 00 	mov    0xa0b0(%rsp),%rbx
    2cc0:	00 
    2cc1:	4c 8b bc 24 b8 a0 00 	mov    0xa0b8(%rsp),%r15
    2cc8:	00 
    2cc9:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2cd0:	00 00 
    2cd2:	48 89 84 24 68 a0 00 	mov    %rax,0xa068(%rsp)
    2cd9:	00 
    2cda:	31 c0                	xor    %eax,%eax
    2cdc:	c7 44 24 3c 00 00 00 	movl   $0x0,0x3c(%rsp)
    2ce3:	00 
    2ce4:	ba 00 00 00 00       	mov    $0x0,%edx
    2ce9:	be 01 00 00 00       	mov    $0x1,%esi
    2cee:	bf 02 00 00 00       	mov    $0x2,%edi
    2cf3:	e8 78 f0 ff ff       	callq  1d70 <socket@plt>
    2cf8:	85 c0                	test   %eax,%eax
    2cfa:	0f 88 35 01 00 00    	js     2e35 <submitr+0x1a6>
    2d00:	41 89 c4             	mov    %eax,%r12d
    2d03:	4c 89 ef             	mov    %r13,%rdi
    2d06:	e8 85 ef ff ff       	callq  1c90 <gethostbyname@plt>
    2d0b:	48 85 c0             	test   %rax,%rax
    2d0e:	0f 84 71 01 00 00    	je     2e85 <submitr+0x1f6>
    2d14:	4c 8d 6c 24 40       	lea    0x40(%rsp),%r13
    2d19:	48 c7 44 24 42 00 00 	movq   $0x0,0x42(%rsp)
    2d20:	00 00 
    2d22:	c7 44 24 4a 00 00 00 	movl   $0x0,0x4a(%rsp)
    2d29:	00 
    2d2a:	66 c7 44 24 4e 00 00 	movw   $0x0,0x4e(%rsp)
    2d31:	66 c7 44 24 40 02 00 	movw   $0x2,0x40(%rsp)
    2d38:	48 63 50 14          	movslq 0x14(%rax),%rdx
    2d3c:	48 8b 40 18          	mov    0x18(%rax),%rax
    2d40:	48 8d 7c 24 44       	lea    0x44(%rsp),%rdi
    2d45:	b9 0c 00 00 00       	mov    $0xc,%ecx
    2d4a:	48 8b 30             	mov    (%rax),%rsi
    2d4d:	e8 4e ef ff ff       	callq  1ca0 <__memmove_chk@plt>
    2d52:	66 c1 cd 08          	ror    $0x8,%bp
    2d56:	66 89 6c 24 42       	mov    %bp,0x42(%rsp)
    2d5b:	ba 10 00 00 00       	mov    $0x10,%edx
    2d60:	4c 89 ee             	mov    %r13,%rsi
    2d63:	44 89 e7             	mov    %r12d,%edi
    2d66:	e8 b5 ef ff ff       	callq  1d20 <connect@plt>
    2d6b:	85 c0                	test   %eax,%eax
    2d6d:	0f 88 7d 01 00 00    	js     2ef0 <submitr+0x261>
    2d73:	49 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%r9
    2d7a:	b8 00 00 00 00       	mov    $0x0,%eax
    2d7f:	4c 89 c9             	mov    %r9,%rcx
    2d82:	48 89 df             	mov    %rbx,%rdi
    2d85:	f2 ae                	repnz scas %es:(%rdi),%al
    2d87:	48 89 ce             	mov    %rcx,%rsi
    2d8a:	48 f7 d6             	not    %rsi
    2d8d:	4c 89 c9             	mov    %r9,%rcx
    2d90:	48 8b 7c 24 08       	mov    0x8(%rsp),%rdi
    2d95:	f2 ae                	repnz scas %es:(%rdi),%al
    2d97:	49 89 c8             	mov    %rcx,%r8
    2d9a:	4c 89 c9             	mov    %r9,%rcx
    2d9d:	48 8b 7c 24 10       	mov    0x10(%rsp),%rdi
    2da2:	f2 ae                	repnz scas %es:(%rdi),%al
    2da4:	48 89 ca             	mov    %rcx,%rdx
    2da7:	48 f7 d2             	not    %rdx
    2daa:	4c 89 c9             	mov    %r9,%rcx
    2dad:	48 8b 7c 24 18       	mov    0x18(%rsp),%rdi
    2db2:	f2 ae                	repnz scas %es:(%rdi),%al
    2db4:	4c 29 c2             	sub    %r8,%rdx
    2db7:	48 29 ca             	sub    %rcx,%rdx
    2dba:	48 8d 44 76 fd       	lea    -0x3(%rsi,%rsi,2),%rax
    2dbf:	48 8d 44 02 7b       	lea    0x7b(%rdx,%rax,1),%rax
    2dc4:	48 3d 00 20 00 00    	cmp    $0x2000,%rax
    2dca:	0f 87 7d 01 00 00    	ja     2f4d <submitr+0x2be>
    2dd0:	48 8d 94 24 60 40 00 	lea    0x4060(%rsp),%rdx
    2dd7:	00 
    2dd8:	b9 00 04 00 00       	mov    $0x400,%ecx
    2ddd:	b8 00 00 00 00       	mov    $0x0,%eax
    2de2:	48 89 d7             	mov    %rdx,%rdi
    2de5:	f3 48 ab             	rep stos %rax,%es:(%rdi)
    2de8:	48 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%rcx
    2def:	48 89 df             	mov    %rbx,%rdi
    2df2:	f2 ae                	repnz scas %es:(%rdi),%al
    2df4:	48 89 ca             	mov    %rcx,%rdx
    2df7:	48 f7 d2             	not    %rdx
    2dfa:	48 89 d1             	mov    %rdx,%rcx
    2dfd:	48 83 e9 01          	sub    $0x1,%rcx
    2e01:	85 c9                	test   %ecx,%ecx
    2e03:	0f 84 9c 06 00 00    	je     34a5 <submitr+0x816>
    2e09:	8d 41 ff             	lea    -0x1(%rcx),%eax
    2e0c:	4c 8d 74 03 01       	lea    0x1(%rbx,%rax,1),%r14
    2e11:	48 8d ac 24 60 40 00 	lea    0x4060(%rsp),%rbp
    2e18:	00 
    2e19:	48 8d 84 24 60 80 00 	lea    0x8060(%rsp),%rax
    2e20:	00 
    2e21:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
    2e26:	49 bd d9 ff 00 00 00 	movabs $0x2000000000ffd9,%r13
    2e2d:	00 20 00 
    2e30:	e9 a6 01 00 00       	jmpq   2fdb <submitr+0x34c>
    2e35:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    2e3c:	3a 20 43 
    2e3f:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    2e46:	20 75 6e 
    2e49:	49 89 07             	mov    %rax,(%r15)
    2e4c:	49 89 57 08          	mov    %rdx,0x8(%r15)
    2e50:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    2e57:	74 6f 20 
    2e5a:	48 ba 63 72 65 61 74 	movabs $0x7320657461657263,%rdx
    2e61:	65 20 73 
    2e64:	49 89 47 10          	mov    %rax,0x10(%r15)
    2e68:	49 89 57 18          	mov    %rdx,0x18(%r15)
    2e6c:	41 c7 47 20 6f 63 6b 	movl   $0x656b636f,0x20(%r15)
    2e73:	65 
    2e74:	66 41 c7 47 24 74 00 	movw   $0x74,0x24(%r15)
    2e7b:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    2e80:	e9 f7 04 00 00       	jmpq   337c <submitr+0x6ed>
    2e85:	48 b8 45 72 72 6f 72 	movabs $0x44203a726f727245,%rax
    2e8c:	3a 20 44 
    2e8f:	48 ba 4e 53 20 69 73 	movabs $0x6e7520736920534e,%rdx
    2e96:	20 75 6e 
    2e99:	49 89 07             	mov    %rax,(%r15)
    2e9c:	49 89 57 08          	mov    %rdx,0x8(%r15)
    2ea0:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    2ea7:	74 6f 20 
    2eaa:	48 ba 72 65 73 6f 6c 	movabs $0x2065766c6f736572,%rdx
    2eb1:	76 65 20 
    2eb4:	49 89 47 10          	mov    %rax,0x10(%r15)
    2eb8:	49 89 57 18          	mov    %rdx,0x18(%r15)
    2ebc:	48 b8 73 65 72 76 65 	movabs $0x6120726576726573,%rax
    2ec3:	72 20 61 
    2ec6:	49 89 47 20          	mov    %rax,0x20(%r15)
    2eca:	41 c7 47 28 64 64 72 	movl   $0x65726464,0x28(%r15)
    2ed1:	65 
    2ed2:	66 41 c7 47 2c 73 73 	movw   $0x7373,0x2c(%r15)
    2ed9:	41 c6 47 2e 00       	movb   $0x0,0x2e(%r15)
    2ede:	44 89 e7             	mov    %r12d,%edi
    2ee1:	e8 6a ed ff ff       	callq  1c50 <close@plt>
    2ee6:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    2eeb:	e9 8c 04 00 00       	jmpq   337c <submitr+0x6ed>
    2ef0:	48 b8 45 72 72 6f 72 	movabs $0x55203a726f727245,%rax
    2ef7:	3a 20 55 
    2efa:	48 ba 6e 61 62 6c 65 	movabs $0x6f7420656c62616e,%rdx
    2f01:	20 74 6f 
    2f04:	49 89 07             	mov    %rax,(%r15)
    2f07:	49 89 57 08          	mov    %rdx,0x8(%r15)
    2f0b:	48 b8 20 63 6f 6e 6e 	movabs $0x7463656e6e6f6320,%rax
    2f12:	65 63 74 
    2f15:	48 ba 20 74 6f 20 74 	movabs $0x20656874206f7420,%rdx
    2f1c:	68 65 20 
    2f1f:	49 89 47 10          	mov    %rax,0x10(%r15)
    2f23:	49 89 57 18          	mov    %rdx,0x18(%r15)
    2f27:	41 c7 47 20 73 65 72 	movl   $0x76726573,0x20(%r15)
    2f2e:	76 
    2f2f:	66 41 c7 47 24 65 72 	movw   $0x7265,0x24(%r15)
    2f36:	41 c6 47 26 00       	movb   $0x0,0x26(%r15)
    2f3b:	44 89 e7             	mov    %r12d,%edi
    2f3e:	e8 0d ed ff ff       	callq  1c50 <close@plt>
    2f43:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    2f48:	e9 2f 04 00 00       	jmpq   337c <submitr+0x6ed>
    2f4d:	48 b8 45 72 72 6f 72 	movabs $0x52203a726f727245,%rax
    2f54:	3a 20 52 
    2f57:	48 ba 65 73 75 6c 74 	movabs $0x747320746c757365,%rdx
    2f5e:	20 73 74 
    2f61:	49 89 07             	mov    %rax,(%r15)
    2f64:	49 89 57 08          	mov    %rdx,0x8(%r15)
    2f68:	48 b8 72 69 6e 67 20 	movabs $0x6f6f7420676e6972,%rax
    2f6f:	74 6f 6f 
    2f72:	48 ba 20 6c 61 72 67 	movabs $0x202e656772616c20,%rdx
    2f79:	65 2e 20 
    2f7c:	49 89 47 10          	mov    %rax,0x10(%r15)
    2f80:	49 89 57 18          	mov    %rdx,0x18(%r15)
    2f84:	48 b8 49 6e 63 72 65 	movabs $0x6573616572636e49,%rax
    2f8b:	61 73 65 
    2f8e:	48 ba 20 53 55 42 4d 	movabs $0x5254494d42555320,%rdx
    2f95:	49 54 52 
    2f98:	49 89 47 20          	mov    %rax,0x20(%r15)
    2f9c:	49 89 57 28          	mov    %rdx,0x28(%r15)
    2fa0:	48 b8 5f 4d 41 58 42 	movabs $0x46554258414d5f,%rax
    2fa7:	55 46 00 
    2faa:	49 89 47 30          	mov    %rax,0x30(%r15)
    2fae:	44 89 e7             	mov    %r12d,%edi
    2fb1:	e8 9a ec ff ff       	callq  1c50 <close@plt>
    2fb6:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    2fbb:	e9 bc 03 00 00       	jmpq   337c <submitr+0x6ed>
    2fc0:	49 0f a3 c5          	bt     %rax,%r13
    2fc4:	73 21                	jae    2fe7 <submitr+0x358>
    2fc6:	44 88 45 00          	mov    %r8b,0x0(%rbp)
    2fca:	48 8d 6d 01          	lea    0x1(%rbp),%rbp
    2fce:	48 83 c3 01          	add    $0x1,%rbx
    2fd2:	4c 39 f3             	cmp    %r14,%rbx
    2fd5:	0f 84 ca 04 00 00    	je     34a5 <submitr+0x816>
    2fdb:	44 0f b6 03          	movzbl (%rbx),%r8d
    2fdf:	41 8d 40 d6          	lea    -0x2a(%r8),%eax
    2fe3:	3c 35                	cmp    $0x35,%al
    2fe5:	76 d9                	jbe    2fc0 <submitr+0x331>
    2fe7:	44 89 c0             	mov    %r8d,%eax
    2fea:	83 e0 df             	and    $0xffffffdf,%eax
    2fed:	83 e8 41             	sub    $0x41,%eax
    2ff0:	3c 19                	cmp    $0x19,%al
    2ff2:	76 d2                	jbe    2fc6 <submitr+0x337>
    2ff4:	41 80 f8 20          	cmp    $0x20,%r8b
    2ff8:	74 60                	je     305a <submitr+0x3cb>
    2ffa:	41 8d 40 e0          	lea    -0x20(%r8),%eax
    2ffe:	3c 5f                	cmp    $0x5f,%al
    3000:	76 0a                	jbe    300c <submitr+0x37d>
    3002:	41 80 f8 09          	cmp    $0x9,%r8b
    3006:	0f 85 0c 04 00 00    	jne    3418 <submitr+0x789>
    300c:	45 0f b6 c0          	movzbl %r8b,%r8d
    3010:	48 8d 0d e9 16 00 00 	lea    0x16e9(%rip),%rcx        # 4700 <array.3425+0xce0>
    3017:	ba 08 00 00 00       	mov    $0x8,%edx
    301c:	be 01 00 00 00       	mov    $0x1,%esi
    3021:	48 8b 7c 24 28       	mov    0x28(%rsp),%rdi
    3026:	b8 00 00 00 00       	mov    $0x0,%eax
    302b:	e8 30 ed ff ff       	callq  1d60 <__sprintf_chk@plt>
    3030:	0f b6 84 24 60 80 00 	movzbl 0x8060(%rsp),%eax
    3037:	00 
    3038:	88 45 00             	mov    %al,0x0(%rbp)
    303b:	0f b6 84 24 61 80 00 	movzbl 0x8061(%rsp),%eax
    3042:	00 
    3043:	88 45 01             	mov    %al,0x1(%rbp)
    3046:	0f b6 84 24 62 80 00 	movzbl 0x8062(%rsp),%eax
    304d:	00 
    304e:	88 45 02             	mov    %al,0x2(%rbp)
    3051:	48 8d 6d 03          	lea    0x3(%rbp),%rbp
    3055:	e9 74 ff ff ff       	jmpq   2fce <submitr+0x33f>
    305a:	c6 45 00 2b          	movb   $0x2b,0x0(%rbp)
    305e:	48 8d 6d 01          	lea    0x1(%rbp),%rbp
    3062:	e9 67 ff ff ff       	jmpq   2fce <submitr+0x33f>
    3067:	48 b8 45 72 72 6f 72 	movabs $0x47203a726f727245,%rax
    306e:	3a 20 47 
    3071:	48 ba 45 54 20 72 65 	movabs $0x6575716572205445,%rdx
    3078:	71 75 65 
    307b:	49 89 07             	mov    %rax,(%r15)
    307e:	49 89 57 08          	mov    %rdx,0x8(%r15)
    3082:	48 b8 73 74 20 65 78 	movabs $0x6565637865207473,%rax
    3089:	63 65 65 
    308c:	48 ba 64 73 20 62 75 	movabs $0x6566667562207364,%rdx
    3093:	66 66 65 
    3096:	49 89 47 10          	mov    %rax,0x10(%r15)
    309a:	49 89 57 18          	mov    %rdx,0x18(%r15)
    309e:	41 c7 47 20 72 20 73 	movl   $0x69732072,0x20(%r15)
    30a5:	69 
    30a6:	66 41 c7 47 24 7a 65 	movw   $0x657a,0x24(%r15)
    30ad:	41 c6 47 26 00       	movb   $0x0,0x26(%r15)
    30b2:	44 89 e7             	mov    %r12d,%edi
    30b5:	e8 96 eb ff ff       	callq  1c50 <close@plt>
    30ba:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    30bf:	e9 b8 02 00 00       	jmpq   337c <submitr+0x6ed>
    30c4:	48 01 c5             	add    %rax,%rbp
    30c7:	48 29 c3             	sub    %rax,%rbx
    30ca:	74 26                	je     30f2 <submitr+0x463>
    30cc:	48 89 da             	mov    %rbx,%rdx
    30cf:	48 89 ee             	mov    %rbp,%rsi
    30d2:	44 89 e7             	mov    %r12d,%edi
    30d5:	e8 46 eb ff ff       	callq  1c20 <write@plt>
    30da:	48 85 c0             	test   %rax,%rax
    30dd:	7f e5                	jg     30c4 <submitr+0x435>
    30df:	e8 0c eb ff ff       	callq  1bf0 <__errno_location@plt>
    30e4:	83 38 04             	cmpl   $0x4,(%rax)
    30e7:	0f 85 31 01 00 00    	jne    321e <submitr+0x58f>
    30ed:	4c 89 f0             	mov    %r14,%rax
    30f0:	eb d2                	jmp    30c4 <submitr+0x435>
    30f2:	4d 85 ed             	test   %r13,%r13
    30f5:	0f 88 23 01 00 00    	js     321e <submitr+0x58f>
    30fb:	44 89 64 24 50       	mov    %r12d,0x50(%rsp)
    3100:	c7 44 24 54 00 00 00 	movl   $0x0,0x54(%rsp)
    3107:	00 
    3108:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
    310d:	48 8d 47 10          	lea    0x10(%rdi),%rax
    3111:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
    3116:	48 8d b4 24 60 20 00 	lea    0x2060(%rsp),%rsi
    311d:	00 
    311e:	ba 00 20 00 00       	mov    $0x2000,%edx
    3123:	e8 ab fa ff ff       	callq  2bd3 <rio_readlineb>
    3128:	48 85 c0             	test   %rax,%rax
    312b:	0f 8e 4c 01 00 00    	jle    327d <submitr+0x5ee>
    3131:	48 8d 4c 24 3c       	lea    0x3c(%rsp),%rcx
    3136:	48 8d 94 24 60 60 00 	lea    0x6060(%rsp),%rdx
    313d:	00 
    313e:	48 8d bc 24 60 20 00 	lea    0x2060(%rsp),%rdi
    3145:	00 
    3146:	4c 8d 84 24 60 80 00 	lea    0x8060(%rsp),%r8
    314d:	00 
    314e:	48 8d 35 b2 15 00 00 	lea    0x15b2(%rip),%rsi        # 4707 <array.3425+0xce7>
    3155:	b8 00 00 00 00       	mov    $0x0,%eax
    315a:	e8 71 eb ff ff       	callq  1cd0 <__isoc99_sscanf@plt>
    315f:	44 8b 44 24 3c       	mov    0x3c(%rsp),%r8d
    3164:	41 81 f8 c8 00 00 00 	cmp    $0xc8,%r8d
    316b:	0f 85 80 01 00 00    	jne    32f1 <submitr+0x662>
    3171:	48 8d 9c 24 60 20 00 	lea    0x2060(%rsp),%rbx
    3178:	00 
    3179:	48 8d 2d 98 15 00 00 	lea    0x1598(%rip),%rbp        # 4718 <array.3425+0xcf8>
    3180:	4c 8d 6c 24 50       	lea    0x50(%rsp),%r13
    3185:	b9 03 00 00 00       	mov    $0x3,%ecx
    318a:	48 89 de             	mov    %rbx,%rsi
    318d:	48 89 ef             	mov    %rbp,%rdi
    3190:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    3192:	0f 97 c0             	seta   %al
    3195:	1c 00                	sbb    $0x0,%al
    3197:	84 c0                	test   %al,%al
    3199:	0f 84 89 01 00 00    	je     3328 <submitr+0x699>
    319f:	ba 00 20 00 00       	mov    $0x2000,%edx
    31a4:	48 89 de             	mov    %rbx,%rsi
    31a7:	4c 89 ef             	mov    %r13,%rdi
    31aa:	e8 24 fa ff ff       	callq  2bd3 <rio_readlineb>
    31af:	48 85 c0             	test   %rax,%rax
    31b2:	7f d1                	jg     3185 <submitr+0x4f6>
    31b4:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    31bb:	3a 20 43 
    31be:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    31c5:	20 75 6e 
    31c8:	49 89 07             	mov    %rax,(%r15)
    31cb:	49 89 57 08          	mov    %rdx,0x8(%r15)
    31cf:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    31d6:	74 6f 20 
    31d9:	48 ba 72 65 61 64 20 	movabs $0x6165682064616572,%rdx
    31e0:	68 65 61 
    31e3:	49 89 47 10          	mov    %rax,0x10(%r15)
    31e7:	49 89 57 18          	mov    %rdx,0x18(%r15)
    31eb:	48 b8 64 65 72 73 20 	movabs $0x6f72662073726564,%rax
    31f2:	66 72 6f 
    31f5:	48 ba 6d 20 73 65 72 	movabs $0x726576726573206d,%rdx
    31fc:	76 65 72 
    31ff:	49 89 47 20          	mov    %rax,0x20(%r15)
    3203:	49 89 57 28          	mov    %rdx,0x28(%r15)
    3207:	41 c6 47 30 00       	movb   $0x0,0x30(%r15)
    320c:	44 89 e7             	mov    %r12d,%edi
    320f:	e8 3c ea ff ff       	callq  1c50 <close@plt>
    3214:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3219:	e9 5e 01 00 00       	jmpq   337c <submitr+0x6ed>
    321e:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    3225:	3a 20 43 
    3228:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    322f:	20 75 6e 
    3232:	49 89 07             	mov    %rax,(%r15)
    3235:	49 89 57 08          	mov    %rdx,0x8(%r15)
    3239:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    3240:	74 6f 20 
    3243:	48 ba 77 72 69 74 65 	movabs $0x6f74206574697277,%rdx
    324a:	20 74 6f 
    324d:	49 89 47 10          	mov    %rax,0x10(%r15)
    3251:	49 89 57 18          	mov    %rdx,0x18(%r15)
    3255:	48 b8 20 74 68 65 20 	movabs $0x7265732065687420,%rax
    325c:	73 65 72 
    325f:	49 89 47 20          	mov    %rax,0x20(%r15)
    3263:	41 c7 47 28 76 65 72 	movl   $0x726576,0x28(%r15)
    326a:	00 
    326b:	44 89 e7             	mov    %r12d,%edi
    326e:	e8 dd e9 ff ff       	callq  1c50 <close@plt>
    3273:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3278:	e9 ff 00 00 00       	jmpq   337c <submitr+0x6ed>
    327d:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    3284:	3a 20 43 
    3287:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    328e:	20 75 6e 
    3291:	49 89 07             	mov    %rax,(%r15)
    3294:	49 89 57 08          	mov    %rdx,0x8(%r15)
    3298:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    329f:	74 6f 20 
    32a2:	48 ba 72 65 61 64 20 	movabs $0x7269662064616572,%rdx
    32a9:	66 69 72 
    32ac:	49 89 47 10          	mov    %rax,0x10(%r15)
    32b0:	49 89 57 18          	mov    %rdx,0x18(%r15)
    32b4:	48 b8 73 74 20 68 65 	movabs $0x6564616568207473,%rax
    32bb:	61 64 65 
    32be:	48 ba 72 20 66 72 6f 	movabs $0x73206d6f72662072,%rdx
    32c5:	6d 20 73 
    32c8:	49 89 47 20          	mov    %rax,0x20(%r15)
    32cc:	49 89 57 28          	mov    %rdx,0x28(%r15)
    32d0:	41 c7 47 30 65 72 76 	movl   $0x65767265,0x30(%r15)
    32d7:	65 
    32d8:	66 41 c7 47 34 72 00 	movw   $0x72,0x34(%r15)
    32df:	44 89 e7             	mov    %r12d,%edi
    32e2:	e8 69 e9 ff ff       	callq  1c50 <close@plt>
    32e7:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    32ec:	e9 8b 00 00 00       	jmpq   337c <submitr+0x6ed>
    32f1:	4c 8d 8c 24 60 80 00 	lea    0x8060(%rsp),%r9
    32f8:	00 
    32f9:	48 8d 0d 50 13 00 00 	lea    0x1350(%rip),%rcx        # 4650 <array.3425+0xc30>
    3300:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    3307:	be 01 00 00 00       	mov    $0x1,%esi
    330c:	4c 89 ff             	mov    %r15,%rdi
    330f:	b8 00 00 00 00       	mov    $0x0,%eax
    3314:	e8 47 ea ff ff       	callq  1d60 <__sprintf_chk@plt>
    3319:	44 89 e7             	mov    %r12d,%edi
    331c:	e8 2f e9 ff ff       	callq  1c50 <close@plt>
    3321:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3326:	eb 54                	jmp    337c <submitr+0x6ed>
    3328:	48 8d b4 24 60 20 00 	lea    0x2060(%rsp),%rsi
    332f:	00 
    3330:	48 8d 7c 24 50       	lea    0x50(%rsp),%rdi
    3335:	ba 00 20 00 00       	mov    $0x2000,%edx
    333a:	e8 94 f8 ff ff       	callq  2bd3 <rio_readlineb>
    333f:	48 85 c0             	test   %rax,%rax
    3342:	7e 61                	jle    33a5 <submitr+0x716>
    3344:	48 8d b4 24 60 20 00 	lea    0x2060(%rsp),%rsi
    334b:	00 
    334c:	4c 89 ff             	mov    %r15,%rdi
    334f:	e8 ac e8 ff ff       	callq  1c00 <strcpy@plt>
    3354:	44 89 e7             	mov    %r12d,%edi
    3357:	e8 f4 e8 ff ff       	callq  1c50 <close@plt>
    335c:	b9 03 00 00 00       	mov    $0x3,%ecx
    3361:	48 8d 3d b3 13 00 00 	lea    0x13b3(%rip),%rdi        # 471b <array.3425+0xcfb>
    3368:	4c 89 fe             	mov    %r15,%rsi
    336b:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    336d:	0f 97 c0             	seta   %al
    3370:	1c 00                	sbb    $0x0,%al
    3372:	84 c0                	test   %al,%al
    3374:	0f 95 c0             	setne  %al
    3377:	0f b6 c0             	movzbl %al,%eax
    337a:	f7 d8                	neg    %eax
    337c:	48 8b 94 24 68 a0 00 	mov    0xa068(%rsp),%rdx
    3383:	00 
    3384:	64 48 33 14 25 28 00 	xor    %fs:0x28,%rdx
    338b:	00 00 
    338d:	0f 85 a5 01 00 00    	jne    3538 <submitr+0x8a9>
    3393:	48 81 c4 78 a0 00 00 	add    $0xa078,%rsp
    339a:	5b                   	pop    %rbx
    339b:	5d                   	pop    %rbp
    339c:	41 5c                	pop    %r12
    339e:	41 5d                	pop    %r13
    33a0:	41 5e                	pop    %r14
    33a2:	41 5f                	pop    %r15
    33a4:	c3                   	retq   
    33a5:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    33ac:	3a 20 43 
    33af:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    33b6:	20 75 6e 
    33b9:	49 89 07             	mov    %rax,(%r15)
    33bc:	49 89 57 08          	mov    %rdx,0x8(%r15)
    33c0:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    33c7:	74 6f 20 
    33ca:	48 ba 72 65 61 64 20 	movabs $0x6174732064616572,%rdx
    33d1:	73 74 61 
    33d4:	49 89 47 10          	mov    %rax,0x10(%r15)
    33d8:	49 89 57 18          	mov    %rdx,0x18(%r15)
    33dc:	48 b8 74 75 73 20 6d 	movabs $0x7373656d20737574,%rax
    33e3:	65 73 73 
    33e6:	48 ba 61 67 65 20 66 	movabs $0x6d6f726620656761,%rdx
    33ed:	72 6f 6d 
    33f0:	49 89 47 20          	mov    %rax,0x20(%r15)
    33f4:	49 89 57 28          	mov    %rdx,0x28(%r15)
    33f8:	48 b8 20 73 65 72 76 	movabs $0x72657672657320,%rax
    33ff:	65 72 00 
    3402:	49 89 47 30          	mov    %rax,0x30(%r15)
    3406:	44 89 e7             	mov    %r12d,%edi
    3409:	e8 42 e8 ff ff       	callq  1c50 <close@plt>
    340e:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3413:	e9 64 ff ff ff       	jmpq   337c <submitr+0x6ed>
    3418:	48 b8 45 72 72 6f 72 	movabs $0x52203a726f727245,%rax
    341f:	3a 20 52 
    3422:	48 ba 65 73 75 6c 74 	movabs $0x747320746c757365,%rdx
    3429:	20 73 74 
    342c:	49 89 07             	mov    %rax,(%r15)
    342f:	49 89 57 08          	mov    %rdx,0x8(%r15)
    3433:	48 b8 72 69 6e 67 20 	movabs $0x6e6f6320676e6972,%rax
    343a:	63 6f 6e 
    343d:	48 ba 74 61 69 6e 73 	movabs $0x6e6120736e696174,%rdx
    3444:	20 61 6e 
    3447:	49 89 47 10          	mov    %rax,0x10(%r15)
    344b:	49 89 57 18          	mov    %rdx,0x18(%r15)
    344f:	48 b8 20 69 6c 6c 65 	movabs $0x6c6167656c6c6920,%rax
    3456:	67 61 6c 
    3459:	48 ba 20 6f 72 20 75 	movabs $0x72706e7520726f20,%rdx
    3460:	6e 70 72 
    3463:	49 89 47 20          	mov    %rax,0x20(%r15)
    3467:	49 89 57 28          	mov    %rdx,0x28(%r15)
    346b:	48 b8 69 6e 74 61 62 	movabs $0x20656c6261746e69,%rax
    3472:	6c 65 20 
    3475:	48 ba 63 68 61 72 61 	movabs $0x6574636172616863,%rdx
    347c:	63 74 65 
    347f:	49 89 47 30          	mov    %rax,0x30(%r15)
    3483:	49 89 57 38          	mov    %rdx,0x38(%r15)
    3487:	66 41 c7 47 40 72 2e 	movw   $0x2e72,0x40(%r15)
    348e:	41 c6 47 42 00       	movb   $0x0,0x42(%r15)
    3493:	44 89 e7             	mov    %r12d,%edi
    3496:	e8 b5 e7 ff ff       	callq  1c50 <close@plt>
    349b:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    34a0:	e9 d7 fe ff ff       	jmpq   337c <submitr+0x6ed>
    34a5:	48 8d bc 24 60 20 00 	lea    0x2060(%rsp),%rdi
    34ac:	00 
    34ad:	48 8d 84 24 60 40 00 	lea    0x4060(%rsp),%rax
    34b4:	00 
    34b5:	50                   	push   %rax
    34b6:	ff 74 24 20          	pushq  0x20(%rsp)
    34ba:	ff 74 24 30          	pushq  0x30(%rsp)
    34be:	ff 74 24 28          	pushq  0x28(%rsp)
    34c2:	4c 8b 4c 24 28       	mov    0x28(%rsp),%r9
    34c7:	4c 8d 05 b2 11 00 00 	lea    0x11b2(%rip),%r8        # 4680 <array.3425+0xc60>
    34ce:	b9 00 20 00 00       	mov    $0x2000,%ecx
    34d3:	ba 01 00 00 00       	mov    $0x1,%edx
    34d8:	be 00 20 00 00       	mov    $0x2000,%esi
    34dd:	b8 00 00 00 00       	mov    $0x0,%eax
    34e2:	e8 e9 e6 ff ff       	callq  1bd0 <__snprintf_chk@plt>
    34e7:	48 83 c4 20          	add    $0x20,%rsp
    34eb:	3d ff 1f 00 00       	cmp    $0x1fff,%eax
    34f0:	0f 8f 71 fb ff ff    	jg     3067 <submitr+0x3d8>
    34f6:	48 8d bc 24 60 20 00 	lea    0x2060(%rsp),%rdi
    34fd:	00 
    34fe:	48 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%rcx
    3505:	b8 00 00 00 00       	mov    $0x0,%eax
    350a:	f2 ae                	repnz scas %es:(%rdi),%al
    350c:	48 89 ce             	mov    %rcx,%rsi
    350f:	48 f7 d6             	not    %rsi
    3512:	48 89 f1             	mov    %rsi,%rcx
    3515:	48 83 e9 01          	sub    $0x1,%rcx
    3519:	49 89 cd             	mov    %rcx,%r13
    351c:	0f 84 d9 fb ff ff    	je     30fb <submitr+0x46c>
    3522:	48 89 cb             	mov    %rcx,%rbx
    3525:	48 8d ac 24 60 20 00 	lea    0x2060(%rsp),%rbp
    352c:	00 
    352d:	41 be 00 00 00 00    	mov    $0x0,%r14d
    3533:	e9 94 fb ff ff       	jmpq   30cc <submitr+0x43d>
    3538:	e8 f3 e6 ff ff       	callq  1c30 <__stack_chk_fail@plt>

000000000000353d <init_timeout>:
    353d:	85 ff                	test   %edi,%edi
    353f:	74 25                	je     3566 <init_timeout+0x29>
    3541:	53                   	push   %rbx
    3542:	89 fb                	mov    %edi,%ebx
    3544:	48 8d 35 58 f6 ff ff 	lea    -0x9a8(%rip),%rsi        # 2ba3 <sigalrm_handler>
    354b:	bf 0e 00 00 00       	mov    $0xe,%edi
    3550:	e8 2b e7 ff ff       	callq  1c80 <signal@plt>
    3555:	85 db                	test   %ebx,%ebx
    3557:	bf 00 00 00 00       	mov    $0x0,%edi
    355c:	0f 49 fb             	cmovns %ebx,%edi
    355f:	e8 dc e6 ff ff       	callq  1c40 <alarm@plt>
    3564:	5b                   	pop    %rbx
    3565:	c3                   	retq   
    3566:	f3 c3                	repz retq 

0000000000003568 <init_driver>:
    3568:	41 54                	push   %r12
    356a:	55                   	push   %rbp
    356b:	53                   	push   %rbx
    356c:	48 83 ec 20          	sub    $0x20,%rsp
    3570:	49 89 fc             	mov    %rdi,%r12
    3573:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    357a:	00 00 
    357c:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    3581:	31 c0                	xor    %eax,%eax
    3583:	be 01 00 00 00       	mov    $0x1,%esi
    3588:	bf 0d 00 00 00       	mov    $0xd,%edi
    358d:	e8 ee e6 ff ff       	callq  1c80 <signal@plt>
    3592:	be 01 00 00 00       	mov    $0x1,%esi
    3597:	bf 1d 00 00 00       	mov    $0x1d,%edi
    359c:	e8 df e6 ff ff       	callq  1c80 <signal@plt>
    35a1:	be 01 00 00 00       	mov    $0x1,%esi
    35a6:	bf 1d 00 00 00       	mov    $0x1d,%edi
    35ab:	e8 d0 e6 ff ff       	callq  1c80 <signal@plt>
    35b0:	ba 00 00 00 00       	mov    $0x0,%edx
    35b5:	be 01 00 00 00       	mov    $0x1,%esi
    35ba:	bf 02 00 00 00       	mov    $0x2,%edi
    35bf:	e8 ac e7 ff ff       	callq  1d70 <socket@plt>
    35c4:	85 c0                	test   %eax,%eax
    35c6:	0f 88 a3 00 00 00    	js     366f <init_driver+0x107>
    35cc:	89 c3                	mov    %eax,%ebx
    35ce:	48 8d 3d 49 11 00 00 	lea    0x1149(%rip),%rdi        # 471e <array.3425+0xcfe>
    35d5:	e8 b6 e6 ff ff       	callq  1c90 <gethostbyname@plt>
    35da:	48 85 c0             	test   %rax,%rax
    35dd:	0f 84 df 00 00 00    	je     36c2 <init_driver+0x15a>
    35e3:	48 89 e5             	mov    %rsp,%rbp
    35e6:	48 c7 44 24 02 00 00 	movq   $0x0,0x2(%rsp)
    35ed:	00 00 
    35ef:	c7 45 0a 00 00 00 00 	movl   $0x0,0xa(%rbp)
    35f6:	66 c7 45 0e 00 00    	movw   $0x0,0xe(%rbp)
    35fc:	66 c7 04 24 02 00    	movw   $0x2,(%rsp)
    3602:	48 63 50 14          	movslq 0x14(%rax),%rdx
    3606:	48 8b 40 18          	mov    0x18(%rax),%rax
    360a:	48 8d 7d 04          	lea    0x4(%rbp),%rdi
    360e:	b9 0c 00 00 00       	mov    $0xc,%ecx
    3613:	48 8b 30             	mov    (%rax),%rsi
    3616:	e8 85 e6 ff ff       	callq  1ca0 <__memmove_chk@plt>
    361b:	66 c7 44 24 02 3b 6e 	movw   $0x6e3b,0x2(%rsp)
    3622:	ba 10 00 00 00       	mov    $0x10,%edx
    3627:	48 89 ee             	mov    %rbp,%rsi
    362a:	89 df                	mov    %ebx,%edi
    362c:	e8 ef e6 ff ff       	callq  1d20 <connect@plt>
    3631:	85 c0                	test   %eax,%eax
    3633:	0f 88 fb 00 00 00    	js     3734 <init_driver+0x1cc>
    3639:	89 df                	mov    %ebx,%edi
    363b:	e8 10 e6 ff ff       	callq  1c50 <close@plt>
    3640:	66 41 c7 04 24 4f 4b 	movw   $0x4b4f,(%r12)
    3647:	41 c6 44 24 02 00    	movb   $0x0,0x2(%r12)
    364d:	b8 00 00 00 00       	mov    $0x0,%eax
    3652:	48 8b 4c 24 18       	mov    0x18(%rsp),%rcx
    3657:	64 48 33 0c 25 28 00 	xor    %fs:0x28,%rcx
    365e:	00 00 
    3660:	0f 85 06 01 00 00    	jne    376c <init_driver+0x204>
    3666:	48 83 c4 20          	add    $0x20,%rsp
    366a:	5b                   	pop    %rbx
    366b:	5d                   	pop    %rbp
    366c:	41 5c                	pop    %r12
    366e:	c3                   	retq   
    366f:	48 b8 45 72 72 6f 72 	movabs $0x43203a726f727245,%rax
    3676:	3a 20 43 
    3679:	48 ba 6c 69 65 6e 74 	movabs $0x6e7520746e65696c,%rdx
    3680:	20 75 6e 
    3683:	49 89 04 24          	mov    %rax,(%r12)
    3687:	49 89 54 24 08       	mov    %rdx,0x8(%r12)
    368c:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    3693:	74 6f 20 
    3696:	48 ba 63 72 65 61 74 	movabs $0x7320657461657263,%rdx
    369d:	65 20 73 
    36a0:	49 89 44 24 10       	mov    %rax,0x10(%r12)
    36a5:	49 89 54 24 18       	mov    %rdx,0x18(%r12)
    36aa:	41 c7 44 24 20 6f 63 	movl   $0x656b636f,0x20(%r12)
    36b1:	6b 65 
    36b3:	66 41 c7 44 24 24 74 	movw   $0x74,0x24(%r12)
    36ba:	00 
    36bb:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    36c0:	eb 90                	jmp    3652 <init_driver+0xea>
    36c2:	48 b8 45 72 72 6f 72 	movabs $0x44203a726f727245,%rax
    36c9:	3a 20 44 
    36cc:	48 ba 4e 53 20 69 73 	movabs $0x6e7520736920534e,%rdx
    36d3:	20 75 6e 
    36d6:	49 89 04 24          	mov    %rax,(%r12)
    36da:	49 89 54 24 08       	mov    %rdx,0x8(%r12)
    36df:	48 b8 61 62 6c 65 20 	movabs $0x206f7420656c6261,%rax
    36e6:	74 6f 20 
    36e9:	48 ba 72 65 73 6f 6c 	movabs $0x2065766c6f736572,%rdx
    36f0:	76 65 20 
    36f3:	49 89 44 24 10       	mov    %rax,0x10(%r12)
    36f8:	49 89 54 24 18       	mov    %rdx,0x18(%r12)
    36fd:	48 b8 73 65 72 76 65 	movabs $0x6120726576726573,%rax
    3704:	72 20 61 
    3707:	49 89 44 24 20       	mov    %rax,0x20(%r12)
    370c:	41 c7 44 24 28 64 64 	movl   $0x65726464,0x28(%r12)
    3713:	72 65 
    3715:	66 41 c7 44 24 2c 73 	movw   $0x7373,0x2c(%r12)
    371c:	73 
    371d:	41 c6 44 24 2e 00    	movb   $0x0,0x2e(%r12)
    3723:	89 df                	mov    %ebx,%edi
    3725:	e8 26 e5 ff ff       	callq  1c50 <close@plt>
    372a:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    372f:	e9 1e ff ff ff       	jmpq   3652 <init_driver+0xea>
    3734:	4c 8d 05 e3 0f 00 00 	lea    0xfe3(%rip),%r8        # 471e <array.3425+0xcfe>
    373b:	48 8d 0d 96 0f 00 00 	lea    0xf96(%rip),%rcx        # 46d8 <array.3425+0xcb8>
    3742:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    3749:	be 01 00 00 00       	mov    $0x1,%esi
    374e:	4c 89 e7             	mov    %r12,%rdi
    3751:	b8 00 00 00 00       	mov    $0x0,%eax
    3756:	e8 05 e6 ff ff       	callq  1d60 <__sprintf_chk@plt>
    375b:	89 df                	mov    %ebx,%edi
    375d:	e8 ee e4 ff ff       	callq  1c50 <close@plt>
    3762:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    3767:	e9 e6 fe ff ff       	jmpq   3652 <init_driver+0xea>
    376c:	e8 bf e4 ff ff       	callq  1c30 <__stack_chk_fail@plt>

0000000000003771 <driver_post>:
    3771:	53                   	push   %rbx
    3772:	4c 89 c3             	mov    %r8,%rbx
    3775:	85 c9                	test   %ecx,%ecx
    3777:	75 17                	jne    3790 <driver_post+0x1f>
    3779:	48 85 ff             	test   %rdi,%rdi
    377c:	74 05                	je     3783 <driver_post+0x12>
    377e:	80 3f 00             	cmpb   $0x0,(%rdi)
    3781:	75 33                	jne    37b6 <driver_post+0x45>
    3783:	66 c7 03 4f 4b       	movw   $0x4b4f,(%rbx)
    3788:	c6 43 02 00          	movb   $0x0,0x2(%rbx)
    378c:	89 c8                	mov    %ecx,%eax
    378e:	5b                   	pop    %rbx
    378f:	c3                   	retq   
    3790:	48 8d 35 a2 0f 00 00 	lea    0xfa2(%rip),%rsi        # 4739 <array.3425+0xd19>
    3797:	bf 01 00 00 00       	mov    $0x1,%edi
    379c:	b8 00 00 00 00       	mov    $0x0,%eax
    37a1:	e8 3a e5 ff ff       	callq  1ce0 <__printf_chk@plt>
    37a6:	66 c7 03 4f 4b       	movw   $0x4b4f,(%rbx)
    37ab:	c6 43 02 00          	movb   $0x0,0x2(%rbx)
    37af:	b8 00 00 00 00       	mov    $0x0,%eax
    37b4:	eb d8                	jmp    378e <driver_post+0x1d>
    37b6:	41 50                	push   %r8
    37b8:	52                   	push   %rdx
    37b9:	4c 8d 0d 90 0f 00 00 	lea    0xf90(%rip),%r9        # 4750 <array.3425+0xd30>
    37c0:	49 89 f0             	mov    %rsi,%r8
    37c3:	48 89 f9             	mov    %rdi,%rcx
    37c6:	48 8d 15 87 0f 00 00 	lea    0xf87(%rip),%rdx        # 4754 <array.3425+0xd34>
    37cd:	be 6e 3b 00 00       	mov    $0x3b6e,%esi
    37d2:	48 8d 3d 45 0f 00 00 	lea    0xf45(%rip),%rdi        # 471e <array.3425+0xcfe>
    37d9:	e8 b1 f4 ff ff       	callq  2c8f <submitr>
    37de:	48 83 c4 10          	add    $0x10,%rsp
    37e2:	eb aa                	jmp    378e <driver_post+0x1d>
    37e4:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    37eb:	00 00 00 
    37ee:	66 90                	xchg   %ax,%ax

00000000000037f0 <__libc_csu_init>:
    37f0:	41 57                	push   %r15
    37f2:	41 56                	push   %r14
    37f4:	49 89 d7             	mov    %rdx,%r15
    37f7:	41 55                	push   %r13
    37f9:	41 54                	push   %r12
    37fb:	4c 8d 25 de 24 20 00 	lea    0x2024de(%rip),%r12        # 205ce0 <__frame_dummy_init_array_entry>
    3802:	55                   	push   %rbp
    3803:	48 8d 2d de 24 20 00 	lea    0x2024de(%rip),%rbp        # 205ce8 <__init_array_end>
    380a:	53                   	push   %rbx
    380b:	41 89 fd             	mov    %edi,%r13d
    380e:	49 89 f6             	mov    %rsi,%r14
    3811:	4c 29 e5             	sub    %r12,%rbp
    3814:	48 83 ec 08          	sub    $0x8,%rsp
    3818:	48 c1 fd 03          	sar    $0x3,%rbp
    381c:	e8 6f e3 ff ff       	callq  1b90 <_init>
    3821:	48 85 ed             	test   %rbp,%rbp
    3824:	74 20                	je     3846 <__libc_csu_init+0x56>
    3826:	31 db                	xor    %ebx,%ebx
    3828:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    382f:	00 
    3830:	4c 89 fa             	mov    %r15,%rdx
    3833:	4c 89 f6             	mov    %r14,%rsi
    3836:	44 89 ef             	mov    %r13d,%edi
    3839:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
    383d:	48 83 c3 01          	add    $0x1,%rbx
    3841:	48 39 dd             	cmp    %rbx,%rbp
    3844:	75 ea                	jne    3830 <__libc_csu_init+0x40>
    3846:	48 83 c4 08          	add    $0x8,%rsp
    384a:	5b                   	pop    %rbx
    384b:	5d                   	pop    %rbp
    384c:	41 5c                	pop    %r12
    384e:	41 5d                	pop    %r13
    3850:	41 5e                	pop    %r14
    3852:	41 5f                	pop    %r15
    3854:	c3                   	retq   
    3855:	90                   	nop
    3856:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    385d:	00 00 00 

0000000000003860 <__libc_csu_fini>:
    3860:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000003864 <_fini>:
    3864:	48 83 ec 08          	sub    $0x8,%rsp
    3868:	48 83 c4 08          	add    $0x8,%rsp
    386c:	c3                   	retq   
