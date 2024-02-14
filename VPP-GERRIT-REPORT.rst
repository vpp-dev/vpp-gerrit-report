
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2024-02-14, 01:56:46
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

build: **Damjan Marion** <damarion@cisco.com>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 29]: hs-test: added targets to makefiles to get coverage from HS tests

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `40046 <https:////gerrit.fd.io/r/c/vpp/+/40046>`_ [VECr 7]: wireguard: notify key changes to crypto engine

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `40047 <https:////gerrit.fd.io/r/c/vpp/+/40047>`_ [VECr 7]: crypto-openssl: refactor openssl API usage

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 1]: dpdk: create and remove interface in runtime

fib: **Neale Ranns** <neale@graphiant.com>
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 13]: fib: coverity 335348 out-of-bounds access

flowprobe: **Ole Troan** <otroan@employees.org>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 0]: flowprobe: fix flush callbacks when multiple workers

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39988 <https:////gerrit.fd.io/r/c/vpp/+/39988>`_ [VECr 0]: hs-test: experimental support for multiple test instances
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 29]: hs-test: added targets to makefiles to get coverage from HS tests

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 1]: misc: fix icmp
  | `40294 <https:////gerrit.fd.io/r/c/vpp/+/40294>`_ [VECr 6]: ip: force full reassembly before virtual

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 10]: linux-cp: Add VRF synchronization

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40322 <https:////gerrit.fd.io/r/c/vpp/+/40322>`_ [VECr 1]: build: add fib configuring option

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 0]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 6]: session: make local port allocator fib aware

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 8]: tap: add virtio polling option

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 6]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 0]: flowprobe: fix flush callbacks when multiple workers
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 1]: misc: fix icmp
  | `40283 <https:////gerrit.fd.io/r/c/vpp/+/40283>`_ [VECr 6]: tests: refactor virtual interface tests
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VECr 28]: tests: organize test coverage report generation
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 29]: hs-test: added targets to makefiles to get coverage from HS tests

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `40333 <https:////gerrit.fd.io/r/c/vpp/+/40333>`_ [VECr 0]: tls: mark ho done atomically after ctx init

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 6]: session: make local port allocator fib aware
  | `40320 <https:////gerrit.fd.io/r/c/vpp/+/40320>`_ [VECr 6]: udp: unregister ports on all cleanups

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VECr 5]: virtio: RSS support
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 8]: tap: add virtio polling option

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VECr 15]: vppinfra: Link against lib execinfo on FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 160]: nat: nat44-ed get out2in workers failed for static mapping without port

**Adrian Villin** <avillin@cisco.com>:

  | `39987 <https:////gerrit.fd.io/r/c/vpp/+/39987>`_ [VEc 0]: hs-test: shortened interface names to avoid character limit
  | `39986 <https:////gerrit.fd.io/r/c/vpp/+/39986>`_ [VEc 0]: hs-test: improved readability of some error messages, printing container logs to stdout
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VeC 64]: tests: Added SRv6 End.Am behaviour test
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VeC 64]: tests: Added a simple prom(etheus exporter) plugin test

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 15]: ip: add support for buffer offload metadata in ip midchain
  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 55]: ena: add tx checksum offloads and tso support

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 32]: fib: log an error when destroying non-empty tables
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 32]: ip6: ECMP hash support for ipv6 fragments

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 55]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [vEC 15]: misc: patch to test CI infra changes

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40332 <https:////gerrit.fd.io/r/c/vpp/+/40332>`_ [vEC 0]: tracedump: Fixed trace dump API result issue.
  | `40257 <https:////gerrit.fd.io/r/c/vpp/+/40257>`_ [vEC 0]: ikev2: dump state and profile name in CLI and API

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VEc 15]: vppinfra: fix mask compare and compress OOB reads
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 39]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 55]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 56]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 62]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 68]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [VEc 6]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 53]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vEc 25]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 105]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 94]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 94]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 57]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 75]: interface: move set rss queues function

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VeC 40]: vlib: improve core pinning
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VeC 62]: misc: move lawful-intercept to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 131]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 174]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 127]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 0]: nat: add in2out-ip-fib-index config option

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 160]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 84]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 78]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 124]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 9]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 98]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 165]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 165]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 56]: geneve: support custom options in decap

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 91]: interface: check sw_if_index more thoroughly

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 131]: l2: fix crash while sending traffic out orphan BVI

**Tom Jones** <thj@freebsd.org>:

  | `40248 <https:////gerrit.fd.io/r/c/vpp/+/40248>`_ [VEc 0]: build: Add FreeBSD as a supported platform for cmake
  | `40262 <https:////gerrit.fd.io/r/c/vpp/+/40262>`_ [VEc 0]: vppinfra: Stub out get_current_cpu and get_current_numa on FreeBSD
  | `40271 <https:////gerrit.fd.io/r/c/vpp/+/40271>`_ [VEc 0]: vppinfra: Provide FreeBSD implementation of clib_mem functions
  | `40252 <https:////gerrit.fd.io/r/c/vpp/+/40252>`_ [VEc 0]: vlib: Use platform specific headers for sched.h

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 133]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 140]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 140]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 140]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 140]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 76]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 83]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 139]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 147]: ip-neighbor: add version 3 of neighbor event

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [vEC 11]: build: use GNUInstallDirs where possible

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 144]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 165]: af_xdp: optimizing send performance

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 153]: vrrp: dump vrrp vr peer

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [vEC 21]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 101]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 111]: ping:mark ipv6 packets as locally originated

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [Vec 32]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
authors          65
maintainers      20
committers       0
abandoned        0
================ ===

