# shopify-scripts

Disclosed reports: **161**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 181879 | Code Injection | critical | $18000 | [Struct type confusion RCE](181879-struct-type-confusion-rce.md) |
| 187305 | Uncontrolled Resource Consumption | high | $10000 | [Invalid handling of zero-length heredoc identifiers leads to infinite loop in the sandbox](187305-invalid-handling-of-zero-length-heredoc-identifiers-leads-to.md) |
| 186723 | Memory Corruption - Generic | high | $10000 | [Crash: Overwriting NoMethodError with a builtin class crashes/corrupts memory](186723-crash-overwriting-nomethoderror-with-a-builtin-class-crashes.md) |
| 183356 | Uncontrolled Resource Consumption | high | $10000 | [Segfault and/or potential unwanted (byte)code execution with "break" and "\|\|=" inside a loop](183356-segfault-and-or-potential-unwanted-byte-code-execution-with.md) |
| 188326 | Uncontrolled Resource Consumption | high | $10000 | [Buffer overflow in mrb_time_asctime](188326-buffer-overflow-in-mrb-time-asctime.md) |
| 189633 | Memory Corruption - Generic | high | $10000 | [Certain inputs cause tight C-level recursion leading to process stack overflow](189633-certain-inputs-cause-tight-c-level-recursion-leading-to-proc.md) |
| 182484 | Uncontrolled Resource Consumption | high | $10000 | [Broken handling of maximum number of method call arguments leads to segfault](182484-broken-handling-of-maximum-number-of-method-call-arguments-l.md) |
| 185775 | Crash: Initialize Decimal with itself triggers an assertion | high | $10000 | [Crash: Initialize Decimal with itself triggers an assertion](185775-crash-initialize-decimal-with-itself-triggers-an-assertion.md) |
| 187536 | Uncontrolled Resource Consumption | high | $10000 | [Null pointer derefence due to bug in codegen with negation without using value](187536-null-pointer-derefence-due-to-bug-in-codegen-with-negation-w.md) |
| 181685 | Uncontrolled Resource Consumption | high | $10000 | [Range#initialize_copy null pointer dereference](181685-range-initialize-copy-null-pointer-dereference.md) |
| 181910 | Uncontrolled Resource Consumption | high | $10000 | [Range constructor type confusion DoS](181910-range-constructor-type-confusion-dos.md) |
| 181828 | Uncontrolled Resource Consumption | high | $10000 | [Segfault in mruby, mruby_engine and the parent MRI Ruby due to null pointer dereference](181828-segfault-in-mruby-mruby-engine-and-the-parent-mri-ruby-due-t.md) |
| 183425 | Uncontrolled Resource Consumption | high | $8000 | [Segmentation fault when a Ruby method is invoked by a C method via Object#send](183425-segmentation-fault-when-a-ruby-method-is-invoked-by-a-c-meth.md) |
| 183405 | Uncontrolled Resource Consumption | high | $8000 | [Null target_class DoS](183405-null-target-class-dos.md) |
| 184712 | Uncontrolled Resource Consumption | high | $8000 | [Denial of service due to invalid memory access in mrb_ary_concat](184712-denial-of-service-due-to-invalid-memory-access-in-mrb-ary-co.md) |
| 181232 | Uncontrolled Resource Consumption | high | $8000 | [Denial of Service in mruby due to null pointer dereference](181232-denial-of-service-in-mruby-due-to-null-pointer-dereference.md) |
| 181695 | Uncontrolled Resource Consumption | high | $8000 | [Undefined method_missing null pointer dereference](181695-undefined-method-missing-null-pointer-dereference.md) |
| 180695 | Uncontrolled Resource Consumption | high | $8000 | [ruby DoS https://www.mruby.science](180695-ruby-dos-https-www-mruby-science.md) |
| 188313 | Uncontrolled Resource Consumption | high | $8000 | [Segmentation fault due to bad memory access in kh_get_mt](188313-segmentation-fault-due-to-bad-memory-access-in-kh-get-mt.md) |
| 185794 | Memory Corruption - Generic | high | $8000 | [Crash: mrb_any_to_s can't handle NilClass, Symbol and Fixnum](185794-crash-mrb-any-to-s-can-t-handle-nilclass-symbol-and-fixnum.md) |
| 184857 | Memory Corruption - Generic | high | $8000 | [Crash: calling Proc::initialize_copy with a Proc instance where initialize never ran leads to a crash](184857-crash-calling-proc-initialize-copy-with-a-proc-instance-wher.md) |
| 184661 | Memory Corruption - Generic | high | $8000 | [mruby-time: Crash host with uninitialized Time obj](184661-mruby-time-crash-host-with-uninitialized-time-obj.md) |
| 201897 | Memory Corruption - Generic | low | $2000 | [Recursion causing uninitialized memory reads leading to a segfault](201897-recursion-causing-uninitialized-memory-reads-leading-to-a-se.md) |
| 535827 | Classic Buffer Overflow | n/a | $1000 | [Buffer overflow in yywarning_s](535827-buffer-overflow-in-yywarning-s.md) |
| 621308 | NULL Pointer Dereference | n/a | $1000 | [NULL pointer dereference in `mrb_check_frozen`](621308-null-pointer-dereference-in-mrb-check-frozen.md) |
| 191689 | Uncontrolled Resource Consumption | low | $1000 | [Incorrect code generation when result of NODE_NEGATE is not used](191689-incorrect-code-generation-when-result-of-node-negate-is-not.md) |
| 184715 | Memory Corruption - Generic | n/a | $1000 | [Read after free in mrb_vm_exec with OP_ARYCAT reading R(B)](184715-read-after-free-in-mrb-vm-exec-with-op-arycat-reading-r-b.md) |
| 633607 | Out-of-bounds Read | n/a | $1000 | [Invalid read in `str_replace_partial`](633607-invalid-read-in-str-replace-partial.md) |
| 192896 | Memory Corruption - Generic | low | $1000 | [Memory disclosure in timegm](192896-memory-disclosure-in-timegm.md) |
| 185899 | Uncontrolled Resource Consumption | low | $1000 | [Invalid memory write caused by incorrect upper bound in array_copy](185899-invalid-memory-write-caused-by-incorrect-upper-bound-in-arra.md) |
| 190133 | Uncontrolled Resource Consumption | low | $1000 | [Segfault when passing invalid values to `values_at`](190133-segfault-when-passing-invalid-values-to-values-at.md) |
| 185387 | Uncontrolled Resource Consumption | low | $1000 | [Null pointer dereference regression in parse.y](185387-null-pointer-dereference-regression-in-parse-y.md) |
| 185957 | Memory Corruption - Generic | low | $1000 | [Crash: A call to Symbol.new leads to a crash when inspecting the resulting object](185957-crash-a-call-to-symbol-new-leads-to-a-crash-when-inspecting.md) |
| 204047 | Uncontrolled Resource Consumption | low | $1000 | [Segmentation fault while printing backtrace](204047-segmentation-fault-while-printing-backtrace.md) |
| 420115 | NULL Pointer Dereference | n/a | $800 | [Crash in mrb_ary_push](420115-crash-in-mrb-ary-push.md) |
| 204421 | Memory Corruption - Generic | n/a | $800 | [Heap buffer oveflow with many arguments](204421-heap-buffer-oveflow-with-many-arguments.md) |
| 216992 | Uncontrolled Resource Consumption | n/a | $800 | [Heap Buffer Overflow in mrb_hash_keys](216992-heap-buffer-overflow-in-mrb-hash-keys.md) |
| 214681 | NULL Pointer Dereference | low | $800 | [Null pointer dereference in ary_concat ](214681-null-pointer-dereference-in-ary-concat.md) |
| 213261 | Uncontrolled Resource Consumption | low | $800 | [Use-after-free leading to an invalid pointer dereference](213261-use-after-free-leading-to-an-invalid-pointer-dereference.md) |
| 193143 | Memory Corruption - Generic | n/a | $800 | [Use After Free in str_replace](193143-use-after-free-in-str-replace.md) |
| 295380 | Heap Overflow | none | $800 | [heap-buffer-overflow in OP_R_BREAK](295380-heap-buffer-overflow-in-op-r-break.md) |
| 296198 | Memory Corruption - Generic | n/a | $800 | [SEGV on ary_concat](296198-segv-on-ary-concat.md) |
| 295680 | Out-of-bounds Read | low | $800 | [Invalid read leading to a segfault](295680-invalid-read-leading-to-a-segfault.md) |
| 214171 | Uncontrolled Resource Consumption | n/a | $800 | [Null pointer dereferences in ary_concat](214171-null-pointer-dereferences-in-ary-concat.md) |
| 210671 | Uncontrolled Resource Consumption | n/a | $800 | [Null pointer dereferences from mrb_vm_exec](210671-null-pointer-dereferences-from-mrb-vm-exec.md) |
| 196819 | Uncontrolled Resource Consumption | low | $800 | [Heap Buffer overflow in mrb_funcall_with_block](196819-heap-buffer-overflow-in-mrb-funcall-with-block.md) |
| 194906 | Memory Corruption - Generic | n/a | $800 | [Heap overflow due to off-by-one when expanding stack](194906-heap-overflow-due-to-off-by-one-when-expanding-stack.md) |
| 295276 | Use After Free | n/a | $800 | [heap-use-after-free in OP_RESCUE](295276-heap-use-after-free-in-op-rescue.md) |
| 216351 | Uncontrolled Resource Consumption | n/a | $800 | [Null pointer dereferences in mrb_get_args](216351-null-pointer-dereferences-in-mrb-get-args.md) |
| 206239 | Uncontrolled Resource Consumption | n/a | $800 | [Heap Buffer Overflow while processing OP_SEND](206239-heap-buffer-overflow-while-processing-op-send.md) |
| 192362 | Memory Corruption - Generic | low | $800 | [Heap Overflow in mrb_arb_splice](192362-heap-overflow-in-mrb-arb-splice.md) |
| 222294 | Memory Corruption - Generic | medium | $800 | [heap-use-after-free in mrb_vm_exec - vm.c:1247](222294-heap-use-after-free-in-mrb-vm-exec-vm-c-1247.md) |
| 221712 | Null pointer dereferences in kh_copy_mt | n/a | $800 | [Null pointer dereferences in kh_copy_mt](221712-null-pointer-dereferences-in-kh-copy-mt.md) |
| 218570 | Uncontrolled Resource Consumption | low | $800 | [Invalid pointer dereference in OP_ENTER](218570-invalid-pointer-dereference-in-op-enter.md) |
| 218233 | NULL Pointer Dereference | low | $800 | [Null pointer dereference in OP_ENTER](218233-null-pointer-dereference-in-op-enter.md) |
| 215891 | NULL Pointer Dereference | low | $800 | [Null pointer dereference in mrb_class](215891-null-pointer-dereference-in-mrb-class.md) |
| 217610 | Memory Corruption - Generic | medium | $800 | [kh_put_iv SEGFAULT - mruby 1.2.0](217610-kh-put-iv-segfault-mruby-1-2-0.md) |
| 211021 | Uncontrolled Resource Consumption | n/a | $800 | [Null pointer dereference in 'get_file'](211021-null-pointer-dereference-in-get-file.md) |
| 210246 | Uncontrolled Resource Consumption | n/a | $800 | [Invalid Pointer Reference from OP_RESCUE](210246-invalid-pointer-reference-from-op-rescue.md) |
| 205521 | Uncontrolled Resource Consumption | n/a | $800 | [Heap Buffer overflow in mrb_ary_unshift](205521-heap-buffer-overflow-in-mrb-ary-unshift.md) |
| 205536 | Uncontrolled Resource Consumption | n/a | $800 | [Use After Free in mrb_vm_exec](205536-use-after-free-in-mrb-vm-exec.md) |
| 197719 | Uncontrolled Resource Consumption | n/a | $800 | [Still heap overflow in mrb_ary_splice](197719-still-heap-overflow-in-mrb-ary-splice.md) |
| 193081 | Uncontrolled Resource Consumption | n/a | $800 | [Null pointer dereference in mrb_str_prepend](193081-null-pointer-dereference-in-mrb-str-prepend.md) |
| 242354 | NULL Pointer Dereference | n/a | $800 | [Null pointer dereference with send/method_missing](242354-null-pointer-dereference-with-send-method-missing.md) |
| 218567 | Memory Corruption - Generic | medium | $800 | [SIGSEGV in array_copy - array.c:71](218567-sigsegv-in-array-copy-array-c-71.md) |
| 208526 | Uncontrolled Resource Consumption | low | $800 | [Null pointer dereference in mark_context_stack](208526-null-pointer-dereference-in-mark-context-stack.md) |
| 212107 | Uncontrolled Resource Consumption | low | $800 | [Null pointer dereference in mrb_class](212107-null-pointer-dereference-in-mrb-class.md) |
| 209449 | Uncontrolled Resource Consumption | n/a | $800 | [Heap buffer overflow with long array assignment](209449-heap-buffer-overflow-with-long-array-assignment.md) |
| 244904 | Use After Free | n/a | $800 | [Use after free in mruby-mpdecimal](244904-use-after-free-in-mruby-mpdecimal.md) |
| 215854 | Uncontrolled Resource Consumption | low | $300 | [Garbage collector crash](215854-garbage-collector-crash.md) |
| 193719 | Memory Corruption - Generic | n/a | $200 | [Double free of filename after codegen error](193719-double-free-of-filename-after-codegen-error.md) |
| 194884 | Memory Corruption - Generic | low | $200 | [Heap use-after-free during range creation](194884-heap-use-after-free-during-range-creation.md) |
| 208363 | Memory Corruption - Generic | high | $100 | [Memory corrouption in mrb_gc_mark](208363-memory-corrouption-in-mrb-gc-mark.md) |
| 202362 | Uncontrolled Resource Consumption | none | $100 | [Null pointer dereference in mrb_random_initialize](202362-null-pointer-dereference-in-mrb-random-initialize.md) |
| 205884 | Uncontrolled Resource Consumption | high | $100 | [Interger overflow in str_substr leading to read/write out of bound memory](205884-interger-overflow-in-str-substr-leading-to-read-write-out-of.md) |
| 192665 | Memory Corruption - Generic | none | $100 | [heap-buffer-overflow on mruby](192665-heap-buffer-overflow-on-mruby.md) |
| 191328 | Uncontrolled Resource Consumption | none | $100 | [Invalid memory access in `mrb_str_format`](191328-invalid-memory-access-in-mrb-str-format.md) |
| 212239 | sprintf gem - format string combined attack | none | $100 | [sprintf gem - format string combined attack](212239-sprintf-gem-format-string-combined-attack.md) |
| 207321 | Information Disclosure | medium | $100 | [Controlled address leak due to type confusion - ASLR bypass](207321-controlled-address-leak-due-to-type-confusion-aslr-bypass.md) |
| 204628 | Uncontrolled Resource Consumption | medium | $100 | [segafult in mruby's sprintf - mrb_str_format](204628-segafult-in-mruby-s-sprintf-mrb-str-format.md) |
| 200387 | Uncontrolled Resource Consumption | low | $100 | [Incorrect code generation with redo inside NODE_RESCUE.](200387-incorrect-code-generation-with-redo-inside-node-rescue.md) |
| 201903 | Uncontrolled Resource Consumption | medium | $100 | [Segmentfault at mrb_vm_exec](201903-segmentfault-at-mrb-vm-exec.md) |
| 200821 | Memory Corruption - Generic | n/a | $100 | [ heap-use-after-free /home/operac/testafl/mruby/mrubylast/mruby/src/gc.c](200821-heap-use-after-free-home-operac-testafl-mruby-mrubylast-mrub.md) |
| 197916 | Uncontrolled Resource Consumption | n/a | $100 | [Crash in print_backtrace](197916-crash-in-print-backtrace.md) |
| 192235 | Memory Corruption - Generic | n/a | $100 | [Integer Overflow in mrb_ary_set](192235-integer-overflow-in-mrb-ary-set.md) |
| 219293 | Uncontrolled Resource Consumption | n/a | $100 | [Invalid Pointer reference in L_RESCUE](219293-invalid-pointer-reference-in-l-rescue.md) |
| 222171 | heap use after free in fiber_switch | n/a | $100 | [heap use after free in fiber_switch](222171-heap-use-after-free-in-fiber-switch.md) |
| 218803 | Memory Corruption - Generic | medium | $100 | [SIGABRT in sym_validate_len - symbol.c:44](218803-sigabrt-in-sym-validate-len-symbol-c-44.md) |
| 181871 | Uncontrolled Resource Consumption | critical | $0 | [DoS: type confusion in mrb_no_method_error](181871-dos-type-confusion-in-mrb-no-method-error.md) |
| 185041 | Uncontrolled Resource Consumption | critical | $0 | [Type confusion in mrb_exc_set leading to memory corruption](185041-type-confusion-in-mrb-exc-set-leading-to-memory-corruption.md) |
| 185051 | Code Injection | critical | $0 | [Type confusion in wrap_decimal leading to memory corruption](185051-type-confusion-in-wrap-decimal-leading-to-memory-corruption.md) |
| 181321 | Code Injection | critical | $0 | [Use after free vulnerability in mruby Array#to_h causing DOS possible RCE](181321-use-after-free-vulnerability-in-mruby-array-to-h-causing-dos.md) |
| 181893 | Code Injection | critical | $0 | [TOCTTOU bug in mrb_str_setbyte leading the memory corruption](181893-tocttou-bug-in-mrb-str-setbyte-leading-the-memory-corruption.md) |
| 182274 | Uncontrolled Resource Consumption | high | $0 | [Null pointer dereference due to TOCTTOU bug in mrb_time_initialize](182274-null-pointer-dereference-due-to-tocttou-bug-in-mrb-time-init.md) |
| 193773 | Memory Corruption - Generic | low | $0 | [SIGABRT - mrb_default_allocf ](193773-sigabrt-mrb-default-allocf.md) |
| 180977 | Uncontrolled Resource Consumption | high | $0 | [Exception cause SIGABRT](180977-exception-cause-sigabrt.md) |
| 196416 | Violation of Secure Design Principles | none | $0 | [Clearing , Shifting and Pop Value from Frozen Array  ](196416-clearing-shifting-and-pop-value-from-frozen-array.md) |
| 194866 | Violation of Secure Design Principles | none | $0 | [Deleting Key-value pair from Frozen HASH or Clearing a Frozen HASH](194866-deleting-key-value-pair-from-frozen-hash-or-clearing-a-froze.md) |
| 196498 | Memory Corruption - Generic | low | $0 | [Segmentation fault on program counter](196498-segmentation-fault-on-program-counter.md) |
| 181677 | Uncontrolled Resource Consumption | high | $0 | [NULL pointer dereference when parsing ternary operators](181677-null-pointer-dereference-when-parsing-ternary-operators.md) |
| 181319 | Memory Corruption - Generic | high | $0 | [Memory disclosure in mruby String#lines method](181319-memory-disclosure-in-mruby-string-lines-method.md) |
| 181874 | Uncontrolled Resource Consumption | high | $0 | [SIGSEGV when invalid argument on remove_method](181874-sigsegv-when-invalid-argument-on-remove-method.md) |
| 197694 | Uncontrolled Resource Consumption | n/a | $0 | [SIGSEGV - mrb_obj_extend - line:413](197694-sigsegv-mrb-obj-extend-line-413.md) |
| 192578 | Memory Corruption - Generic | low | $0 | [kh_get_n2s() stack overrun](192578-kh-get-n2s-stack-overrun.md) |
| 209937 | Memory Corruption - Generic | n/a | $0 | [SIGSEGV - mark_context_stack](209937-sigsegv-mark-context-stack.md) |
| 214000 | Memory Corruption - Generic | n/a | $0 | [SIGABRT - mirb and mruby](214000-sigabrt-mirb-and-mruby.md) |
| 214845 | NULL Pointer Dereference | n/a | $0 | [SIGSEGV in mrb_vm_exec](214845-sigsegv-in-mrb-vm-exec.md) |
| 215967 | Memory Corruption - Generic | n/a | $0 | [SIGABRT in mrb_debug_info_append_file](215967-sigabrt-in-mrb-debug-info-append-file.md) |
| 216725 | Memory Corruption - Generic | n/a | $0 | [SIGABRT - in free](216725-sigabrt-in-free.md) |
| 213779 | Uncontrolled Resource Consumption | medium | $0 | [SIGSEGV - mrb_obj_value](213779-sigsegv-mrb-obj-value.md) |
| 197693 | Uncontrolled Resource Consumption | n/a | $0 | [SIGSEGV - mrb_vm_exec - line:1681](197693-sigsegv-mrb-vm-exec-line-1681.md) |
| 193517 | Memory Corruption - Generic | high | $0 | [attempting double-free using the mruby compiler `mrbc`](193517-attempting-double-free-using-the-mruby-compiler-mrbc.md) |
| 193077 | Uncontrolled Resource Consumption | n/a | $0 | [mrb_str_modify try to write to memory not marked for writing](193077-mrb-str-modify-try-to-write-to-memory-not-marked-for-writing.md) |
| 214576 | Double Free | n/a | $0 | [SIGABRT - mirb - Double Free](214576-sigabrt-mirb-double-free.md) |
| 215447 | NULL Pointer Dereference | n/a | $0 | [SIGSEGV in mrb_class](215447-sigsegv-in-mrb-class.md) |
| 213255 | Memory Corruption - Generic | n/a | $0 | [SIGSEGV in str_buf_cat](213255-sigsegv-in-str-buf-cat.md) |
| 210429 | Uncontrolled Resource Consumption | medium | $0 | [mrb_vm_exec - null ptr dereference](210429-mrb-vm-exec-null-ptr-dereference.md) |
| 201905 | Uncontrolled Resource Consumption | n/a | $0 | [SIGSEGV - vm.c - line:1214](201905-sigsegv-vm-c-line-1214.md) |
| 205284 | Memory Corruption - Generic | n/a | $0 | [SIGABRT - method_missing - mark_context_stack](205284-sigabrt-method-missing-mark-context-stack.md) |
| 196386 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV - mrb_vm_exec - vm.c in line:1272](196386-sigsegv-mrb-vm-exec-vm-c-in-line-1272.md) |
| 192734 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV Null Pointer mrb_str_concat()](192734-sigsegv-null-pointer-mrb-str-concat.md) |
| 182027 | Uncontrolled Resource Consumption | high | $0 | [SIGSEV on mrb_ary_splice](182027-sigsev-on-mrb-ary-splice.md) |
| 183231 | Uncontrolled Resource Consumption | high | $0 | [SIGSEGV on mruby mrb_str_modify() (Invalid memory access)](183231-sigsegv-on-mruby-mrb-str-modify-invalid-memory-access.md) |
| 183239 | Memory Corruption - Generic | high | $0 | [SIGSEGV on mruby's mark_tbl() (Invalid memory access)](183239-sigsegv-on-mruby-s-mark-tbl-invalid-memory-access.md) |
| 297383 | Uncontrolled Resource Consumption | n/a | $0 | [mruby heredoc notation](297383-mruby-heredoc-notation.md) |
| 216700 | heap use-after-free in mrb_vm_exec() | n/a | $0 | [heap use-after-free in mrb_vm_exec()](216700-heap-use-after-free-in-mrb-vm-exec.md) |
| 217083 | NULL Pointer Dereference | n/a | $0 | [SIGSEGV in mrb_str_inum](217083-sigsegv-in-mrb-str-inum.md) |
| 217097 | NULL Pointer Dereference | n/a | $0 | [SIGSEGV in mrb_vm_exec](217097-sigsegv-in-mrb-vm-exec.md) |
| 212882 | Memory Corruption - Generic | n/a | $0 | [SIGABRT in only mirb](212882-sigabrt-in-only-mirb.md) |
| 212074 | Violation of Secure Design Principles | medium | $0 | [SIGSEGV - mrb_yield_with_class](212074-sigsegv-mrb-yield-with-class.md) |
| 198452 | Memory Corruption - Generic | n/a | $0 | [SIGABRT - mrb_realloc_simple - gc.c - line:201](198452-sigabrt-mrb-realloc-simple-gc-c-line-201.md) |
| 203513 | Uncontrolled Resource Consumption | n/a | $0 | [SIGSEGV - mrb_vm_exec - line:1312](203513-sigsegv-mrb-vm-exec-line-1312.md) |
| 193724 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV - kh_resize_iv - Null Deref](193724-sigsegv-kh-resize-iv-null-deref.md) |
| 199764 | Uncontrolled Resource Consumption | n/a | $0 | [Aborted - proc.c - line:143](199764-aborted-proc-c-line-143.md) |
| 196380 | Memory Corruption - Generic | n/a | $0 | [SIGSEGV in mrb_vm_exec](196380-sigsegv-in-mrb-vm-exec.md) |
| 204774 | A crash when an exception is caught in a caller and the receiver returned from `ensure` | n/a | $0 | [A crash when an exception is caught in a caller and the receiver returned from `ensure`](204774-a-crash-when-an-exception-is-caught-in-a-caller-and-the-rece.md) |
| 191994 | Memory Corruption - Generic | low | $0 | [SIGSEGV mrb_obj_freeze() Manipulating Register RAX and RSI](191994-sigsegv-mrb-obj-freeze-manipulating-register-rax-and-rsi.md) |
| 191938 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV on mruby mrb_get_args() ](191938-sigsegv-on-mruby-mrb-get-args.md) |
| 192318 | Memory Corruption - Generic | none | $0 | [mrb_vformat() heap overflow could lead to code execution](192318-mrb-vformat-heap-overflow-could-lead-to-code-execution.md) |
| 197723 | Uncontrolled Resource Consumption | low | $0 | [Null pointer dereference in mrb_str_modify](197723-null-pointer-dereference-in-mrb-str-modify.md) |
| 227762 | Heap Overflow | high | $0 | [Heap Overflow in fiber_switch triggered from Fiber.transfer](227762-heap-overflow-in-fiber-switch-triggered-from-fiber-transfer.md) |
| 226200 | Write-what-where Condition | critical | $0 | [OP_SCALL in LHS of a OP_ASGN resulting in arbitrary memory write](226200-op-scall-in-lhs-of-a-op-asgn-resulting-in-arbitrary-memory-w.md) |
| 216615 | Crash in ary_concat()  | n/a | $0 | [Crash in ary_concat() ](216615-crash-in-ary-concat.md) |
| 221251 | Heap Overflow | high | $0 | [heap-buffer-overflow (read outside of buffer) in mrb_vm_exec()](221251-heap-buffer-overflow-read-outside-of-buffer-in-mrb-vm-exec.md) |
| 219870 | Stack Overflow | high | $0 | [mirb only: stack-buffer-overflow (OOB write) in main()](219870-mirb-only-stack-buffer-overflow-oob-write-in-main.md) |
| 212456 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV - kh_get_n2s - in /src/symbol.c:37](212456-sigsegv-kh-get-n2s-in-src-symbol-c-37.md) |
| 206109 | Memory Corruption - Generic | n/a | $0 | [mruby heap use-after-free ](206109-mruby-heap-use-after-free.md) |
| 203595 | Memory Corruption - Generic | n/a | $0 | [forgot to add the patch](203595-forgot-to-add-the-patch.md) |
| 195842 | Uncontrolled Resource Consumption | high | $0 | [Segmentation fault - mrb_gc_mark](195842-segmentation-fault-mrb-gc-mark.md) |
| 193075 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV - mrb_check_intern_str() - NullPointer](193075-sigsegv-mrb-check-intern-str-nullpointer.md) |
| 192485 | Uncontrolled Resource Consumption | low | $0 | [SIGSEGV on mrb_vm_exec() Null Deref](192485-sigsegv-on-mrb-vm-exec-null-deref.md) |
| 192532 | Uncontrolled Resource Consumption | n/a | $0 | [SIGABRT, SIGSEGV mspace_free() and mrb_default_allocf()](192532-sigabrt-sigsegv-mspace-free-and-mrb-default-allocf.md) |
| 202582 | Uncontrolled Resource Consumption | medium | $0 | [Denial of service (segfault) due to null pointer dereference in mrb_obj_instance_eval](202582-denial-of-service-segfault-due-to-null-pointer-dereference-i.md) |
| 183667 | Uncontrolled Resource Consumption | n/a | $0 | [Null pointer dereference in ary_concat](183667-null-pointer-dereference-in-ary-concat.md) |
| 209765 | Memory Corruption - Generic | medium | $0 | [Heap buffer overflow in mruby value_move](209765-heap-buffer-overflow-in-mruby-value-move.md) |
| 207710 | Memory Corruption - Generic | n/a | $0 | [Heap use-after-free in mrb_vm_exec ](207710-heap-use-after-free-in-mrb-vm-exec.md) |
| 202584 | Uncontrolled Resource Consumption | medium | $0 | [Denial of service (segfault) due to null pointer dereference in mrb_vm_exec](202584-denial-of-service-segfault-due-to-null-pointer-dereference-i.md) |
| 183696 | Uncontrolled Resource Consumption | n/a | $0 | [Invalid memory access while freeing memory, caused by invalid type passed to mrb_ary_unshift](183696-invalid-memory-access-while-freeing-memory-caused-by-invalid.md) |
| 185705 | Uncontrolled Resource Consumption | n/a | $0 | [Null pointer dereference in mrb_str_concat](185705-null-pointer-dereference-in-mrb-str-concat.md) |
| 187539 | Uncontrolled Resource Consumption | n/a | $0 | [Null pointer dereference due to bug in codegen with negation of floats](187539-null-pointer-dereference-due-to-bug-in-codegen-with-negation.md) |
| 189704 | Uncontrolled Resource Consumption | n/a | $0 | [Segmentation fault due to invalid memory access in codegen when using break with the 127th argument a constant](189704-segmentation-fault-due-to-invalid-memory-access-in-codegen-w.md) |
