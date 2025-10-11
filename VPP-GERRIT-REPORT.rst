
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2025-10-11, 02:32:04
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

bufmon: **Benoît Ganne** <bganne@cisco.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 10]: cnat: converge new cnat implementation to support encaps (calico)

build: **Damjan Marion** <damarion@cisco.com>
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 25]: vppinfra: add ARM Neoverse-V1 support

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 10]: cnat: converge new cnat implementation to support encaps (calico)
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 22]: cnat: add vrf awareness

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 0]: ipsec: unify crypto+HMAC in single op for ESP
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 7]: crypto: experimental single key+op thread-safe handlers

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43869 <https:////gerrit.fd.io/r/c/vpp/+/43869>`_ [VECr 0]: sfdp: StateFul Data Plane
  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [VECr 0]: npol: Network Policies plugin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43848 <https:////gerrit.fd.io/r/c/vpp/+/43848>`_ [VECr 0]: session svm vcl: stop tracking app si in shr
  | `43866 <https:////gerrit.fd.io/r/c/vpp/+/43866>`_ [VECr 1]: quic: failed handshake improvements
  | `43846 <https:////gerrit.fd.io/r/c/vpp/+/43846>`_ [VECr 2]: quic: ALPN support

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `43844 <https:////gerrit.fd.io/r/c/vpp/+/43844>`_ [VECr 0]: svm: support decoupling fifo signals from shared fifo
  | `43848 <https:////gerrit.fd.io/r/c/vpp/+/43848>`_ [VECr 0]: session svm vcl: stop tracking app si in shr
  | `43849 <https:////gerrit.fd.io/r/c/vpp/+/43849>`_ [VECr 0]: svm session: stop sharing vpp si in shr
  | `43866 <https:////gerrit.fd.io/r/c/vpp/+/43866>`_ [VECr 1]: quic: failed handshake improvements

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 30]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 0]: ipsec: unify crypto+HMAC in single op for ESP

kube-test: **Florin Coras** <fcoras@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 2]: kube-test: bare metal cluster support

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43869 <https:////gerrit.fd.io/r/c/vpp/+/43869>`_ [VECr 0]: sfdp: StateFul Data Plane
  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [VECr 0]: npol: Network Policies plugin
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 0]: ipsec: unify crypto+HMAC in single op for ESP
  | `43873 <https:////gerrit.fd.io/r/c/vpp/+/43873>`_ [VECr 0]: sfdp_services: plugin with basic SFDP services
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 2]: kube-test: bare metal cluster support
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 7]: crypto: experimental single key+op thread-safe handlers
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 7]: crypto: enforce native thread-safe dataplane via read-only keys
  | `43694 <https:////gerrit.fd.io/r/c/vpp/+/43694>`_ [VECr 18]: oe: add README.rst
  | `43695 <https:////gerrit.fd.io/r/c/vpp/+/43695>`_ [VECr 18]: oe: add myself to OE maintainers

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `43880 <https:////gerrit.fd.io/r/c/vpp/+/43880>`_ [VECr 0]: quic: basic state formatting
  | `43877 <https:////gerrit.fd.io/r/c/vpp/+/43877>`_ [VECr 0]: quic: cleanup listener if crypto init fails
  | `43866 <https:////gerrit.fd.io/r/c/vpp/+/43866>`_ [VECr 1]: quic: failed handshake improvements
  | `43846 <https:////gerrit.fd.io/r/c/vpp/+/43846>`_ [VECr 2]: quic: ALPN support
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 7]: crypto: experimental single key+op thread-safe handlers

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `43760 <https:////gerrit.fd.io/r/c/vpp/+/43760>`_ [VECr 13]: rdma: allow dynamic libibverbs and libmlx5

selog: **Mohammed Hawari** <mohammed@hawari.fr>
  | `43875 <https:////gerrit.fd.io/r/c/vpp/+/43875>`_ [VECr 0]: selog: fix coverity warnings

session: **Florin Coras** <fcoras@cisco.com>
  | `43878 <https:////gerrit.fd.io/r/c/vpp/+/43878>`_ [VECr 0]: session: fix al cleanup if listen fails
  | `43844 <https:////gerrit.fd.io/r/c/vpp/+/43844>`_ [VECr 0]: svm: support decoupling fifo signals from shared fifo
  | `43848 <https:////gerrit.fd.io/r/c/vpp/+/43848>`_ [VECr 0]: session svm vcl: stop tracking app si in shr
  | `43849 <https:////gerrit.fd.io/r/c/vpp/+/43849>`_ [VECr 0]: svm session: stop sharing vpp si in shr

snort: **Damjan Marion** <damarion@cisco.com>
  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VECr 2]: snort: fix crash when using an output interface
  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VECr 3]: snort: update VPP DAQ for multi-instance
  | `43764 <https:////gerrit.fd.io/r/c/vpp/+/43764>`_ [VECr 4]: snort: add support for packet injection

svm: **Dave Barach** <vpp@barachs.net>
  | `43844 <https:////gerrit.fd.io/r/c/vpp/+/43844>`_ [VECr 0]: svm: support decoupling fifo signals from shared fifo
  | `43848 <https:////gerrit.fd.io/r/c/vpp/+/43848>`_ [VECr 0]: session svm vcl: stop tracking app si in shr
  | `43849 <https:////gerrit.fd.io/r/c/vpp/+/43849>`_ [VECr 0]: svm session: stop sharing vpp si in shr

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [VECr 0]: npol: Network Policies plugin
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 0]: ipsec: unify crypto+HMAC in single op for ESP
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 10]: cnat: converge new cnat implementation to support encaps (calico)
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 22]: cnat: add vrf awareness

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 0]: ipsec: unify crypto+HMAC in single op for ESP

vcl: **Florin Coras** <fcoras@cisco.com>
  | `43844 <https:////gerrit.fd.io/r/c/vpp/+/43844>`_ [VECr 0]: svm: support decoupling fifo signals from shared fifo
  | `43848 <https:////gerrit.fd.io/r/c/vpp/+/43848>`_ [VECr 0]: session svm vcl: stop tracking app si in shr
  | `43849 <https:////gerrit.fd.io/r/c/vpp/+/43849>`_ [VECr 0]: svm session: stop sharing vpp si in shr
  | `43691 <https:////gerrit.fd.io/r/c/vpp/+/43691>`_ [VECr 0]: misc: patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 29]: vcl: LDP default to regular option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43862 <https:////gerrit.fd.io/r/c/vpp/+/43862>`_ [VECr 2]: vlib: Fix version.h include error
  | `43841 <https:////gerrit.fd.io/r/c/vpp/+/43841>`_ [VECr 4]: stats: add missing gauge type in remove check

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43876 <https:////gerrit.fd.io/r/c/vpp/+/43876>`_ [VECr 0]: vppinfra: don't use dlmalloc apis outside of mem_dlmalloc.c
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 7]: crypto: enforce native thread-safe dataplane via read-only keys
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 25]: vppinfra: add ARM Neoverse-V1 support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [VEc 10]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 147]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VeC 46]: gpcapng: first draft
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 73]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 80]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 101]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 102]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 135]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [VEc 16]: kube-test: added felix tests for calico in kube-test

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 130]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 145]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [Vec 47]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [Vec 32]: vppinfra: force cpu time sync when difference is too big
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 59]: stats: show raw value in show stat segment
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VeC 66]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 120]: session: fix parse_uri() usage

**Damjan Marion** <dmarion@0xa5.net>:

  | `43879 <https:////gerrit.fd.io/r/c/vpp/+/43879>`_ [vEC 0]: vppinfra: forward declare clib_mem_heap_t

**Florin Coras** <florin.coras@gmail.com>:

  | `43860 <https:////gerrit.fd.io/r/c/vpp/+/43860>`_ [VEc 0]: vcl: optimize handling of ct fifos

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 171]: feature: embed data lengths in feat cfg strings

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VeC 71]: ping: add option to specify interface src-address

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 23]: capo: Calico Policies plugin
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 128]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 141]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 155]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 128]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 179]: tests: add send_and_expect_multi

**Maxim Uvarov** <maxim@skbuff.ru>:

  | `43693 <https:////gerrit.fd.io/r/c/vpp/+/43693>`_ [vEc 18]: oe: add openembedded layer to build vpp

**Maxime Peim** <maxime.peim@gmail.com>:

  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [VEc 4]: ping: introduce traceroute tool
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VeC 74]: dispatch-trace: add offload flags to trace

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `43874 <https:////gerrit.fd.io/r/c/vpp/+/43874>`_ [vEC 0]: unittest: add sfdp testing and unity framework

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 112]: ipip: fix support for ipip6o6 from linux tunnel

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [VEc 4]: af_xdp: allow usage of dynamic libbpf and libxdp
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [VEc 4]: af_xdp: introduce flag to allow SKB mode
  | `43611 <https:////gerrit.fd.io/r/c/vpp/+/43611>`_ [VEc 11]: build: use /usr/bin/env bash in checkstyle shebang instead of /bin/bash

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 79]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 143]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 94]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 142]: acl: added hit count logic in VPP for debugging

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 149]: tm: add tm framework for hw traffic management

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [Vec 42]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 115]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 117]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 117]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 135]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 166]: nat: add nat44-ed ipfix dst address and port logging

**Vratko Polak** <vrpolak@cisco.com>:

  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VEc 1]: crypto: call _mm256_zeroupper to fix SHA256 perf

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 164]: ip-neighbor: ARP/NA per-interface counter improvements

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 148]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 76]: dispatch-trace: fix crash issues caused by buffer-trace

**echo** <614699596@qq.com>:

  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VeC 66]: bonding: capture rx packets before ethernet-input node.

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 144]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 148]: Makefile: Added support for the Wind River eLxr distribution

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 96]: ethernet: fix mac mismatch in promisc mode

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
maintainers      31
committers       0
abandoned        0
================ ===

