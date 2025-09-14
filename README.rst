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
generated on Sunday 2025-09-14, 02:41:10
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
  | `43600 <https:////gerrit.fd.io/r/c/vpp/+/43600>`_ [VECr 1]: hs-test: move hs-test to vpp/test-c

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43600 <https:////gerrit.fd.io/r/c/vpp/+/43600>`_ [VECr 1]: hs-test: move hs-test to vpp/test-c
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 19]: gpcapng: first draft

fib: **Neale Ranns** <neale@graphiant.com>
  | `43679 <https:////gerrit.fd.io/r/c/vpp/+/43679>`_ [VECr 1]: fib: guard against reallocs

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43681 <https:////gerrit.fd.io/r/c/vpp/+/43681>`_ [VECr 1]: session tls: add support for configurable trusted cas
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 4]: hsa: http connect proxy client
  | `43667 <https:////gerrit.fd.io/r/c/vpp/+/43667>`_ [VECr 4]: http: add worker counters
  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [VECr 5]: hs-test: added felix and finalizer tests for calico in hs-test

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `43681 <https:////gerrit.fd.io/r/c/vpp/+/43681>`_ [VECr 1]: session tls: add support for configurable trusted cas
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 4]: hsa: http connect proxy client
  | `43676 <https:////gerrit.fd.io/r/c/vpp/+/43676>`_ [VECr 4]: hsa: proxy don't send tx event when fifo is empty
  | `43674 <https:////gerrit.fd.io/r/c/vpp/+/43674>`_ [VECr 4]: hsa: proxy http can be closed on ao connected err

http: **Florin Coras** <fcoras@cisco.com>
  | `43673 <https:////gerrit.fd.io/r/c/vpp/+/43673>`_ [VECr 4]: http: add half-close support for h2 tcp tunnels
  | `43667 <https:////gerrit.fd.io/r/c/vpp/+/43667>`_ [VECr 4]: http: add worker counters

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 3]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `43643 <https:////gerrit.fd.io/r/c/vpp/+/43643>`_ [VECr 16]: ipsec: Improve tunnel mode detection in ESP decrypt post-crypto

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43600 <https:////gerrit.fd.io/r/c/vpp/+/43600>`_ [VECr 1]: hs-test: move hs-test to vpp/test-c
  | `43695 <https:////gerrit.fd.io/r/c/vpp/+/43695>`_ [VECr 1]: oe: add myself to OE maintainers
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 3]: crypto: enforce native thread-safe dataplane via read-only keys
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 19]: gpcapng: first draft

session: **Florin Coras** <fcoras@cisco.com>
  | `43681 <https:////gerrit.fd.io/r/c/vpp/+/43681>`_ [VECr 1]: session tls: add support for configurable trusted cas

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 19]: gpcapng: first draft

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `43681 <https:////gerrit.fd.io/r/c/vpp/+/43681>`_ [VECr 1]: session tls: add support for configurable trusted cas

vcl: **Florin Coras** <fcoras@cisco.com>
  | `43691 <https:////gerrit.fd.io/r/c/vpp/+/43691>`_ [VECr 1]: misc: patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 2]: vcl: LDP default to regular option

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43679 <https:////gerrit.fd.io/r/c/vpp/+/43679>`_ [VECr 1]: fib: guard against reallocs
  | `43602 <https:////gerrit.fd.io/r/c/vpp/+/43602>`_ [VECr 1]: vppinfra: zero-terminate self netns path
  | `43683 <https:////gerrit.fd.io/r/c/vpp/+/43683>`_ [VECr 3]: crypto: enforce native thread-safe dataplane via read-only keys

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `43603 <https:////gerrit.fd.io/r/c/vpp/+/43603>`_ [vEC 1]: kube-test: multi-worker calicovpp iperf tests

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 120]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 46]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `42599 <https:////gerrit.fd.io/r/c/vpp/+/42599>`_ [veC 169]: WIP pvti: additional tests + fixes Change-Id: Id5ec994928bd757d395e61c464ee6341c1f6272d
  | `42192 <https:////gerrit.fd.io/r/c/vpp/+/42192>`_ [veC 179]: WIP: the tests which fail with a FIPS version of openssl

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 53]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 74]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 75]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 108]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 103]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 118]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [VEc 20]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [VEc 5]: vppinfra: force cpu time sync when difference is too big
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VeC 32]: stats: show raw value in show stat segment
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VeC 39]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 93]: session: fix parse_uri() usage

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 144]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 160]: ip:fix pmtu next node index errror, it should use own value

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VeC 44]: ping: add option to specify interface src-address

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 24]: capo: Calico Policies plugin
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VeC 60]: cnat: converge new cnat implementation to support old usecases (calico)
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 101]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 114]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [vEc 23]: ipsec: unify crypto+HMAC in single op for ESP
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 128]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 101]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 152]: tests: add send_and_expect_multi

**Matus Fabian** <matfabia@cisco.com>:

  | `43616 <https:////gerrit.fd.io/r/c/vpp/+/43616>`_ [vEC 3]: hsa: http connect proxy client multiworker support

**Maxim Uvarov** <maxim@skbuff.ru>:

  | `43694 <https:////gerrit.fd.io/r/c/vpp/+/43694>`_ [vEC 1]: add README.rst
  | `43693 <https:////gerrit.fd.io/r/c/vpp/+/43693>`_ [vEC 1]: oe: add openembedded layer to build vpp

**Maxime Peim** <mpeim@cisco.com>:

  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [vEc 26]: ping: introduce traceroute tool
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VeC 47]: dispatch-trace: add offload flags to trace

**Michael Aronovici** <aronovic@cisco.com>:

  | `43439 <https:////gerrit.fd.io/r/c/vpp/+/43439>`_ [VEc 4]: bfd: add API to configure TOS for IP of BFD packets

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `43688 <https:////gerrit.fd.io/r/c/vpp/+/43688>`_ [vEC 2]: session: hack to fix UDP CL

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 85]: ipip: fix support for ipip6o6 from linux tunnel

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 52]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 116]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 82]: snort: update VPP DAQ for multi-instance

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 67]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 115]: acl: added hit count logic in VPP for debugging

**Semir Sionek** <ssionek@cisco.com>:

  | `43669 <https:////gerrit.fd.io/r/c/vpp/+/43669>`_ [VEc 1]: hsa: include rtt & jitter measurements in echo client periodic reports

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `43015 <https:////gerrit.fd.io/r/c/vpp/+/43015>`_ [VeC 71]: vapi: uds transport pass client index correctly
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VeC 88]: cnat: add vrf awareness

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 122]: tm: add tm framework for hw traffic management

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [veC 172]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 166]: ip6-nd: simplify API to directly set options

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VEc 15]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 88]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 90]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 90]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 108]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 139]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 173]: nat: speedup nat44-ed vrf table lookups
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 174]: fib: fix fib entry tracking crash on table remove

**Vratko Polak** <vrpolak@cisco.com>:

  | `43682 <https:////gerrit.fd.io/r/c/vpp/+/43682>`_ [vEC 1]: dpdk-cryptodev: guard against cmt->keys realloc

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 137]: ip-neighbor: ARP/NA per-interface counter improvements

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 121]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 49]: dispatch-trace: fix crash issues caused by buffer-trace

**echo** <614699596@qq.com>:

  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VeC 39]: bonding: capture rx packets before ethernet-input node.

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 117]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 121]: Makefile: Added support for the Wind River eLxr distribution

**steven luong** <sluong@cisco.com>:

  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 2]: session: refactoring application_local.c

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 128]: snort: fix crash when using an output interface

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 69]: ethernet: fix mac mismatch in promisc mode

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
authors          64
maintainers      17
committers       0
abandoned        0
================ ===

