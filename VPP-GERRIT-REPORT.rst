
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2024-03-04, 02:09:41
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

  | `40408 <https:////gerrit.fd.io/r/c/vpp/+/40408>`_ [VECR 3]: octeon: add support for VF device

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `39993 <https:////gerrit.fd.io/r/c/vpp/+/39993>`_ [VECr 5]: af_packet: fix the device input feature arc support

bier: **Neale Ranns** <neale@graphiant.com>
  | `40449 <https:////gerrit.fd.io/r/c/vpp/+/40449>`_ [VECr 0]: fib: fix crash while adding intf-rx routes

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `40443 <https:////gerrit.fd.io/r/c/vpp/+/40443>`_ [VECr 0]: bpf_trace_filter: support bpf filter optimization and dump

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `40409 <https:////gerrit.fd.io/r/c/vpp/+/40409>`_ [VECr 3]: vppinfra: add os_get_online_cpu_core() and os_get_online_cpu_node()
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 9]: build: Connect FreeBSD system files to build

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 5]: docs: Restore and update nat section of progressive tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces
  | `40407 <https:////gerrit.fd.io/r/c/vpp/+/40407>`_ [VECr 4]: dpdk: correct waiting times
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 5]: dpdk: create and remove interface in runtime

fib: **Neale Ranns** <neale@graphiant.com>
  | `40449 <https:////gerrit.fd.io/r/c/vpp/+/40449>`_ [VECr 0]: fib: fix crash while adding intf-rx routes
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VECr 0]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 0]: fib: add ip4 fib preallocation support
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 1]: nat: fix nat44-ed address removal from fib
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 2]: fib: fix covered_inherit_add
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 11]: fib: coverity 335348 out-of-bounds access
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 12]: ip: add support for buffer offload metadata in ip midchain
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 18]: fib: log an error when destroying non-empty tables

flowprobe: **Ole Troan** <otroan@employees.org>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 5]: flowprobe: fix flush callbacks when multiple workers

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 4]: ikev2: handoff packets to main thread

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 17]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40449 <https:////gerrit.fd.io/r/c/vpp/+/40449>`_ [VECr 0]: fib: fix crash while adding intf-rx routes
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 0]: mpls: fix default mpls lb hash config
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VECr 0]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces
  | `40439 <https:////gerrit.fd.io/r/c/vpp/+/40439>`_ [VECr 0]: ip: fix warning on interface ipv6 prefix remove
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VECr 1]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `40294 <https:////gerrit.fd.io/r/c/vpp/+/40294>`_ [VECr 2]: ip: force full reassembly before virtual
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 12]: ip: add support for buffer offload metadata in ip midchain
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 20]: misc: fix icmp

ipip: **Ole Troan** <otroan@employees.org>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 12]: ip: add support for buffer offload metadata in ip midchain

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 12]: ip: add support for buffer offload metadata in ip midchain

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 0]: vxlan: fix src port entropy with mpls payload
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `40441 <https:////gerrit.fd.io/r/c/vpp/+/40441>`_ [VECr 0]: linux-cp: add support for tap num queues config
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VECr 9]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 29]: linux-cp: Add VRF synchronization

lisp: **Florin Coras** <fcoras@cisco.com>
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40437 <https:////gerrit.fd.io/r/c/vpp/+/40437>`_ [VECr 0]: vnet: fix format of deleted sw interfaces
  | `40442 <https:////gerrit.fd.io/r/c/vpp/+/40442>`_ [VECr 0]: api: fix rx timeout thread busy loop after reconnect
  | `40373 <https:////gerrit.fd.io/r/c/vpp/+/40373>`_ [VECr 4]: crypto-sw-scheduler: crypto-dispatch improvement

mpls: **Neale Ranns** <neale@graphiant.com>
  | `40449 <https:////gerrit.fd.io/r/c/vpp/+/40449>`_ [VECr 0]: fib: fix crash while adding intf-rx routes
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 0]: mpls: fix default mpls lb hash config

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 1]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VECr 1]: nat: stick nat44-ed to use configured outside-fib
  | `39989 <https:////gerrit.fd.io/r/c/vpp/+/39989>`_ [VECr 2]: nat: add saddr info to nat44-ed o2i flow's rewrite

perfmon: **Damjan Marion** <damarion@cisco.com>, **Ray Kinsella** <mdr@ashroe.eu>
  | `40409 <https:////gerrit.fd.io/r/c/vpp/+/40409>`_ [VECr 3]: vppinfra: add os_get_online_cpu_core() and os_get_online_cpu_node()

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 19]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

pnat: **Ole Troan** <ot@cisco.com>
  | `40385 <https:////gerrit.fd.io/r/c/vpp/+/40385>`_ [VECr 9]: nat: Include platform specific headers on FreeBSD

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 7]: session: make local port allocator fib aware

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 27]: tap: add virtio polling option

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 7]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 0]: vxlan: fix src port entropy with mpls payload
  | `40449 <https:////gerrit.fd.io/r/c/vpp/+/40449>`_ [VECr 0]: fib: fix crash while adding intf-rx routes
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 0]: mpls: fix default mpls lb hash config
  | `40443 <https:////gerrit.fd.io/r/c/vpp/+/40443>`_ [VECr 0]: bpf_trace_filter: support bpf filter optimization and dump
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 1]: nat: fix nat44-ed address removal from fib
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 4]: ikev2: handoff packets to main thread
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 5]: flowprobe: fix flush callbacks when multiple workers
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 11]: tests: Added a simple prom(etheus exporter) plugin test
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 11]: tests: Added SRv6 End.Am behaviour test
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 12]: ip: add support for buffer offload metadata in ip midchain
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 20]: misc: fix icmp

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `40405 <https:////gerrit.fd.io/r/c/vpp/+/40405>`_ [VECr 4]: tls: avoid app session preallocation

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 7]: session: make local port allocator fib aware

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 2]: fib: fix covered_inherit_add

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VECr 24]: virtio: RSS support
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 27]: tap: add virtio polling option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40445 <https:////gerrit.fd.io/r/c/vpp/+/40445>`_ [VECr 0]: vlib: fix initial stats time for the process nodes
  | `40409 <https:////gerrit.fd.io/r/c/vpp/+/40409>`_ [VECr 3]: vppinfra: add os_get_online_cpu_core() and os_get_online_cpu_node()
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 9]: build: Connect FreeBSD system files to build
  | `39992 <https:////gerrit.fd.io/r/c/vpp/+/39992>`_ [VECr 10]: vlib: fix counter_index check it need to check counter_index effectiveness with the commit 96158834db0, but it should be checked before addtion operation
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 14]: build: Link agaist FREEBSD_LIBS

vpp: **Dave Barach** <vpp@barachs.net>
  | `40446 <https:////gerrit.fd.io/r/c/vpp/+/40446>`_ [VECr 0]: vpp: fix stdin vs non-interactive command clash
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 14]: build: Link agaist FREEBSD_LIBS

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VECr 0]: vppinfra: fix mhash oob after unset and add tests
  | `40409 <https:////gerrit.fd.io/r/c/vpp/+/40409>`_ [VECr 3]: vppinfra: add os_get_online_cpu_core() and os_get_online_cpu_node()
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VECr 9]: vppinfra: fix cpu freq init error if cpu support aperfmperf
  | `40392 <https:////gerrit.fd.io/r/c/vpp/+/40392>`_ [VECr 9]: vppinfra: Add platform cpu and domain bitmap get functions
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 9]: build: Connect FreeBSD system files to build
  | `40380 <https:////gerrit.fd.io/r/c/vpp/+/40380>`_ [VECr 9]: vppinfra: Add a platform specific system functions for FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 179]: nat: nat44-ed get out2in workers failed for static mapping without port

**Adrian Villin** <avillin@cisco.com>:

  | `39988 <https:////gerrit.fd.io/r/c/vpp/+/39988>`_ [VEc 3]: hs-test: experimental support for multiple test instances
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VeC 48]: hs-test: added targets to makefiles to get coverage from HS tests

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [VEc 10]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 74]: ena: add tx checksum offloads and tso support

**Damjan Marion** <dmarion@0xa5.net>:

  | `40450 <https:////gerrit.fd.io/r/c/vpp/+/40450>`_ [vEC 0]: vppinfra: SHA2-256 ARM ISA support

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 74]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [veC 34]: misc: patch to test CI infra changes
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 47]: tests: organize test coverage report generation

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [Vec 34]: vppinfra: fix mask compare and compress OOB reads
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 58]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 74]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 75]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 81]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 87]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [VEc 25]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 72]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vec 44]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 124]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 113]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 113]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 76]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 94]: interface: move set rss queues function

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VeC 59]: vlib: improve core pinning
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VeC 81]: misc: move lawful-intercept to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 150]: ip: fix crash in ip4_neighbor_advertise

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 1]: nat: add in2out-ip-fib-index config option

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 179]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 103]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 97]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 143]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [vEC 11]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [vEC 14]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 28]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 117]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 75]: geneve: support custom options in decap

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 150]: l2: fix crash while sending traffic out orphan BVI

**Tom Jones** <thj@freebsd.org>:

  | `40393 <https:////gerrit.fd.io/r/c/vpp/+/40393>`_ [VEc 3]: vlib: Add calls to retrieve cpu and domain bitmaps on FreeBSD
  | `40390 <https:////gerrit.fd.io/r/c/vpp/+/40390>`_ [vEc 9]: tlsopenssl: Use EBADF on FreeBSD
  | `40389 <https:////gerrit.fd.io/r/c/vpp/+/40389>`_ [VEc 9]: vcl: Only build vcl_ldpreload on Linux
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [vEC 9]: vlib: Add vlib method for getting the current executable name
  | `40341 <https:////gerrit.fd.io/r/c/vpp/+/40341>`_ [vEC 9]: vlib: Add FreeBSD thread specific header and calls
  | `40386 <https:////gerrit.fd.io/r/c/vpp/+/40386>`_ [vEC 9]: tracedump: Add platform specific header on FreeBSD
  | `40383 <https:////gerrit.fd.io/r/c/vpp/+/40383>`_ [vEC 9]: acl: Add FreeBSD specific include to build
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VeC 34]: vppinfra: Link against lib execinfo on FreeBSD

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 159]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 159]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 159]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 159]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 95]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 102]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 158]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 166]: ip-neighbor: add version 3 of neighbor event

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [vEC 30]: build: use GNUInstallDirs where possible

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 163]: interface dpdk avf: introducing setting RSS hash key feature

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 172]: vrrp: dump vrrp vr peer

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 40]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 120]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 130]: ping:mark ipv6 packets as locally originated

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 10]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
maintainers      48
committers       1
abandoned        0
================ ===

