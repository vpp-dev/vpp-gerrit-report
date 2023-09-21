
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2023-09-21, 01:56:55
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

avf: **Damjan Marion** <damarion@cisco.com>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 29]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `39539 <https:////gerrit.fd.io/r/c/vpp/+/39539>`_ [VECr 0]: fib: Don't use an address from an attached prefix when sending ARP requests.
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 6]: fib: log an error when destroying non-empty tables
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 19]: ip: IP address family common input node

geneve: **community** vpp-dev@lists.fd.io
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 0]: geneve: support custom options in decap

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 0]: hsa: unify echo test setup

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 30]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39539 <https:////gerrit.fd.io/r/c/vpp/+/39539>`_ [VECr 0]: fib: Don't use an address from an attached prefix when sending ARP requests.
  | `39459 <https:////gerrit.fd.io/r/c/vpp/+/39459>`_ [VECr 1]: arp: fix arp request for ip4-glean node
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 1]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 19]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 19]: ip: IP address family common input node

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 13]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 30]: ipsec: huge anti-replay window support

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 1]: linux-cp: Add VRF synchronization
  | `39486 <https:////gerrit.fd.io/r/c/vpp/+/39486>`_ [VECr 15]: linux-cp: check if lcp_itf_pair exists before creating tap

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 0]: interface dpdk avf: introducing setting RSS hash key feature

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 14]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VECr 14]: nat: fix address resolution
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 14]: nat: nat66 cli bug fix

session: **Florin Coras** <fcoras@cisco.com>
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VECr 0]: session: program rx events only if none are pending

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VECr 28]: sr: SRv6 Path Tracing source node behavior

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 0]: hsa: unify echo test setup
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 0]: geneve: support custom options in decap
  | `39539 <https:////gerrit.fd.io/r/c/vpp/+/39539>`_ [VECr 0]: fib: Don't use an address from an attached prefix when sending ARP requests.
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 1]: tests: fix issues found when enabling DMAC check
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 1]: ip-neighbor: add version 3 of neighbor event
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 13]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 14]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 19]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 29]: ethernet: run callbacks for subifs too when mac changes
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 30]: ipsec: huge anti-replay window support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 30]: ipsec: huge anti-replay window support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 6]: misc: patch to test CI infra changes

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 30]: ipsec: huge anti-replay window support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 54]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 54]: api trace: the api trace info about barrier is opposite

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vec 33]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEC 1]: arp: fix arp request for ip4-glean node
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 48]: linux-cp: Fix update on IPv4 routes

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 98]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 118]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 128]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 176]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vEC 5]: ena: add tx checksum offloads and tso support
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 43]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 35]: ip6: ECMP hash support for ipv6 fragments

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 6]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 112]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 14]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 124]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 112]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 155]: dpdk: use adapter MTU in max_frame_size setting

**Florian Gavril** <gflorian@3nets.io>:

  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VEc 0]: fib: Crash when specify a big prefix length from CLI.

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VEc 2]: ethernet: check dmacs_bad in the fastpath case

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `39507 <https:////gerrit.fd.io/r/c/vpp/+/39507>`_ [VEc 1]: cnat: add flow hash config to cnat translation

**Jieqiang Wang** <jieqiang.wang@arm.com>:

  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VeC 35]: build: add multi-arch support for Neoverse N2 CPU

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 55]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 173]: nat: fix tcp session reopen in nat44-ed

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [VEc 14]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 44]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [vEC 19]: ip: Set the buffer error in ip6-input

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `39528 <https:////gerrit.fd.io/r/c/vpp/+/39528>`_ [VEc 0]: ping: Simple binary API for running ping based on events

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `39535 <https:////gerrit.fd.io/r/c/vpp/+/39535>`_ [VEc 0]: dpdk-cryptodev: improve dequeue behavior, fix cache stats logging
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 56]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 133]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 40]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 119]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 43]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 50]: interface: check sw_if_index more thoroughly
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 51]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 142]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 54]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 56]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 97]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 44]: libmemif: fix segfault and buffer overflow in examples

**Ting Xu** <ting.xu@intel.com>:

  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VeC 35]: dpdk: fix variable type in pattern parsing

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 37]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 160]: mpls: fix possible crashes on tunnel create/delete

**Vratko Polak** <vrpolak@cisco.com>:

  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VEc 7]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VEc 14]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 119]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 145]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 147]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 107]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 118]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 19]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 66]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 66]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEc 7]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 173]: nat: add local addresses correctly in nat lb static mapping

**ranjan raj** <ranjanx.raj@intel.com>:

  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VEc 0]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 36]: dhcp: fix dhcp multiple client request

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VeC 44]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 82]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 90]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
authors          61
maintainers      21
committers       0
abandoned        0
================ ===

