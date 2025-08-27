
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2025-08-27, 02:41:08
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

bonding: **Steven Luong** <sluong@cisco.com>
  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VECr 21]: bonding: capture rx packets before ethernet-input node.

build: **Damjan Marion** <damarion@cisco.com>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 8]: vppinfra: add ARM neoverse-v2 support

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 1]: gpcapng: first draft

ebuild: **Dave Barach** <vpp@barachs.net>
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VECr 20]: build: Add VPP_MAX_WORKERS configure option

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43544 <https:////gerrit.fd.io/r/c/vpp/+/43544>`_ [VECr 6]: vnet: add SFF8472 and SFF8636 diagnostics

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `43638 <https:////gerrit.fd.io/r/c/vpp/+/43638>`_ [VECr 0]: hs-test: added felix and finalizer tests for calico in hs-test
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 0]: hsa: http connect proxy client

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `43490 <https:////gerrit.fd.io/r/c/vpp/+/43490>`_ [VECr 0]: hsa: http connect proxy client

interface: **Dave Barach** <vpp@barachs.net>
  | `43544 <https:////gerrit.fd.io/r/c/vpp/+/43544>`_ [VECr 6]: vnet: add SFF8472 and SFF8636 diagnostics
  | `43591 <https:////gerrit.fd.io/r/c/vpp/+/43591>`_ [VECr 6]: vnet: fix set interfaces rx-placement cli
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VECr 29]: dispatch-trace: add offload flags to trace

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `43589 <https:////gerrit.fd.io/r/c/vpp/+/43589>`_ [VECr 0]: fib: change the order of adding interface routes
  | `43551 <https:////gerrit.fd.io/r/c/vpp/+/43551>`_ [VECr 8]: ip: 'format_ip6_header' - re-enable recurse into next proto layer
  | `43507 <https:////gerrit.fd.io/r/c/vpp/+/43507>`_ [VECr 16]: ip: reassembly - enable registering custom next nodes for v6

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 1]: gpcapng: first draft
  | `43544 <https:////gerrit.fd.io/r/c/vpp/+/43544>`_ [VECr 6]: vnet: add SFF8472 and SFF8636 diagnostics
  | `43508 <https:////gerrit.fd.io/r/c/vpp/+/43508>`_ [VECr 25]: vnet: install full reassembly headers

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `43630 <https:////gerrit.fd.io/r/c/vpp/+/43630>`_ [VECr 1]: octeon: add L4 checksum flags

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 26]: ping: add option to specify interface src-address

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43589 <https:////gerrit.fd.io/r/c/vpp/+/43589>`_ [VECr 0]: fib: change the order of adding interface routes
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 1]: gpcapng: first draft
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 26]: ping: add option to specify interface src-address

vcl: **Florin Coras** <fcoras@cisco.com>
  | `42380 <https:////gerrit.fd.io/r/c/vpp/+/42380>`_ [VECr 0]: misc: patch to test CI infra changes

vhost: **Steven Luong** <sluong@cisco.com>
  | `43627 <https:////gerrit.fd.io/r/c/vpp/+/43627>`_ [VECr 0]: vhost: move tracing out of processing loop

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43542 <https:////gerrit.fd.io/r/c/vpp/+/43542>`_ [VECr 8]: vlib: add possibility to disable pager
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VECr 14]: stats: show raw value in show stat segment
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VECr 20]: build: Add VPP_MAX_WORKERS configure option

vpp: **Dave Barach** <vpp@barachs.net>
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VECr 21]: misc: add error message in case of OOM or panic

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 8]: vppinfra: add ARM neoverse-v2 support
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VECr 21]: misc: add error message in case of OOM or panic

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 102]: tm: add 'mark_flow' action for traffic management

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [vEC 28]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `42599 <https:////gerrit.fd.io/r/c/vpp/+/42599>`_ [veC 151]: WIP pvti: additional tests + fixes Change-Id: Id5ec994928bd757d395e61c464ee6341c1f6272d
  | `42192 <https:////gerrit.fd.io/r/c/vpp/+/42192>`_ [veC 161]: WIP: the tests which fail with a FIPS version of openssl

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [Vec 35]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 56]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 57]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 90]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 85]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 100]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [VEc 2]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `36770 <https:////gerrit.fd.io/r/c/vpp/+/36770>`_ [VEc 5]: vppinfra: force cpu time sync when difference is too big
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 75]: session: fix parse_uri() usage

**Changbin Park** <gh4ck3r@gmail.com>:

  | `43386 <https:////gerrit.fd.io/r/c/vpp/+/43386>`_ [VEc 0]: tcp: handle SYN while CLOSED state

**Damjan Marion** <dmarion@0xa5.net>:

  | `43637 <https:////gerrit.fd.io/r/c/vpp/+/43637>`_ [vEc 0]: dev: add option to assign one rx and one tx queue per thread

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 173]: ip: mark ipX_header_t and ip4_address_t as packed

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 126]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 142]: ip:fix pmtu next node index errror, it should use own value

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43595 <https:////gerrit.fd.io/r/c/vpp/+/43595>`_ [vEc 6]: capo: Calico Policies plugin
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VeC 42]: cnat: converge new cnat implementation to support old usecases (calico)
  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 83]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 96]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `43618 <https:////gerrit.fd.io/r/c/vpp/+/43618>`_ [vEc 5]: ipsec: unify crypto+HMAC in single op for ESP
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 110]: tests: reduce sleep interval in ip-neighbor age test

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 83]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 134]: tests: add send_and_expect_multi

**Maxime Peim** <mpeim@cisco.com>:

  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [vEc 8]: ping: introduce traceroute tool

**Michael Aronovici** <aronovic@cisco.com>:

  | `43439 <https:////gerrit.fd.io/r/c/vpp/+/43439>`_ [vEc 11]: bfd: add API to configure TOS for IP of BFD packets

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 67]: ipip: fix support for ipip6o6 from linux tunnel

**Naveen Joy** <najoy@cisco.com>:

  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VeC 34]: misc: patch to test CI infra changes
  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 98]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Ole Troan** <otroan@employees.org>:

  | `42463 <https:////gerrit.fd.io/r/c/vpp/+/42463>`_ [veC 165]: tests: tests python package and uv venv

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 64]: snort: update VPP DAQ for multi-instance

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 49]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 97]: acl: added hit count logic in VPP for debugging

**Semir Sionek** <ssionek@cisco.com>:

  | `43594 <https:////gerrit.fd.io/r/c/vpp/+/43594>`_ [vEC 0]: hsa: add periodic reports to builtin echo client

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `43015 <https:////gerrit.fd.io/r/c/vpp/+/43015>`_ [VeC 53]: vapi: uds transport pass client index correctly
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VeC 70]: cnat: add vrf awareness

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 104]: tm: add tm framework for hw traffic management

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [veC 154]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 148]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 70]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 72]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 72]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 90]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 121]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 155]: nat: speedup nat44-ed vrf table lookups
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 156]: fib: fix fib entry tracking crash on table remove

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 119]: ip-neighbor: ARP/NA per-interface counter improvements

**Yoann Desmouceaux** <ydesmouc@cisco.com>:

  | `43282 <https:////gerrit.fd.io/r/c/vpp/+/43282>`_ [VeC 62]: svm: fix includes for musl

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 103]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**chenxk** <case2111@163.com>:

  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VeC 31]: dispatch-trace: fix crash issues caused by buffer-trace

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 99]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 103]: Makefile: Added support for the Wind River eLxr distribution

**shaohui jin** <jinshaohui789@163.com>:

  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [veC 173]: dhcp:dhcp request packets always use the first server address.
  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [veC 173]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.

**steven luong** <sluong@cisco.com>:

  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 18]: session: refactoring application_local.c
  | `42178 <https:////gerrit.fd.io/r/c/vpp/+/42178>`_ [veC 165]: af_xdp: add option to support checksum, multi-buffer, and show af_xdp stats

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 110]: snort: fix crash when using an output interface

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 51]: ethernet: fix mac mismatch in promisc mode

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [A 180]: geneve: add support for layer 3

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
authors          60
maintainers      20
committers       0
abandoned        1
================ ===

