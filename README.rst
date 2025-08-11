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
generated on Monday 2025-08-11, 03:13:20
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
  | `43371 <https:////gerrit.fd.io/r/c/vpp/+/43371>`_ [VECr 4]: af_xdp: fix missing recvmsg argument

bonding: **Steven Luong** <sluong@cisco.com>
  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VECr 5]: bonding: capture rx packets before ethernet-input node.

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 26]: cnat: converge new cnat implementation to support old usecases (calico)

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VECr 15]: dispatch-trace: fix crash issues caused by buffer-trace

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 3]: gpcapng: first draft

ebuild: **Dave Barach** <vpp@barachs.net>
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VECr 4]: build: Add VPP_MAX_WORKERS configure option

interface: **Dave Barach** <vpp@barachs.net>
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VECr 13]: dispatch-trace: add offload flags to trace

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `43507 <https:////gerrit.fd.io/r/c/vpp/+/43507>`_ [VECr 0]: ip: reassembly - enable registering custom next nodes for v6

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 3]: gpcapng: first draft
  | `43508 <https:////gerrit.fd.io/r/c/vpp/+/43508>`_ [VECr 9]: vnet: install full reassembly headers

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 10]: ping: add option to specify interface src-address

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [VECr 3]: gpcapng: first draft
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 10]: ping: add option to specify interface src-address
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 26]: cnat: converge new cnat implementation to support old usecases (calico)

vcl: **Florin Coras** <fcoras@cisco.com>
  | `42380 <https:////gerrit.fd.io/r/c/vpp/+/42380>`_ [VECr 6]: misc: patch to test CI infra changes
  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VECr 18]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VECr 4]: build: Add VPP_MAX_WORKERS configure option

vpp: **Dave Barach** <vpp@barachs.net>
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VECr 5]: misc: add error message in case of OOM or panic

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [VECr 5]: misc: add error message in case of OOM or panic

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 86]: tm: add 'mark_flow' action for traffic management

**Andrew Lunn** <andrew@lunn.ch>:

  | `42195 <https:////gerrit.fd.io/r/c/vpp/+/42195>`_ [VeC 165]: ip6-nd: Punt RS to LCP if not locally answered
  | `42194 <https:////gerrit.fd.io/r/c/vpp/+/42194>`_ [VeC 165]: ip6-nd: Adjust length once decided to reply to RS
  | `42416 <https:////gerrit.fd.io/r/c/vpp/+/42416>`_ [VeC 165]: ip6-nd: Fix stylecheck

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [vEC 12]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `42599 <https:////gerrit.fd.io/r/c/vpp/+/42599>`_ [veC 135]: WIP pvti: additional tests + fixes Change-Id: Id5ec994928bd757d395e61c464ee6341c1f6272d
  | `42192 <https:////gerrit.fd.io/r/c/vpp/+/42192>`_ [veC 145]: WIP: the tests which fail with a FIPS version of openssl

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [VEc 19]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 40]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 41]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 74]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 69]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 84]: pnat: do not disable pnat on rule deletion

**Benison Technologies** <benison@benisontech.com>:

  | `43527 <https:////gerrit.fd.io/r/c/vpp/+/43527>`_ [vEC 3]: ipsec: handoff and vlan fixes ipsec - AH

**Benoît Ganne** <bganne@cisco.com>:

  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 59]: session: fix parse_uri() usage

**Changbin Park** <gh4ck3r@gmail.com>:

  | `43386 <https:////gerrit.fd.io/r/c/vpp/+/43386>`_ [VEc 3]: tcp: handle SYN while CLOSED state

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 157]: ip: mark ipX_header_t and ip4_address_t as packed

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 110]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 126]: ip:fix pmtu next node index errror, it should use own value

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 67]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 80]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 95]: tests: reduce sleep interval in ip-neighbor age test

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 55]: vppinfra: add ARM neoverse-v2 support

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 67]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 118]: tests: add send_and_expect_multi

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 179]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 179]: docs: Add doc for API Trace Tools

**Michael Aronovici** <aronovic@cisco.com>:

  | `43439 <https:////gerrit.fd.io/r/c/vpp/+/43439>`_ [vEc 16]: bfd: add API to configure TOS for IP of BFD packets

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 51]: ipip: fix support for ipip6o6 from linux tunnel
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [vec 164]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 82]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Ole Troan** <otroan@employees.org>:

  | `42463 <https:////gerrit.fd.io/r/c/vpp/+/42463>`_ [veC 149]: tests: tests python package and uv venv

**Pierre Pfister** <ppfister@cisco.com>:

  | `42032 <https:////gerrit.fd.io/r/c/vpp/+/42032>`_ [veC 173]: clib: add full simulated time support

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 48]: snort: update VPP DAQ for multi-instance

**Rock Go** <guozhenqiangg@qq.com>:

  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VeC 33]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 81]: acl: added hit count logic in VPP for debugging

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `43015 <https:////gerrit.fd.io/r/c/vpp/+/43015>`_ [VeC 37]: vapi: uds transport pass client index correctly
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VeC 54]: cnat: add vrf awareness

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 88]: tm: add tm framework for hw traffic management

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [veC 138]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 132]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 54]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 56]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 56]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 74]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 105]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 139]: nat: speedup nat44-ed vrf table lookups
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 140]: fib: fix fib entry tracking crash on table remove

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 103]: ip-neighbor: ARP/NA per-interface counter improvements

**Yoann Desmouceaux** <ydesmouc@cisco.com>:

  | `43282 <https:////gerrit.fd.io/r/c/vpp/+/43282>`_ [VeC 46]: svm: fix includes for musl

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 87]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**echo** <614699596@qq.com>:

  | `41994 <https:////gerrit.fd.io/r/c/vpp/+/41994>`_ [VeC 165]: af_packet: fix crash on af_packet_fd_error

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 83]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 87]: Makefile: Added support for the Wind River eLxr distribution

**shaohui jin** <jinshaohui789@163.com>:

  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [veC 157]: dhcp:dhcp request packets always use the first server address.
  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [veC 157]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.

**steven luong** <sluong@cisco.com>:

  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 2]: session: refactoring application_local.c
  | `42178 <https:////gerrit.fd.io/r/c/vpp/+/42178>`_ [veC 149]: af_xdp: add option to support checksum, multi-buffer, and show af_xdp stats

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 94]: snort: fix crash when using an output interface

**yu lintao** <oopsadm@gmail.com>:

  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VeC 35]: ethernet: fix mac mismatch in promisc mode

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
maintainers      13
committers       0
abandoned        0
================ ===

