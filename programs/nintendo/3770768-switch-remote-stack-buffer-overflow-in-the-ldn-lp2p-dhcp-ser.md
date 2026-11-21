# [Switch] Remote stack buffer overflow in the LDN/LP2P DHCP server leads to control-flow hijack

- Program: Nintendo
- Weakness / temuan: **Stack Overflow**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 35
- Submitted: 2026-05-30
- Disclosed: 2026-10-15
- Report: https://hackerone.com/reports/3770768
- CVE: CVE-2026-82079

## Team summary

# Description
A stack-based buffer overflow vulnerability in the Nintendo Switch local wireless networking functionality may allow an attacker within wireless range to execute arbitrary code using return-oriented programming (ROP) through crafted network traffic.

## Researcher summary

The `ldn` system module runs a DHCP server while the console hosts a local-wireless **lp2p/LDN** session (for example, photo sharing or local session in Mario Kart Live: Home Circuit). On receiving a frame, it reassembles received data into a fixed stack buffer with `memmove(dst, src, total_size)` and **never checks `total_size` against the buffer size**. `src` is the global BPF capture buffer holding the frame exactly as it arrived; `total_size` is the sum of the parsed layer lengths, and the DHCP-layer length is attacker-controlled - so a single oversized DHCP frame from a Wi-Fi peer overflows the stack, overwriting the **saved return address and callee-saved registers**. On Switch, the function returns to an attacker-chosen address. Overwriting only the low 2 bytes of the saved LR redirects PC within a 64 KB window of the module's own code without knowing the ASLR base.
