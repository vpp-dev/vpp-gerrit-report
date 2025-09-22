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
generated on Monday 2025-09-22, 02:45:52
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
  | `43606 <https:////gerrit.fd.io/r/c/vpp/+/43606>`_ [VECr 1]: af_xdp: introduce flag to allow SKB mode
  | `43610 <https:////gerrit.fd.io/r/c/vpp/+/43610>`_ [VECr 1]: af_xdp: allow usage of dynamic libbpf and libxdp

build: **Damjan Marion** <damarion@cisco.com>
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 6]: vppinfra: add ARM Neoverse-V1 support

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 3]: cnat: add vrf awareness

dev: **Damjan Marion** <damarion@cisco.com>
  | `43725 <https:////gerrit.fd.io/r/c/vpp/+/43725>`_ [VECr 2]: dev: add ability for process node to wait for device config

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 27]: gpcapng: first draft

ena: **Damjan Marion** <damarion@cisco.com>
  | `43725 <https:////gerrit.fd.io/r/c/vpp/+/43725>`_ [VECr 2]: dev: add ability for process node to wait for device config

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43669 <https:////gerrit.fd.io/r/c/vpp/+/43669>`_ [VECr 2]: hsa: include rtt & jitter measurements in echo client periodic reports
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 5]: hsa: http connect proxy client

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `43669 <https:////gerrit.fd.io/r/c/vpp/+/43669>`_ [VECr 2]: hsa: include rtt & jitter measurements in echo client periodic reports
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 5]: hsa: http connect proxy client

iavf: **Damjan Marion** <damarion@cisco.com>
  | `43725 <https:////gerrit.fd.io/r/c/vpp/+/43725>`_ [VECr 2]: dev: add ability for process node to wait for device config

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 11]: ip: make running_fragment_id thread safe

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43611 <https:////gerrit.fd.io/r/c/vpp/+/43611>`_ [VECr 1]: build: use /usr/bin/env bash in checkstyle shebang instead of /bin/bash
  | `43695 <https:////gerrit.fd.io/r/c/vpp/+/43695>`_ [VECr 2]: oe: add myself to OE maintainers
  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VECr 2]: crypto: call _mm256_zeroupper to fix SHA256 perf
  | `43712 <https:////gerrit.fd.io/r/c/vpp/+/43712>`_ [VECr 3]: interface: add cli config option for fq nelts
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 11]: crypto: enforce native thread-safe dataplane via read-only keys
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 27]: gpcapng: first draft

snort: **Damjan Marion** <damarion@cisco.com>
  | `43605 <https:////gerrit.fd.io/r/c/vpp/+/43605>`_ [VECr 5]: snort: fix the cli help

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VECr 3]: cnat: add vrf awareness
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 27]: gpcapng: first draft

vcl: **Florin Coras** <fcoras@cisco.com>
  | `43691 <https:////gerrit.fd.io/r/c/vpp/+/43691>`_ [VECr 3]: misc: patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 10]: vcl: LDP default to regular option

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43707 <https:////gerrit.fd.io/r/c/vpp/+/43707>`_ [VECr 2]: crypto: call _mm256_zeroupper to fix SHA256 perf
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 6]: vppinfra: add ARM Neoverse-V1 support
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 11]: crypto: enforce native thread-safe dataplane via read-only keys

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 128]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 54]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `42599 <https:////gerrit.fd.io/r/c/vpp/+/42599>`_ [veC 177]: WIP pvti: additional tests + fixes Change-Id: Id5ec994928bd757d395e61c464ee6341c1f6272d

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 61]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 82]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 83]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 116]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [vEC 2]: kube-test: added felix tests for calico in kube-test

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 111]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 126]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [VEc 28]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [VEc 13]: vppinfra: force cpu time sync when difference is too big
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 40]: stats: show raw value in show stat segment
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VeC 47]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 101]: session: fix parse_uri() usage

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 152]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 168]: ip:fix pmtu next node index errror, it should use own value

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VeC 52]: ping: add option to specify interface src-address

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43710 <https:////gerrit.fd.io/r/c/vpp/+/43710>`_ [vEc 3]: npol: Network Policies plugin
  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 4]: capo: Calico Policies plugin
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VeC 68]: cnat: converge new cnat implementation to support old usecases (calico)
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 109]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 122]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [vEC 3]: ipsec: unify crypto+HMAC in single op for ESP
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 136]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 109]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 160]: tests: add send_and_expect_multi

**Maxim Uvarov** <maxim@skbuff.ru>:

  | `43694 <https:////gerrit.fd.io/r/c/vpp/+/43694>`_ [vEC 2]: oe: add README.rst
  | `43693 <https:////gerrit.fd.io/r/c/vpp/+/43693>`_ [vEc 2]: oe: add openembedded layer to build vpp

**Maxime Peim** <maxime.peim@gmail.com>:

  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [vEC 4]: ping: introduce traceroute tool
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VeC 55]: dispatch-trace: add offload flags to trace

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 93]: ipip: fix support for ipip6o6 from linux tunnel

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 60]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 124]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 90]: snort: update VPP DAQ for multi-instance

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 75]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 123]: acl: added hit count logic in VPP for debugging

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 130]: tm: add tm framework for hw traffic management

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 174]: ip6-nd: simplify API to directly set options

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VEc 23]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 96]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 98]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 98]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 116]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 147]: nat: add nat44-ed ipfix dst address and port logging

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 145]: ip-neighbor: ARP/NA per-interface counter improvements

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 129]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 57]: dispatch-trace: fix crash issues caused by buffer-trace

**echo** <614699596@qq.com>:

  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VeC 47]: bonding: capture rx packets before ethernet-input node.

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 125]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 129]: Makefile: Added support for the Wind River eLxr distribution

**steven luong** <sluong@cisco.com>:

  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 4]: session: refactoring application_local.c

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 136]: snort: fix crash when using an output interface

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 77]: ethernet: fix mac mismatch in promisc mode

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [A 180]: build: support 128B/64B cache-line size in Arm image

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
maintainers      17
committers       0
abandoned        1
================ ===

