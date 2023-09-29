
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2023-09-29, 01:58:03
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

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECR 1]: nat: nat66 cli bug fix

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39151 <https:////gerrit.fd.io/r/c/vpp/+/39151>`_ [VECr 1]: build: test

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 6]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 3]: build: modify N_PREFETCH on Arm N2 to achieve best perf

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39583 <https:////gerrit.fd.io/r/c/vpp/+/39583>`_ [VECr 0]: dpdk: add Mellanox BlueField NICs
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 0]: interface dpdk: refactor RSS queues feature
  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VECr 2]: dpdk: fix description for mlx5_pci driver
  | `39581 <https:////gerrit.fd.io/r/c/vpp/+/39581>`_ [VECr 3]: dpdk: correct the printing of Rx offloading flags
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 6]: interface dpdk avf: introducing setting RSS hash key feature

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 0]: interface dpdk: refactor RSS queues feature

fib: **Neale Ranns** <neale@graphiant.com>
  | `39593 <https:////gerrit.fd.io/r/c/vpp/+/39593>`_ [VECr 0]: fib: only use interface address for glean
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 1]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 2]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 2]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 2]: fib: fix udp encap mp-safe ops and id validation
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 2]: fib: Crash when specify a big prefix length from CLI.
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 14]: fib: log an error when destroying non-empty tables
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 27]: ip: IP address family common input node

geneve: **community** vpp-dev@lists.fd.io
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 8]: geneve: support custom options in decap

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup

interface: **Dave Barach** <vpp@barachs.net>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 0]: interface dpdk: refactor RSS queues feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 6]: interface dpdk avf: introducing setting RSS hash key feature

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 9]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 2]: fib: Crash when specify a big prefix length from CLI.
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 27]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 27]: ip: IP address family common input node

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 21]: ipsec: allow receiving encrypted IP packets with TFC padding

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 6]: linux-cp: Add VRF synchronization
  | `39486 <https:////gerrit.fd.io/r/c/vpp/+/39486>`_ [VECr 23]: linux-cp: check if lcp_itf_pair exists before creating tap

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 6]: interface dpdk avf: introducing setting RSS hash key feature

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 2]: mpls: fix crashes on mpls tunnel create/delete

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39576 <https:////gerrit.fd.io/r/c/vpp/+/39576>`_ [VECr 4]: nat: add ipfix rate-limiter for nat44-ed, nat44-ei and nat64
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 22]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VECr 22]: nat: fix address resolution

session: **Florin Coras** <fcoras@cisco.com>
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VECr 8]: session: program rx events only if none are pending

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 1]: nat: fix nat44-ed address removal from fib
  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VECr 2]: tests: memif ethernet type interface tests
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 2]: mpls: fix crashes on mpls tunnel create/delete
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 2]: fib: fix udp encap mp-safe ops and id validation
  | `39576 <https:////gerrit.fd.io/r/c/vpp/+/39576>`_ [VECr 4]: nat: add ipfix rate-limiter for nat44-ed, nat44-ei and nat64
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 8]: geneve: support custom options in decap
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 9]: tests: fix issues found when enabling DMAC check
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 9]: ip-neighbor: add version 3 of neighbor event
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 21]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 22]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 27]: ip: IPv6 validate input packet's header length does not exist buffer size

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 2]: fib: fix udp encap mp-safe ops and id validation

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 6]: misc: patch to test CI infra changes

vnet: **Damjan Marion** <damarion@cisco.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 2]: fib: Crash when specify a big prefix length from CLI.

vpp: **Dave Barach** <vpp@barachs.net>
  | `39591 <https:////gerrit.fd.io/r/c/vpp/+/39591>`_ [VECr 0]: stats: added optional CLI arg "port" to specify non-default port

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 62]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 62]: api trace: the api trace info about barrier is opposite

**Alexander Chernavin** <achernavin@netgate.com>:

  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [vEC 6]: ethernet: run callbacks for subifs too when mac changes

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 56]: linux-cp: Fix update on IPv4 routes

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39150 <https:////gerrit.fd.io/r/c/vpp/+/39150>`_ [VEc 0]: build: add ability to disable some plugins from packaging and tests
  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 106]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 126]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 136]: TEST: remove the rdma mappings

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vEC 13]: ena: add tx checksum offloads and tso support
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 51]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 43]: ip6: ECMP hash support for ipv6 fragments

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 14]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 120]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 22]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 132]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 120]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 163]: dpdk: use adapter MTU in max_frame_size setting

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VEc 10]: ethernet: check dmacs_bad in the fastpath case

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `39507 <https:////gerrit.fd.io/r/c/vpp/+/39507>`_ [VEc 9]: cnat: add flow hash config to cnat translation

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 36]: sr: SRv6 Path Tracing source node behavior

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 63]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VeC 38]: ipsec: huge anti-replay window support

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [VEc 22]: geneve: add support for layer 3

**Neale Ranns** <neale@graphiant.com>:

  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [vEC 27]: ip: Set the buffer error in ip6-input

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 64]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 141]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 48]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 127]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 51]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 58]: interface: check sw_if_index more thoroughly
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 59]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 150]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 62]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 64]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 105]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 52]: libmemif: fix segfault and buffer overflow in examples

**Ting Xu** <ting.xu@intel.com>:

  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VeC 43]: dpdk: fix variable type in pattern parsing

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 45]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VEc 1]: ip: make running_fragment_id thread safe
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VEc 15]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 127]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 153]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 155]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 115]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 126]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 27]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 74]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 74]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEc 15]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 44]: dhcp: fix dhcp multiple client request

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VeC 52]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 90]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 98]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
authors          53
maintainers      32
committers       1
abandoned        0
================ ===

