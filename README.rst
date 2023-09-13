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
generated on Wednesday 2023-09-13, 01:57:52
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

adl: **Dave Barach** <vpp@barachs.net>
  | `39140 <https:////gerrit.fd.io/r/c/vpp/+/39140>`_ [VECr 0]: adl: stabilize the API

api: **Dave Barach** <vpp@barachs.net>
  | `39413 <https:////gerrit.fd.io/r/c/vpp/+/39413>`_ [VECr 11]: api: fix vlibmemory coverity warning CID-300152

build: **Damjan Marion** <damarion@cisco.com>
  | `39415 <https:////gerrit.fd.io/r/c/vpp/+/39415>`_ [VECr 11]: build: add vpp_plugins include directory
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 27]: dpdk: fix variable type in pattern parsing
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 27]: build: add multi-arch support for Neoverse N2 CPU

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VECr 28]: dhcp: fix dhcp multiple client request

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 21]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 11]: ip: IP address family common input node

flow: **Damjan Marion** <damarion@cisco.com>
  | `39143 <https:////gerrit.fd.io/r/c/vpp/+/39143>`_ [VECr 0]: flow: mark API as production

geneve: **community** vpp-dev@lists.fd.io
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 8]: geneve: support custom options in decap

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `39411 <https:////gerrit.fd.io/r/c/vpp/+/39411>`_ [VECr 11]: hsa: fix coverity issue CID-313635

idpf: **Ting Xu** <ting.xu@intel.com>
  | `39522 <https:////gerrit.fd.io/r/c/vpp/+/39522>`_ [VECr 0]: idpf: make plugin default disabled until issues are fixed

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `39500 <https:////gerrit.fd.io/r/c/vpp/+/39500>`_ [VECr 6]: build: fix clang-16 build

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39459 <https:////gerrit.fd.io/r/c/vpp/+/39459>`_ [VECr 0]: arp: fix arp request for ip4-glean node
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 0]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 11]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VECr 11]: ip: IP address family common input node
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 27]: ip6: ECMP hash support for ipv6 fragments

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VECr 29]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 5]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 0]: linux-cp: Add VRF synchronization
  | `39486 <https:////gerrit.fd.io/r/c/vpp/+/39486>`_ [VECr 7]: linux-cp: check if lcp_itf_pair exists before creating tap

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39141 <https:////gerrit.fd.io/r/c/vpp/+/39141>`_ [VECr 0]: crypto-sw-scheduler: stabilize the API

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 6]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VECr 6]: nat: fix address resolution
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 6]: nat: nat66 cli bug fix
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 26]: nat: fix nat44_ed set_session_limit crash

npt66: **Ole Troan** <otroan@employees.org>
  | `39506 <https:////gerrit.fd.io/r/c/vpp/+/39506>`_ [VECr 4]: npt66: ensure feature is not configured multiple times

pci: **Damjan Marion** <damarion@cisco.com>
  | `39436 <https:////gerrit.fd.io/r/c/vpp/+/39436>`_ [VECr 11]: vlib: deuglify the offset finding loop in pci.c
  | `39409 <https:////gerrit.fd.io/r/c/vpp/+/39409>`_ [VECr 11]: pci: fix coverity issue CID-322372

perfmon: **Damjan Marion** <damarion@cisco.com>, **Ray Kinsella** <mdr@ashroe.eu>
  | `39469 <https:////gerrit.fd.io/r/c/vpp/+/39469>`_ [VECr 11]: perfmon: fix perf_user_access_enabled type

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `39501 <https:////gerrit.fd.io/r/c/vpp/+/39501>`_ [VECr 5]: quic: fix quic sessions state updates

session: **Florin Coras** <fcoras@cisco.com>
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VECr 6]: session: program rx events only if none are pending

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `39144 <https:////gerrit.fd.io/r/c/vpp/+/39144>`_ [VECr 0]: sr: mark sr_policies_v2_details message as production
  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VECr 20]: sr: SRv6 Path Tracing source node behavior

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 0]: ip-neighbor: add version 3 of neighbor event
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 5]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `39501 <https:////gerrit.fd.io/r/c/vpp/+/39501>`_ [VECr 5]: quic: fix quic sessions state updates
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 6]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 8]: tests: fix issues found when enabling DMAC check
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 8]: geneve: support custom options in decap
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VECr 11]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `39437 <https:////gerrit.fd.io/r/c/vpp/+/39437>`_ [VECr 11]: tests: remove unsupported qemu feature
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 21]: ethernet: run callbacks for subifs too when mac changes
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 26]: nat: fix nat44_ed set_session_limit crash

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VECr 6]: session: program rx events only if none are pending
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 12]: misc: patch to test CI infra changes

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39503 <https:////gerrit.fd.io/r/c/vpp/+/39503>`_ [VECr 5]: vppinfra: fix setns typo
  | `39412 <https:////gerrit.fd.io/r/c/vpp/+/39412>`_ [VECr 11]: vppinfra: fix coverity warning CID-313632
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 27]: build: add multi-arch support for Neoverse N2 CPU

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39142 <https:////gerrit.fd.io/r/c/vpp/+/39142>`_ [VECr 0]: wireguard: stabilize the API

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 46]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 46]: api trace: the api trace info about barrier is opposite

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEc 25]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEC 0]: arp: fix arp request for ip4-glean node
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 40]: linux-cp: Fix update on IPv4 routes

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 90]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 110]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 120]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 168]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 35]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `39523 <https:////gerrit.fd.io/r/c/vpp/+/39523>`_ [vEC 0]: vppinfra: add ARM Neoverse-N2 support
  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [veC 36]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 104]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [VEc 6]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 116]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 104]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39410 <https:////gerrit.fd.io/r/c/vpp/+/39410>`_ [vEC 14]: vapi: fix coverity warnings

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 147]: dpdk: use adapter MTU in max_frame_size setting

**Florian Gavril** <gflorian@3nets.io>:

  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VeC 85]: fib: Crash when specify a big prefix length from CLI.

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VEc 7]: ethernet: check dmacs_bad in the fastpath case

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `39507 <https:////gerrit.fd.io/r/c/vpp/+/39507>`_ [vEC 1]: cnat: add flow hash config to cnat translation

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 47]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 165]: nat: fix tcp session reopen in nat44-ed

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [VEc 6]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 36]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [vEC 11]: ip: Set the buffer error in ip6-input

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 48]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 125]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 32]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 111]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 35]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 42]: interface: check sw_if_index more thoroughly
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 43]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 134]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 46]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 48]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 89]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 36]: libmemif: fix segfault and buffer overflow in examples

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 152]: mpls: fix possible crashes on tunnel create/delete
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 178]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 178]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `39505 <https:////gerrit.fd.io/r/c/vpp/+/39505>`_ [VEc 0]: docs: mention how to build VPP outside git
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VEc 0]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VEc 6]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 111]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 137]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 139]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 174]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 179]: ipsec: missing linear search when flow cache search failed

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 40]: interface dpdk avf: introducing setting RSS hash key feature
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 99]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 110]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 11]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 58]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 58]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 110]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 165]: nat: add local addresses correctly in nat lb static mapping

**ranjan raj** <ranjanx.raj@intel.com>:

  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [vEc 0]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VeC 36]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 74]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 82]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
maintainers      41
committers       0
abandoned        0
================ ===

