
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2025-09-27, 02:31:58
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
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [VECr 6]: af_xdp: introduce flag to allow SKB mode
  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [VECr 6]: af_xdp: allow usage of dynamic libbpf and libxdp

bufmon: **Benoît Ganne** <bganne@cisco.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: converge new cnat implementation to support encaps (calico)

build: **Damjan Marion** <damarion@cisco.com>
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 11]: vppinfra: add ARM Neoverse-V1 support

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: converge new cnat implementation to support encaps (calico)
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 8]: cnat: add vrf awareness

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 1]: ipsec: unify crypto+HMAC in single op for ESP

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [VECr 2]: ping: introduce traceroute tool

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [VECr 2]: ping: introduce traceroute tool

http: **Florin Coras** <fcoras@cisco.com>
  | `43753 <https:////gerrit.fd.io/r/c/vpp/+/43753>`_ [VECr 1]: http: QPACK decoding request and response
  | `43751 <https:////gerrit.fd.io/r/c/vpp/+/43751>`_ [VECr 1]: http: move generic functions to hpack_inlines.h
  | `43651 <https:////gerrit.fd.io/r/c/vpp/+/43651>`_ [VECr 1]: http: QPACK header decoding w/o dynamic table

interface: **Dave Barach** <vpp@barachs.net>
  | `43613 <https:////gerrit.fd.io/r/c/vpp/+/43613>`_ [VECr 3]: interface: interface monitor CLI displays incorrect rate statistics

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `43755 <https:////gerrit.fd.io/r/c/vpp/+/43755>`_ [VECr 1]: ip: ip6 frags should have as much space for headers as original
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 16]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 1]: ipsec: unify crypto+HMAC in single op for ESP

kube-test: **Florin Coras** <fcoras@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 0]: kube-test: bare metal cluster support

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 0]: kube-test: bare metal cluster support
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 1]: ipsec: unify crypto+HMAC in single op for ESP
  | `43694 <https:////gerrit.fd.io/r/c/vpp/+/43694>`_ [VECr 4]: oe: add README.rst
  | `43695 <https:////gerrit.fd.io/r/c/vpp/+/43695>`_ [VECr 4]: oe: add myself to OE maintainers
  | `43611 <https:////gerrit.fd.io/r/c/vpp/+/43611>`_ [VECr 6]: build: use /usr/bin/env bash in checkstyle shebang instead of /bin/bash
  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VECr 7]: crypto: call _mm256_zeroupper to fix SHA256 perf
  | `43712 <https:////gerrit.fd.io/r/c/vpp/+/43712>`_ [VECr 8]: interface: add cli config option for fq nelts
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 16]: crypto: enforce native thread-safe dataplane via read-only keys

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [VECr 2]: ping: introduce traceroute tool

snort: **Damjan Marion** <damarion@cisco.com>
  | `43605 <https:////gerrit.fd.io/r/c/vpp/+/43605>`_ [VECr 10]: snort: fix the cli help

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 0]: cnat: converge new cnat implementation to support encaps (calico)
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 1]: ipsec: unify crypto+HMAC in single op for ESP
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 8]: cnat: add vrf awareness

vcl: **Florin Coras** <fcoras@cisco.com>
  | `43691 <https:////gerrit.fd.io/r/c/vpp/+/43691>`_ [VECr 2]: misc: patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 15]: vcl: LDP default to regular option

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VECr 7]: crypto: call _mm256_zeroupper to fix SHA256 perf
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 11]: vppinfra: add ARM Neoverse-V1 support
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 16]: crypto: enforce native thread-safe dataplane via read-only keys

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `43759 <https:////gerrit.fd.io/r/c/vpp/+/43759>`_ [VEc 0]: hs-test: add suite labels and label filtering

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [VEc 0]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 133]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VeC 32]: gpcapng: first draft
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 59]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 66]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 87]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 88]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 121]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [VEc 2]: kube-test: added felix tests for calico in kube-test

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 116]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 131]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [Vec 33]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [VEc 18]: vppinfra: force cpu time sync when difference is too big
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 45]: stats: show raw value in show stat segment
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VeC 52]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 106]: session: fix parse_uri() usage

**Damjan Marion** <dmarion@0xa5.net>:

  | `43779 <https:////gerrit.fd.io/r/c/vpp/+/43779>`_ [vEC 0]: stats: export stats as fuse fs

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 157]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 173]: ip:fix pmtu next node index errror, it should use own value

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VeC 57]: ping: add option to specify interface src-address

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [VEc 1]: npol: Network Policies plugin
  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 9]: capo: Calico Policies plugin
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 114]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 127]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 141]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 114]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 165]: tests: add send_and_expect_multi

**Maxim Uvarov** <maxim@skbuff.ru>:

  | `43693 <https:////gerrit.fd.io/r/c/vpp/+/43693>`_ [vEc 4]: oe: add openembedded layer to build vpp

**Maxime Peim** <maxime.peim@gmail.com>:

  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VeC 60]: dispatch-trace: add offload flags to trace

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 98]: ipip: fix support for ipip6o6 from linux tunnel

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 65]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 129]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 95]: snort: update VPP DAQ for multi-instance

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 80]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 128]: acl: added hit count logic in VPP for debugging

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 135]: tm: add tm framework for hw traffic management

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 179]: ip6-nd: simplify API to directly set options

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VEc 28]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 101]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 103]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 103]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 121]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 152]: nat: add nat44-ed ipfix dst address and port logging

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 150]: ip-neighbor: ARP/NA per-interface counter improvements

**Yoann Desmouceaux** <ydesmouc@cisco.com>:

  | `43758 <https:////gerrit.fd.io/r/c/vpp/+/43758>`_ [VEc 0]: octeon: add switch_header_type argument

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 134]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 62]: dispatch-trace: fix crash issues caused by buffer-trace

**echo** <614699596@qq.com>:

  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VeC 52]: bonding: capture rx packets before ethernet-input node.

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 130]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 134]: Makefile: Added support for the Wind River eLxr distribution

**steven luong** <sluong@cisco.com>:

  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 9]: session: refactoring application_local.c

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 141]: snort: fix crash when using an output interface

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 82]: ethernet: fix mac mismatch in promisc mode

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
authors          54
maintainers      23
committers       0
abandoned        0
================ ===

