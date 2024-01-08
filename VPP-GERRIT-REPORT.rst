
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2024-01-08, 02:04:56
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

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `40119 <https:////gerrit.fd.io/r/c/vpp/+/40119>`_ [VECr 19]: af_packet: set next0 for AF_PACKET_IF_MODE_ETHERNET mode

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 20]: interface dpdk avf: introducing setting RSS hash key feature

classify: **Dave Barach** <vpp@barachs.net>
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 25]: misc: move lawful-intercept to plugin

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `40046 <https:////gerrit.fd.io/r/c/vpp/+/40046>`_ [VECr 30]: wireguard: notify key changes to crypto engine

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `40047 <https:////gerrit.fd.io/r/c/vpp/+/40047>`_ [VECr 30]: crypto-openssl: refactor openssl API usage

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VECr 3]: vlib: improve core pinning

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 20]: interface dpdk avf: introducing setting RSS hash key feature

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 20]: interface dpdk avf: introducing setting RSS hash key feature

fib: **Neale Ranns** <neale@graphiant.com>
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VECr 18]: fib: fix ip drop path crashes

flowprobe: **Ole Troan** <otroan@employees.org>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 10]: flowprobe: fix flush callbacks when multiple workers

geneve: **community** vpp-dev@lists.fd.io
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 19]: geneve: support custom options in decap

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40026 <https:////gerrit.fd.io/r/c/vpp/+/40026>`_ [VECr 16]: hs-test: add tls proxy test

interface: **Dave Barach** <vpp@barachs.net>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 20]: interface dpdk avf: introducing setting RSS hash key feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VECr 25]: ip: mark ipX_header_t and ip4_address_t as packed

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 25]: misc: move lawful-intercept to plugin

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `40065 <https:////gerrit.fd.io/r/c/vpp/+/40065>`_ [VECr 17]: libmemif: Fix for memif_buffer_alloc rewind logic
  | `40077 <https:////gerrit.fd.io/r/c/vpp/+/40077>`_ [VECr 17]: libmemif: fix for memif_init_queues slot math
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 17]: libmemif: added tests
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 18]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 0]: linux-cp: Fix looping netlink messages
  | `40142 <https:////gerrit.fd.io/r/c/vpp/+/40142>`_ [VECr 11]: linux-cp: fix default ipv6 route addition

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 20]: interface dpdk avf: introducing setting RSS hash key feature
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 25]: misc: move lawful-intercept to plugin

session: **Florin Coras** <fcoras@cisco.com>
  | `40096 <https:////gerrit.fd.io/r/c/vpp/+/40096>`_ [VECr 1]: session: avoid spurious closed notifications
  | `40091 <https:////gerrit.fd.io/r/c/vpp/+/40091>`_ [VECr 5]: session: support for cl port reuse

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40086 <https:////gerrit.fd.io/r/c/vpp/+/40086>`_ [VECr 0]: urpf: add interface dump to API
  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VECr 3]: vlib: improve core pinning
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 10]: flowprobe: fix flush callbacks when multiple workers
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VECr 18]: fib: fix ip drop path crashes
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 19]: geneve: support custom options in decap
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 27]: tests: Added SRv6 End.Am behaviour test
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 27]: tests: Added a simple prom(etheus exporter) plugin test

udp: **Florin Coras** <fcoras@cisco.com>
  | `40091 <https:////gerrit.fd.io/r/c/vpp/+/40091>`_ [VECr 5]: session: support for cl port reuse

urpf: **Neale Ranns** <neale@graphiant.com>
  | `40086 <https:////gerrit.fd.io/r/c/vpp/+/40086>`_ [VECr 0]: urpf: add interface dump to API

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 25]: misc: patch to test CI infra changes

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VECr 24]: virtio: RSS support

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VECr 3]: vlib: improve core pinning

vpp: **Dave Barach** <vpp@barachs.net>
  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VECr 3]: vlib: improve core pinning

vppapigen: **Ole Troan** <otroan@employees.org>
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VECr 19]: vppapigen: fix enum format function

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40152 <https:////gerrit.fd.io/r/c/vpp/+/40152>`_ [VECr 2]: vppinfra: fix memcpy test buffer size
  | `40151 <https:////gerrit.fd.io/r/c/vpp/+/40151>`_ [VECr 2]: vppinfra: fix clib_array_mask_u32 OOB reads
  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VECr 2]: vppinfra: fix mask compare and compress OOB reads
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VECr 2]: vppinfra: fix test_vec invalid checks
  | `40147 <https:////gerrit.fd.io/r/c/vpp/+/40147>`_ [VECr 2]: vppinfra: fix test_bihash
  | `40148 <https:////gerrit.fd.io/r/c/vpp/+/40148>`_ [VECr 2]: vppinfra: fix vec_prepend use-after-free
  | `40089 <https:////gerrit.fd.io/r/c/vpp/+/40089>`_ [VECr 27]: vppinfra: fix bracket balance

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 123]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 163]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 163]: api trace: the api trace info about barrier is opposite

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 157]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vEc 18]: ena: add tx checksum offloads and tso support
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 152]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 74]: ip6: ECMP hash support for ipv6 fragments
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 74]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 18]: ebuild: adding libmemif to debian packages

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 31]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vEc 16]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [VEc 5]: http: fix client receiving large data
  | `40070 <https:////gerrit.fd.io/r/c/vpp/+/40070>`_ [VeC 32]: hs-test: retry command on test setup failure

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 68]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 57]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 57]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 38]: interface: move set rss queues function

**Georgy Borodin** <bogdan10bg@yahoo.com>:

  | `39862 <https:////gerrit.fd.io/r/c/vpp/+/39862>`_ [VeC 58]: vppinfra: change fchmod to umask for unix socket

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 94]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 137]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 90]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 107]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 164]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 123]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39871 <https:////gerrit.fd.io/r/c/vpp/+/39871>`_ [vEC 15]: tests: preload api files
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 47]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [vEC 23]: devices: add support to check host interface offload capabilities
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 41]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 87]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 61]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 128]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 128]: ip: Set the buffer error in ip6-input

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 165]: ipsec: introduce function esp_prepare_packet_for_enc

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 51]: dpdk: create and remove interface in runtime
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 54]: interface: check sw_if_index more thoroughly
  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 152]: ip: flow hash ignore tcp/udp ports when fragmented

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 94]: l2: fix crash while sending traffic out orphan BVI
  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 163]: api: ip - set punt reason max length to fix VAPI generation

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 146]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 96]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 103]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 103]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 103]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 103]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 39]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 46]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 102]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 110]: ip-neighbor: add version 3 of neighbor event

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 107]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 128]: af_xdp: optimizing send performance

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 116]: vrrp: dump vrrp vr peer

**ranjan raj** <ranjanx.raj@intel.com>:

  | `39976 <https:////gerrit.fd.io/r/c/vpp/+/39976>`_ [VEc 2]: crypto: align host and VPP IPsec-mb lib

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 64]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 74]: ping:mark ipv6 packets as locally originated

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 145]: dhcp: fix dhcp multiple client request

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
authors          55
maintainers      32
committers       0
abandoned        0
================ ===

