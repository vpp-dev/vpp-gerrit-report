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
generated on Wednesday 2025-10-08, 02:36:21
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
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 7]: cnat: converge new cnat implementation to support encaps (calico)

build: **Damjan Marion** <damarion@cisco.com>
  | `43842 <https:////gerrit.fd.io/r/c/vpp/+/43842>`_ [VECr 1]: build: update platform cn913x compile flags
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 22]: vppinfra: add ARM Neoverse-V1 support

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 7]: cnat: converge new cnat implementation to support encaps (calico)
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 19]: cnat: add vrf awareness

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 4]: ipsec: unify crypto+HMAC in single op for ESP
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 4]: crypto: experimental single key+op thread-safe handlers

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 27]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 4]: ipsec: unify crypto+HMAC in single op for ESP

kube-test: **Florin Coras** <fcoras@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 0]: kube-test: bare metal cluster support

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43615 <https:////gerrit.fd.io/r/c/vpp/+/43615>`_ [VECr 0]: kube-test: bare metal cluster support
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 4]: ipsec: unify crypto+HMAC in single op for ESP
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 4]: crypto: experimental single key+op thread-safe handlers
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 4]: crypto: enforce native thread-safe dataplane via read-only keys
  | `43694 <https:////gerrit.fd.io/r/c/vpp/+/43694>`_ [VECr 15]: oe: add README.rst
  | `43695 <https:////gerrit.fd.io/r/c/vpp/+/43695>`_ [VECr 15]: oe: add myself to OE maintainers

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `43818 <https:////gerrit.fd.io/r/c/vpp/+/43818>`_ [VECr 4]: crypto: experimental single key+op thread-safe handlers

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `43760 <https:////gerrit.fd.io/r/c/vpp/+/43760>`_ [VECr 10]: rdma: allow dynamic libibverbs and libmlx5

snort: **Damjan Marion** <damarion@cisco.com>
  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VECr 0]: snort: fix crash when using an output interface
  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VECr 0]: snort: update VPP DAQ for multi-instance
  | `43764 <https:////gerrit.fd.io/r/c/vpp/+/43764>`_ [VECr 1]: snort: add support for packet injection

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [VECr 4]: ipsec: unify crypto+HMAC in single op for ESP
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 7]: cnat: converge new cnat implementation to support encaps (calico)
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 19]: cnat: add vrf awareness

vcl: **Florin Coras** <fcoras@cisco.com>
  | `43691 <https:////gerrit.fd.io/r/c/vpp/+/43691>`_ [VECr 0]: misc: patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 26]: vcl: LDP default to regular option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43857 <https:////gerrit.fd.io/r/c/vpp/+/43857>`_ [VECr 0]: vlib: expose function to switch elog_main
  | `43841 <https:////gerrit.fd.io/r/c/vpp/+/43841>`_ [VECr 1]: stats: add missing gauge type in remove check

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43835 <https:////gerrit.fd.io/r/c/vpp/+/43835>`_ [VECr 4]: vppinfra: add CLOEXEC flag to memfd create calls
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 4]: crypto: enforce native thread-safe dataplane via read-only keys
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 22]: vppinfra: add ARM Neoverse-V1 support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [VEc 7]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 144]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VeC 43]: gpcapng: first draft
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 70]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 77]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 98]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 99]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 132]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [VEc 13]: kube-test: added felix tests for calico in kube-test

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 127]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 142]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [Vec 44]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [VEc 29]: vppinfra: force cpu time sync when difference is too big
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 56]: stats: show raw value in show stat segment
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VeC 63]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 117]: session: fix parse_uri() usage

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 168]: feature: embed data lengths in feat cfg strings

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VeC 68]: ping: add option to specify interface src-address

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [VEc 4]: npol: Network Policies plugin
  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 20]: capo: Calico Policies plugin
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 125]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 138]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 152]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 125]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 176]: tests: add send_and_expect_multi

**Matus Fabian** <matfabia@cisco.com>:

  | `43846 <https:////gerrit.fd.io/r/c/vpp/+/43846>`_ [VEc 0]: quic: ALPN support

**Maxim Uvarov** <maxim@skbuff.ru>:

  | `43693 <https:////gerrit.fd.io/r/c/vpp/+/43693>`_ [vEc 15]: oe: add openembedded layer to build vpp

**Maxime Peim** <maxime.peim@gmail.com>:

  | `43840 <https:////gerrit.fd.io/r/c/vpp/+/43840>`_ [VEc 0]: ip: remove hotwired udp-lookup next node
  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [VEc 1]: ping: introduce traceroute tool
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VeC 71]: dispatch-trace: add offload flags to trace

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `43858 <https:////gerrit.fd.io/r/c/vpp/+/43858>`_ [vEC 0]: selog: introduce the Shared Elog plugin
  | `43859 <https:////gerrit.fd.io/r/c/vpp/+/43859>`_ [vEC 0]: selog: selog client lib
  | `43853 <https:////gerrit.fd.io/r/c/vpp/+/43853>`_ [vEC 0]: vlib: introducing Shared Elog (selog)

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 109]: ipip: fix support for ipip6o6 from linux tunnel

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [VEc 1]: af_xdp: allow usage of dynamic libbpf and libxdp
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [VEc 1]: af_xdp: introduce flag to allow SKB mode
  | `43611 <https:////gerrit.fd.io/r/c/vpp/+/43611>`_ [VEc 8]: build: use /usr/bin/env bash in checkstyle shebang instead of /bin/bash

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 76]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 140]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 91]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 139]: acl: added hit count logic in VPP for debugging

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 146]: tm: add tm framework for hw traffic management

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [Vec 39]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 112]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 114]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 114]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 132]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 163]: nat: add nat44-ed ipfix dst address and port logging

**Vratko Polak** <vrpolak@cisco.com>:

  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VEc 4]: crypto: call _mm256_zeroupper to fix SHA256 perf

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 161]: ip-neighbor: ARP/NA per-interface counter improvements

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 145]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 73]: dispatch-trace: fix crash issues caused by buffer-trace

**echo** <614699596@qq.com>:

  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VeC 63]: bonding: capture rx packets before ethernet-input node.

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 141]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 145]: Makefile: Added support for the Wind River eLxr distribution

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 93]: ethernet: fix mac mismatch in promisc mode

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
authors          56
maintainers      20
committers       0
abandoned        0
================ ===

