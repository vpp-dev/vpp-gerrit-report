
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2024-03-13, 01:58:29
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


Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `40482 <https:////gerrit.fd.io/r/c/vpp/+/40482>`_ [VECr 4]: vnet: fix ARP for unnumbered

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 18]: build: Connect FreeBSD system files to build

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 5]: docs: Restore and update nat section of progressive tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 14]: dpdk: create and remove interface in runtime

dpdk-cryptodev: **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40476 <https:////gerrit.fd.io/r/c/vpp/+/40476>`_ [VECr 5]: dpdk-cryptodev: fix coverity issues

fateshare: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 0]: vppinfra: Add method for getting current executable name

fib: **Neale Ranns** <neale@graphiant.com>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40479 <https:////gerrit.fd.io/r/c/vpp/+/40479>`_ [VECr 5]: fib: fix vectorized impl buffer typo
  | `40464 <https:////gerrit.fd.io/r/c/vpp/+/40464>`_ [VECr 5]: fib: fix off-by-one error in rewrite length check
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 7]: fib: coverity 335348 out-of-bounds access
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 9]: fib: add ip4 fib preallocation support
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 10]: nat: fix nat44-ed address removal from fib
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 11]: fib: fix covered_inherit_add
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 21]: ip: add support for buffer offload metadata in ip midchain
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 27]: fib: log an error when destroying non-empty tables

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 8]: ikev2: handoff packets to main thread

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 26]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 1]: ip6: fix icmp error on check fail
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 8]: mpls: fix default mpls lb hash config
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VECr 10]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 21]: ip: add support for buffer offload metadata in ip midchain

ipip: **Ole Troan** <otroan@employees.org>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 21]: ip: add support for buffer offload metadata in ip midchain

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VECr 5]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 21]: ip: add support for buffer offload metadata in ip midchain

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 8]: vxlan: fix src port entropy with mpls payload

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `40465 <https:////gerrit.fd.io/r/c/vpp/+/40465>`_ [VECr 5]: lb: fix using vip after free

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VECr 18]: linux-cp: populate mapping vif-sw_if_index only for default-ns

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40442 <https:////gerrit.fd.io/r/c/vpp/+/40442>`_ [VECr 9]: api: fix rx timeout thread busy loop after reconnect
  | `40373 <https:////gerrit.fd.io/r/c/vpp/+/40373>`_ [VECr 13]: crypto-sw-scheduler: crypto-dispatch improvement

mpls: **Neale Ranns** <neale@graphiant.com>
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 8]: mpls: fix default mpls lb hash config

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 10]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VECr 10]: nat: stick nat44-ed to use configured outside-fib
  | `39989 <https:////gerrit.fd.io/r/c/vpp/+/39989>`_ [VECr 11]: nat: add saddr info to nat44-ed o2i flow's rewrite

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40504 <https:////gerrit.fd.io/r/c/vpp/+/40504>`_ [VECr 0]: papi: use correct size for fixed length strings

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 0]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

pnat: **Ole Troan** <ot@cisco.com>
  | `40385 <https:////gerrit.fd.io/r/c/vpp/+/40385>`_ [VECr 18]: nat: Include platform specific headers on FreeBSD

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 16]: session: make local port allocator fib aware

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 16]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VECr 0]: tests: skip more excpuded plugin tests
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40482 <https:////gerrit.fd.io/r/c/vpp/+/40482>`_ [VECr 4]: vnet: fix ARP for unnumbered
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VECr 8]: ikev2: handoff packets to main thread
  | `40448 <https:////gerrit.fd.io/r/c/vpp/+/40448>`_ [VECr 8]: vxlan: fix src port entropy with mpls payload
  | `40447 <https:////gerrit.fd.io/r/c/vpp/+/40447>`_ [VECr 8]: mpls: fix default mpls lb hash config
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 10]: nat: fix nat44-ed address removal from fib
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 20]: tests: Added a simple prom(etheus exporter) plugin test
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 20]: tests: Added SRv6 End.Am behaviour test
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 21]: ip: add support for buffer offload metadata in ip midchain

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `40405 <https:////gerrit.fd.io/r/c/vpp/+/40405>`_ [VECr 13]: tls: avoid app session preallocation

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 16]: session: make local port allocator fib aware

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 11]: fib: fix covered_inherit_add

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [VECr 0]: virtio: fix crash on show tun cli

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 0]: vppinfra: Add method for getting current executable name
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VECr 5]: vlib: add config for elog tracing
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 18]: build: Connect FreeBSD system files to build
  | `39992 <https:////gerrit.fd.io/r/c/vpp/+/39992>`_ [VECr 19]: vlib: fix counter_index check it need to check counter_index effectiveness with the commit 96158834db0, but it should be checked before addtion operation
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 23]: build: Link agaist FREEBSD_LIBS

vpp: **Dave Barach** <vpp@barachs.net>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 0]: vppinfra: Add method for getting current executable name
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 3]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 23]: build: Link agaist FREEBSD_LIBS

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 0]: vppinfra: Add method for getting current executable name
  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VECr 5]: vppinfra: Add platform cpu and domain get for FreeBSD
  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VECr 5]: vppinfra: fix mask compare and compress OOB reads
  | `40463 <https:////gerrit.fd.io/r/c/vpp/+/40463>`_ [VECr 6]: vppinfra: fix array_mask_u32 underrun
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VECr 18]: vppinfra: fix cpu freq init error if cpu support aperfmperf
  | `40392 <https:////gerrit.fd.io/r/c/vpp/+/40392>`_ [VECr 18]: vppinfra: Add platform cpu and domain bitmap get functions
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 18]: build: Connect FreeBSD system files to build

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VeC 57]: hs-test: added targets to makefiles to get coverage from HS tests

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [VEc 19]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 83]: ena: add tx checksum offloads and tso support

**Dan Geist** <dan@polter.net>:

  | `40491 <https:////gerrit.fd.io/r/c/vpp/+/40491>`_ [vEC 3]: Updates to initial commit based on code formatting guidelines
  | `40489 <https:////gerrit.fd.io/r/c/vpp/+/40489>`_ [vEC 4]: Updates to the MAP plugin, specifically to organization of MAP rules.

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 83]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [veC 43]: misc: patch to test CI infra changes
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 56]: tests: organize test coverage report generation

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 67]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 83]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 84]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 90]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 96]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 34]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 81]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Fan Zhang** <fanzhang.oss@gmail.com>:

  | `40505 <https:////gerrit.fd.io/r/c/vpp/+/40505>`_ [vEC 0]: ipsec: remove unused parameter for esp_add_footer_and_icv

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vec 53]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 133]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 122]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 122]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 85]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 103]: interface: move set rss queues function

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 159]: ip: fix crash in ip4_neighbor_advertise

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 10]: nat: add in2out-ip-fib-index config option
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 38]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 0]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 5]: api: fix path for api definition files in vpe.api

**Maxime Peim** <mpeim@cisco.com>:

  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [vEC 0]: urpf: allow per buffer fib
  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VEc 0]: urpf: export to use it externally
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 112]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 106]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 152]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [vEC 20]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [vEC 23]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 37]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 126]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 84]: geneve: support custom options in decap

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40467 <https:////gerrit.fd.io/r/c/vpp/+/40467>`_ [VEc 2]: vapi: uds transport support
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 36]: tap: add virtio polling option

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 159]: l2: fix crash while sending traffic out orphan BVI

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [vEC 6]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40469 <https:////gerrit.fd.io/r/c/vpp/+/40469>`_ [vEC 5]: vlib: Use platform specific method to get exec name
  | `40470 <https:////gerrit.fd.io/r/c/vpp/+/40470>`_ [vEC 5]: vpp: Add platform specific method to get exec name
  | `40473 <https:////gerrit.fd.io/r/c/vpp/+/40473>`_ [vEC 5]: vlib: Add a skeleton pci interface for FreeBSD
  | `40393 <https:////gerrit.fd.io/r/c/vpp/+/40393>`_ [VEc 12]: vlib: Add calls to retrieve cpu and domain bitmaps on FreeBSD
  | `40390 <https:////gerrit.fd.io/r/c/vpp/+/40390>`_ [vEc 18]: tlsopenssl: Use EBADF on FreeBSD
  | `40389 <https:////gerrit.fd.io/r/c/vpp/+/40389>`_ [VEc 18]: vcl: Only build vcl_ldpreload on Linux
  | `40341 <https:////gerrit.fd.io/r/c/vpp/+/40341>`_ [vEC 18]: vlib: Add FreeBSD thread specific header and calls
  | `40386 <https:////gerrit.fd.io/r/c/vpp/+/40386>`_ [vEC 18]: tracedump: Add platform specific header on FreeBSD
  | `40383 <https:////gerrit.fd.io/r/c/vpp/+/40383>`_ [vEC 18]: acl: Add FreeBSD specific include to build
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VeC 43]: vppinfra: Link against lib execinfo on FreeBSD

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40441 <https:////gerrit.fd.io/r/c/vpp/+/40441>`_ [VEc 7]: linux-cp: add support for tap num queues config
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VEc 7]: vppinfra: fix mhash oob after unset and add tests
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VEc 8]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 168]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 168]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 168]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 168]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 104]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 111]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 167]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 175]: ip-neighbor: add version 3 of neighbor event

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [veC 39]: build: use GNUInstallDirs where possible

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 172]: interface dpdk avf: introducing setting RSS hash key feature

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 49]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 129]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 139]: ping:mark ipv6 packets as locally originated

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 33]: virtio: RSS support

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
authors          68
maintainers      45
committers       0
abandoned        0
================ ===

