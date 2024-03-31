#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Sunday 2024-03-31, 02:01:17
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Committers:
-----------
| **These gerrit changes have been**

    - Verified
    - Not expired
    - Comments resolved
    - Approved by Maintainers

| **Please perform a final review & submit.**

  | `40618 <https:////gerrit.fd.io/r/c/vpp/+/40618>`_ [VECR 1]: octeon: refill even if nothing dequeued from rx queue
  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [VECR 3]: octeon: add support for vnet generic flow type
  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VECR 5]: tests: skip more excpuded plugin tests
  | `40559 <https:////gerrit.fd.io/r/c/vpp/+/40559>`_ [VECR 9]: tests: Add missing socket imports in tests

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40383 <https:////gerrit.fd.io/r/c/vpp/+/40383>`_ [VECr 4]: acl: Add FreeBSD specific include to build

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `40482 <https:////gerrit.fd.io/r/c/vpp/+/40482>`_ [VECr 0]: vnet: fix ARP for unnumbered

build: **Damjan Marion** <damarion@cisco.com>
  | `40608 <https:////gerrit.fd.io/r/c/vpp/+/40608>`_ [VECr 4]: build: Error out Makefile if bash can't be found
  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VECr 17]: octeon: add support for Marvell Octeon9 SoC

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 17]: docs: Restore and update nat section of progressive tutorial
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

fateshare: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40611 <https:////gerrit.fd.io/r/c/vpp/+/40611>`_ [VECr 4]: fateshare: Add FreeBSD specific API for controlling processes
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 18]: vppinfra: Add method for getting current executable name

fib: **Neale Ranns** <neale@graphiant.com>
  | `40605 <https:////gerrit.fd.io/r/c/vpp/+/40605>`_ [VECr 3]: fib: add early config support for IP and IP6 default FIB table names
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 9]: fib: coverity 335348 out-of-bounds access
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40464 <https:////gerrit.fd.io/r/c/vpp/+/40464>`_ [VECr 23]: fib: fix off-by-one error in rewrite length check
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 27]: fib: add ip4 fib preallocation support
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 28]: nat: fix nat44-ed address removal from fib
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 29]: fib: fix covered_inherit_add

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40517 <https:////gerrit.fd.io/r/c/vpp/+/40517>`_ [VECr 10]: hs-test: transition to ginkgo test framework

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 15]: ikev2: handoff packets to main thread

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 0]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 19]: ip6: fix icmp error on check fail
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 26]: mpls: fix default mpls lb hash config
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VECr 28]: ip: mark IP_ADDRESS_DUMP as mp-safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VECr 23]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 0]: l2: fix vxlan src port entropy with mpls payload

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `40465 <https:////gerrit.fd.io/r/c/vpp/+/40465>`_ [VECr 23]: lb: fix using vip after free

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `40441 <https:////gerrit.fd.io/r/c/vpp/+/40441>`_ [VECr 0]: linux-cp: add support for tap num queues config

map: **Ole Troan** <ot@cisco.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40515 <https:////gerrit.fd.io/r/c/vpp/+/40515>`_ [VECr 17]: map: BR rule lookup update

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40373 <https:////gerrit.fd.io/r/c/vpp/+/40373>`_ [VECr 17]: crypto-sw-scheduler: crypto-dispatch improvement
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 17]: urpf: allow per buffer fib
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40442 <https:////gerrit.fd.io/r/c/vpp/+/40442>`_ [VECr 27]: api: fix rx timeout thread busy loop after reconnect

mpls: **Neale Ranns** <neale@graphiant.com>
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 26]: mpls: fix default mpls lb hash config

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 28]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VECr 28]: nat: stick nat44-ed to use configured outside-fib
  | `39989 <https:////gerrit.fd.io/r/c/vpp/+/39989>`_ [VECr 29]: nat: add saddr info to nat44-ed o2i flow's rewrite

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40625 <https:////gerrit.fd.io/r/c/vpp/+/40625>`_ [VECr 0]: octeon: fix buffer free on full tx ring
  | `40619 <https:////gerrit.fd.io/r/c/vpp/+/40619>`_ [VECr 1]: octeon: specify pool when alloc buffers
  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VECr 5]: octeon: add crypto framework
  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VECr 17]: octeon: add support for Marvell Octeon9 SoC

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VECr 1]: papi: more detailed packing error message

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 17]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 0]: l2: fix vxlan src port entropy with mpls payload
  | `40482 <https:////gerrit.fd.io/r/c/vpp/+/40482>`_ [VECr 0]: vnet: fix ARP for unnumbered
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 3]: tests: Added SRv6 End.Am behaviour test
  | `40610 <https:////gerrit.fd.io/r/c/vpp/+/40610>`_ [VECr 4]: tests: Use gnu sed explicitly in test setup/tear down
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 5]: tests: Added a simple prom(etheus exporter) plugin test
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 12]: vlib: allow overlapping cli subcommands
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 15]: ikev2: handoff packets to main thread
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 26]: mpls: fix default mpls lb hash config
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 28]: nat: fix nat44-ed address removal from fib

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 29]: fib: fix covered_inherit_add

urpf: **Neale Ranns** <neale@graphiant.com>
  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VECr 17]: urpf: export to use it externally
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 17]: urpf: allow per buffer fib

vapi: **Ole Troan** <ot@cisco.com>
  | `40604 <https:////gerrit.fd.io/r/c/vpp/+/40604>`_ [VECr 4]: vapi: avoid memory leak
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VECr 11]: vapi: don't store dict in length field

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 0]: misc: patch to test CI infra changes

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `40576 <https:////gerrit.fd.io/r/c/vpp/+/40576>`_ [VECr 10]: virtio: Add RX queue full statisitics

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VECr 5]: vlib: add config for elog tracing
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 12]: vlib: allow overlapping cli subcommands
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 18]: vppinfra: Add method for getting current executable name

vpp: **Dave Barach** <vpp@barachs.net>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 18]: vppinfra: Add method for getting current executable name
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 21]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

vppapigen: **Ole Troan** <otroan@employees.org>
  | `40540 <https:////gerrit.fd.io/r/c/vpp/+/40540>`_ [VECr 15]: misc: in crcchecker.py, don't check for uncommitted changes in CI

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40392 <https:////gerrit.fd.io/r/c/vpp/+/40392>`_ [VECr 4]: vppinfra: Add platform cpu and domain bitmap get functions
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VECr 4]: vppinfra: Link against lib execinfo on FreeBSD
  | `40463 <https:////gerrit.fd.io/r/c/vpp/+/40463>`_ [VECr 9]: vppinfra: fix array_mask_u32 underrun
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 17]: vppinfra: fix memory overrun in mhash_set_mem
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 18]: vppinfra: Add method for getting current executable name
  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VECr 23]: vppinfra: Add platform cpu and domain get for FreeBSD
  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VECr 23]: vppinfra: fix mask compare and compress OOB reads

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VeC 75]: hs-test: added targets to makefiles to get coverage from HS tests

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 37]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 101]: ena: add tx checksum offloads and tso support

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 45]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 101]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 74]: tests: organize test coverage report generation

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40570 <https:////gerrit.fd.io/r/c/vpp/+/40570>`_ [VEc 2]: ikev2: uptime

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 85]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 101]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 102]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 108]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 114]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 52]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 99]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vec 71]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 34]: session: make local port allocator fib aware
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 151]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 140]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 140]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 103]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 121]: interface: move set rss queues function

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [VEc 17]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [VEc 2]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VEc 9]: ip: fix crash in ip4_neighbor_advertise

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VEc 4]: linux-cp: Add VRF synchronization
  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 28]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 10]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 17]: api: fix path for api definition files in vpe.api

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 8]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.

**Maxime Peim** <mpeim@cisco.com>:

  | `40601 <https:////gerrit.fd.io/r/c/vpp/+/40601>`_ [VEc 7]: tests: allow to add paths to default route
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 130]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 124]: geneve: add support for layer 3

**Neale Ranns** <neale@graphiant.com>:

  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 38]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 41]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 55]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 144]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 102]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [VEc 9]: ping: Allow to specify a source interface in ping binary API

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 36]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 54]: tap: add virtio polling option

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 177]: l2: fix crash while sending traffic out orphan BVI

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [vEC 24]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40612 <https:////gerrit.fd.io/r/c/vpp/+/40612>`_ [VEc 3]: vhost: Only enable plugin on Linux
  | `40341 <https:////gerrit.fd.io/r/c/vpp/+/40341>`_ [vEC 4]: vlib: Add FreeBSD thread specific header and calls
  | `40473 <https:////gerrit.fd.io/r/c/vpp/+/40473>`_ [vEC 4]: vlib: Add a skeleton pci interface for FreeBSD
  | `40469 <https:////gerrit.fd.io/r/c/vpp/+/40469>`_ [vEC 23]: vlib: Use platform specific method to get exec name
  | `40470 <https:////gerrit.fd.io/r/c/vpp/+/40470>`_ [vEC 23]: vpp: Add platform specific method to get exec name
  | `40393 <https:////gerrit.fd.io/r/c/vpp/+/40393>`_ [VEc 30]: vlib: Add calls to retrieve cpu and domain bitmaps on FreeBSD
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VeC 36]: build: Connect FreeBSD system files to build
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VeC 41]: build: Link agaist FREEBSD_LIBS

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VEc 25]: vppinfra: fix mhash oob after unset and add tests
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VEc 26]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 122]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 129]: vppapigen: recognize also _event as to_network

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [veC 57]: build: use GNUInstallDirs where possible

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 36]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `39992 <https:////gerrit.fd.io/r/c/vpp/+/39992>`_ [VEc 9]: vlib: fix counter_index check it need to check counter_index effectiveness with the commit 96158834db0, but it should be checked before addtion operation

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [vEC 8]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 157]: ping:mark ipv6 packets as locally originated

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 51]: virtio: RSS support

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          60
maintainers      52
committers       4
abandoned        0
================ ===

