
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2023-12-12, 02:05:23
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

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `40084 <https:////gerrit.fd.io/r/c/vpp/+/40084>`_ [VECr 0]: bpf_trace_filter: allow use whithout classifier

build: **Damjan Marion** <damarion@cisco.com>
  | `39976 <https:////gerrit.fd.io/r/c/vpp/+/39976>`_ [VECr 11]: ipsec: Update host IPsec-mb lib

classify: **Dave Barach** <vpp@barachs.net>
  | `40084 <https:////gerrit.fd.io/r/c/vpp/+/40084>`_ [VECr 0]: bpf_trace_filter: allow use whithout classifier
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 3]: misc: move lawful-intercept to plugin

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `40046 <https:////gerrit.fd.io/r/c/vpp/+/40046>`_ [VECr 3]: wireguard: notify key changes to crypto engine

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `40047 <https:////gerrit.fd.io/r/c/vpp/+/40047>`_ [VECr 3]: crypto-openssl: refactor openssl API usage

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 11]: interface: move set rss queues function
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 24]: dpdk: create and remove interface in runtime
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 11]: interface: move set rss queues function
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40070 <https:////gerrit.fd.io/r/c/vpp/+/40070>`_ [VECr 5]: hs-test: retry command on test setup failure
  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [VECr 14]: http: fix client receiving large data

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [VECr 14]: http: fix client receiving large data
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 14]: http: unify client/server state machines

http: **Florin Coras** <fcoras@cisco.com>
  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [VECr 14]: http: fix client receiving large data
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 14]: http: unify client/server state machines

interface: **Dave Barach** <vpp@barachs.net>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 11]: interface: move set rss queues function
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 27]: interface: check sw_if_index more thoroughly
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VECr 4]: ip: mark ipX_header_t and ip4_address_t as packed

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 0]: ipsec: allow receiving encrypted IP packets with TFC padding

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 3]: misc: move lawful-intercept to plugin

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `40077 <https:////gerrit.fd.io/r/c/vpp/+/40077>`_ [VECr 3]: libmemif: fix for memif_init_queues slot math
  | `40065 <https:////gerrit.fd.io/r/c/vpp/+/40065>`_ [VECr 4]: libmemif: Fix for memif_buffer_alloc rewind logic

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 1]: linux-cp: Fix looping netlink messages
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VECr 3]: misc: move lawful-intercept to plugin
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VECr 20]: misc: tracedump specify cache size

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40086 <https:////gerrit.fd.io/r/c/vpp/+/40086>`_ [VECr 0]: urpf: add interface dump to API
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 0]: tests: Added SRv6 End.Am behaviour test
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 0]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 0]: tests: Added a simple prom(etheus exporter) plugin test
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VECr 4]: nat: fix det44 flaky test
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 30]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 30]: tests: fix issues found when enabling DMAC check

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 12]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40084 <https:////gerrit.fd.io/r/c/vpp/+/40084>`_ [VECr 0]: bpf_trace_filter: allow use whithout classifier

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VECr 19]: vppapigen: recognize also _event as to_network

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40089 <https:////gerrit.fd.io/r/c/vpp/+/40089>`_ [VECr 0]: vppinfra: fix bracket balance
  | `40087 <https:////gerrit.fd.io/r/c/vpp/+/40087>`_ [VECr 0]: vppinfra : fix alignment issue

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 96]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 136]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 136]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `40075 <https:////gerrit.fd.io/r/c/vpp/+/40075>`_ [VEc 0]: tests: Added bpf trace filter plugin test

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 130]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 87]: ena: add tx checksum offloads and tso support
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 125]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 47]: ip6: ECMP hash support for ipv6 fragments
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 47]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 71]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 96]: ebuild: adding libmemif to debian packages

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40026 <https:////gerrit.fd.io/r/c/vpp/+/40026>`_ [VEc 11]: hs-test: add tls proxy test

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 41]: session: program rx events only if none are pending

**Georgy Borodin** <bogdan10bg@yahoo.com>:

  | `39862 <https:////gerrit.fd.io/r/c/vpp/+/39862>`_ [VeC 31]: vppinfra: change fchmod to umask for unix socket

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 67]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 110]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 63]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 80]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 137]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 96]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39871 <https:////gerrit.fd.io/r/c/vpp/+/39871>`_ [vEC 4]: tests: preload api files

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [VEc 14]: geneve: add support for layer 3
  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [veC 40]: devices: add support to check host interface offload capabilities
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [veC 40]: devices: add cli support to enable disable qdisc bypass

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 60]: vlib: allow overlapping cli subcommands

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 76]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 34]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 101]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 101]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 82]: geneve: support custom options in decap

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 138]: ipsec: introduce function esp_prepare_packet_for_enc

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 125]: ip: flow hash ignore tcp/udp ports when fragmented

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 67]: l2: fix crash while sending traffic out orphan BVI
  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 136]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 138]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 179]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 71]: libmemif: fix segfault and buffer overflow in examples

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 119]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 69]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 76]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 76]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 76]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 76]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [vEC 12]: nat: speed-up nat44-ed outside address distribution
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 75]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 83]: ip-neighbor: add version 3 of neighbor event

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 80]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 101]: af_xdp: optimizing send performance

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 89]: vrrp: dump vrrp vr peer

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 37]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 47]: ping:mark ipv6 packets as locally originated

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 118]: dhcp: fix dhcp multiple client request

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
authors          52
maintainers      28
committers       0
abandoned        0
================ ===

