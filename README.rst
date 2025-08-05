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
generated on Tuesday 2025-08-05, 16:47:52
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

  | `43523 <https:////gerrit.fd.io/r/c/vpp/+/43523>`_ [VECR 0]: http: h2 client tunnel fix
  | `43473 <https:////gerrit.fd.io/r/c/vpp/+/43473>`_ [VECR 0]: session: enable sending segmented dgrams
  | `43388 <https:////gerrit.fd.io/r/c/vpp/+/43388>`_ [VECR 1]: hs-test: load k8s pod definitions from a file

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `43371 <https:////gerrit.fd.io/r/c/vpp/+/43371>`_ [VECr 0]: af_xdp: fix missing recvmsg argument

bonding: **Steven Luong** <sluong@cisco.com>
  | `43520 <https:////gerrit.fd.io/r/c/vpp/+/43520>`_ [VECr 0]: bonding: capture rx packets before ethernet-input node.

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 20]: cnat: converge new cnat implementation to support old usecases (calico)

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `43481 <https:////gerrit.fd.io/r/c/vpp/+/43481>`_ [VECr 10]: dispatch-trace: fix crash issues caused by buffer-trace

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `42876 <https:////gerrit.fd.io/r/c/vpp/+/42876>`_ [VECr 7]: gso: add support for ipip tso for phyiscal interfaces

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `43357 <https:////gerrit.fd.io/r/c/vpp/+/43357>`_ [VECr 30]: ethernet: fix mac mismatch in promisc mode

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `42876 <https:////gerrit.fd.io/r/c/vpp/+/42876>`_ [VECr 7]: gso: add support for ipip tso for phyiscal interfaces

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `43447 <https:////gerrit.fd.io/r/c/vpp/+/43447>`_ [VECr 0]: hsa: show tx/rx stats for UDP on timeout and fix test-bytes for UDP

interface: **Dave Barach** <vpp@barachs.net>
  | `42876 <https:////gerrit.fd.io/r/c/vpp/+/42876>`_ [VECr 7]: gso: add support for ipip tso for phyiscal interfaces
  | `43435 <https:////gerrit.fd.io/r/c/vpp/+/43435>`_ [VECr 8]: dispatch-trace: add offload flags to trace

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `43507 <https:////gerrit.fd.io/r/c/vpp/+/43507>`_ [VECr 4]: ip: reassembly - enable registering custom next nodes for v6

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `43508 <https:////gerrit.fd.io/r/c/vpp/+/43508>`_ [VECr 4]: vnet: install full reassembly headers

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `43359 <https:////gerrit.fd.io/r/c/vpp/+/43359>`_ [VECr 28]: nat: fix two problems in hairpin NAT scenario 1. Add source port information to nat44-ed o2i flow's rewrite. 2. Rewrite tx_fib_index when hairpin traffic crosses VRFs.

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 5]: ping: add option to specify interface src-address

tcp: **Florin Coras** <fcoras@cisco.com>
  | `43386 <https:////gerrit.fd.io/r/c/vpp/+/43386>`_ [VECr 1]: tcp: handle SYN while CLOSED state

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `43500 <https:////gerrit.fd.io/r/c/vpp/+/43500>`_ [VECr 5]: ping: add option to specify interface src-address
  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VECr 20]: cnat: converge new cnat implementation to support old usecases (calico)

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `43516 <https:////gerrit.fd.io/r/c/vpp/+/43516>`_ [VECr 1]: tls: fix coverity warning

vcl: **Florin Coras** <fcoras@cisco.com>
  | `42380 <https:////gerrit.fd.io/r/c/vpp/+/42380>`_ [VECr 0]: misc: patch to test CI infra changes
  | `42376 <https:////gerrit.fd.io/r/c/vpp/+/42376>`_ [VECr 13]: misc: patch to test CI infra changes

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `43377 <https:////gerrit.fd.io/r/c/vpp/+/43377>`_ [VECr 28]: vppinfra: fix cpu time on riscv

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alok Mishra** <almishra@marvell.com>:

  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [veC 81]: tm: add 'mark_flow' action for traffic management

**Andrew Lunn** <andrew@lunn.ch>:

  | `42195 <https:////gerrit.fd.io/r/c/vpp/+/42195>`_ [VeC 159]: ip6-nd: Punt RS to LCP if not locally answered
  | `42194 <https:////gerrit.fd.io/r/c/vpp/+/42194>`_ [VeC 159]: ip6-nd: Adjust length once decided to reply to RS
  | `42416 <https:////gerrit.fd.io/r/c/vpp/+/42416>`_ [VeC 159]: ip6-nd: Fix stylecheck

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `43258 <https:////gerrit.fd.io/r/c/vpp/+/43258>`_ [vEC 0]: gpcapng: first draft
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [vEC 7]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `42599 <https:////gerrit.fd.io/r/c/vpp/+/42599>`_ [veC 129]: WIP pvti: additional tests + fixes Change-Id: Id5ec994928bd757d395e61c464ee6341c1f6272d
  | `42192 <https:////gerrit.fd.io/r/c/vpp/+/42192>`_ [veC 140]: WIP: the tests which fail with a FIPS version of openssl

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43461 <https:////gerrit.fd.io/r/c/vpp/+/43461>`_ [VEc 13]: lacp: optionally move lacp tx to the worker ( not vpp_main)
  | `43358 <https:////gerrit.fd.io/r/c/vpp/+/43358>`_ [VeC 35]: lacp: handle lacp input fsm in vpp_main; handle bond change state operations without traffic ( between barrier_sync..  barrier_release)
  | `43281 <https:////gerrit.fd.io/r/c/vpp/+/43281>`_ [Vec 36]: l2: l2_flood-clone whole buffers
  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [veC 69]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [Vec 64]: cnat: fix udp checksum calculation
  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 78]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `42480 <https:////gerrit.fd.io/r/c/vpp/+/42480>`_ [vEC 0]: misc: add error message in case of OOM or panic
  | `42911 <https:////gerrit.fd.io/r/c/vpp/+/42911>`_ [vec 54]: session: fix parse_uri() usage

**Dmitrii Anufriev** <dmitry-anufriev@yandex.ru>:

  | `42164 <https:////gerrit.fd.io/r/c/vpp/+/42164>`_ [VeC 179]: stats: prometheus_export fixes and improvements.

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 152]: ip: mark ipX_header_t and ip4_address_t as packed

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `42784 <https:////gerrit.fd.io/r/c/vpp/+/42784>`_ [VeC 105]: feature: embed data lengths in feat cfg strings

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `42594 <https:////gerrit.fd.io/r/c/vpp/+/42594>`_ [VeC 121]: ip:fix pmtu next node index errror, it should use own value

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43073 <https:////gerrit.fd.io/r/c/vpp/+/43073>`_ [VeC 62]: cnat: fix cnat when there is an encapsulation
  | `43003 <https:////gerrit.fd.io/r/c/vpp/+/43003>`_ [VeC 75]: cnat: delete sessions when translations are updated

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 89]: tests: reduce sleep interval in ip-neighbor age test

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 50]: vppinfra: add ARM neoverse-v2 support

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [veC 62]: vppapigen: fix json build error

**Klement Sekera** <klement.sekera@gmail.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VeC 113]: tests: add send_and_expect_multi

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 174]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 174]: docs: Add doc for API Trace Tools

**Michael Aronovici** <aronovic@cisco.com>:

  | `43439 <https:////gerrit.fd.io/r/c/vpp/+/43439>`_ [vEc 11]: bfd: add API to configure TOS for IP of BFD packets

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 177]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 45]: ipip: fix support for ipip6o6 from linux tunnel
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [vec 159]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `42966 <https:////gerrit.fd.io/r/c/vpp/+/42966>`_ [VeC 76]: tests: ipip checksum offload interface tests for IPv4 tunnels

**Ole Troan** <otroan@employees.org>:

  | `42463 <https:////gerrit.fd.io/r/c/vpp/+/42463>`_ [veC 144]: tests: tests python package and uv venv

**Pierre Pfister** <ppfister@cisco.com>:

  | `42032 <https:////gerrit.fd.io/r/c/vpp/+/42032>`_ [veC 168]: clib: add full simulated time support

**Robin Shapley** <robin.shapley@arm.com>:

  | `43184 <https:////gerrit.fd.io/r/c/vpp/+/43184>`_ [VeC 42]: snort: update VPP DAQ for multi-instance

**Sanjyot Vaidya** <sanjyot.vaidya@arm.com>:

  | `42983 <https:////gerrit.fd.io/r/c/vpp/+/42983>`_ [vec 76]: acl: added hit count logic in VPP for debugging

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `43015 <https:////gerrit.fd.io/r/c/vpp/+/43015>`_ [VeC 32]: vapi: uds transport pass client index correctly
  | `42931 <https:////gerrit.fd.io/r/c/vpp/+/42931>`_ [VeC 49]: cnat: add vrf awareness

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VeC 83]: tm: add tm framework for hw traffic management

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [veC 132]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 127]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 49]: fib: avoid loadbalance dpo node path polarisation
  | `43181 <https:////gerrit.fd.io/r/c/vpp/+/43181>`_ [VeC 50]: fib: set the value of the sw_if_index for NULL route
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VeC 50]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 69]: vlib: mark cli quit command as mp_safe
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [Vec 100]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 134]: nat: speedup nat44-ed vrf table lookups
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 134]: fib: fix fib entry tracking crash on table remove

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 97]: ip-neighbor: ARP/NA per-interface counter improvements

**Yoann Desmouceaux** <ydesmouc@cisco.com>:

  | `43282 <https:////gerrit.fd.io/r/c/vpp/+/43282>`_ [VeC 41]: svm: fix includes for musl

**bsoares.it@gmail.com** <bsoares.it@gmail.com>:

  | `42944 <https:////gerrit.fd.io/r/c/vpp/+/42944>`_ [Vec 82]: vhost: add full_tx_queue_placement option for vhost-user interfaces

**echo** <614699596@qq.com>:

  | `41994 <https:////gerrit.fd.io/r/c/vpp/+/41994>`_ [VeC 160]: af_packet: fix crash on af_packet_fd_error

**lei feng** <1579628578@qq.com>:

  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [Vec 78]: docs: Python apis examples

**mjbenz** <michael.benz@windriver.com>:

  | `42969 <https:////gerrit.fd.io/r/c/vpp/+/42969>`_ [veC 81]: Makefile: Added support for the Wind River eLxr distribution

**shaohui jin** <jinshaohui789@163.com>:

  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [veC 151]: dhcp:dhcp request packets always use the first server address.
  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [veC 151]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.

**steven luong** <sluong@cisco.com>:

  | `43425 <https:////gerrit.fd.io/r/c/vpp/+/43425>`_ [vEC 0]: af_xdp: processing free buffer
  | `43475 <https:////gerrit.fd.io/r/c/vpp/+/43475>`_ [vEC 0]: af_xdp: bump xdp-tools to 1.5.5
  | `43138 <https:////gerrit.fd.io/r/c/vpp/+/43138>`_ [VEc 7]: session: refactoring application_local.c
  | `42178 <https:////gerrit.fd.io/r/c/vpp/+/42178>`_ [veC 143]: af_xdp: add option to support checksum, multi-buffer, and show af_xdp stats

**yoan picchi** <yoan.picchi@arm.com>:

  | `42916 <https:////gerrit.fd.io/r/c/vpp/+/42916>`_ [VeC 89]: snort: fix crash when using an output interface

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `42182 <https:////gerrit.fd.io/r/c/vpp/+/42182>`_ [A 193]: tests: replace the multiprocessing queue with socket-based mechanism
  | `41914 <https:////gerrit.fd.io/r/c/vpp/+/41914>`_ [A 207]: pvti: add a doc with write-up, and fix CLI help
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [A 316]: TEST: remove a DVR test on 22.04

**Animesh Patel** <sbg.github.anipatel@cisco.com>:

  | `42312 <https:////gerrit.fd.io/r/c/vpp/+/42312>`_ [A 180]: docs: vl_msg_api_alloc_internal improved to provide consistent behavior

**Dau Do** <daudo@yahoo.com>:

  | `41966 <https:////gerrit.fd.io/r/c/vpp/+/41966>`_ [A 203]: classify: add options to filter out the geneve packets
  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [A 302]: memif: add support for per queue counters

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [A 298]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [A 298]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [A 335]: vppapigen: fix enum format function

**Florian Larysch** <fl@n621.de>:

  | `41961 <https:////gerrit.fd.io/r/c/vpp/+/41961>`_ [A 241]: build: fix PATH with multiple /usr/lib* matches

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41985 <https:////gerrit.fd.io/r/c/vpp/+/41985>`_ [A 238]: api: fix crash in pcap capture api

**Jay Wang** <jay.wang2@arm.com>:

  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [A 210]: vlib: fix seed parse error

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [A 207]: linux-cp: Add VRF synchronization

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [A 295]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [A 328]: api-trace: enable both rx and tx direction

**Matthew Smith** <mgsmith@netgate.com>:

  | `42123 <https:////gerrit.fd.io/r/c/vpp/+/42123>`_ [A 207]: ip: skip options handling for locally originated packets

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [A 312]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [A 314]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [A 316]: vlib: add vfio-token parsing support

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [A 224]: ping: Allow to specify a source interface in ping binary API

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [A 292]: ip6: don't forward packets with invalid source address

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [A 336]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [A 336]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [A 336]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [A 336]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [A 337]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [A 337]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [A 337]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [A 337]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [A 337]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [A 337]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [A 337]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [A 337]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [A 337]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [A 186]: build: Add VPP_MAX_WORKERS configure option

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [A 201]: stats: add sw interface tags to statseg
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [A 201]: stats: add interface link speed to statseg
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [A 251]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [A 251]: fib: fix udp encap mp-safe ops and id validation
  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [A 298]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [A 301]: nat: add nat44-ed session filtering by fib table
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [A 308]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [A 308]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [A 308]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [A 308]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [A 308]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [A 308]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [A 308]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [A 308]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [A 308]: fib: ensure mpls dpo index is valid for its next node

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [A 309]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [A 315]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [A 328]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [A 312]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `42040 <https:////gerrit.fd.io/r/c/vpp/+/42040>`_ [A 193]: docs: add examples for VXLAN tunnel
  | `42039 <https:////gerrit.fd.io/r/c/vpp/+/42039>`_ [A 193]: docs: add examples for GRE teb tunnel
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [A 203]: dns: support ipv6 server to resolve name
  | `42074 <https:////gerrit.fd.io/r/c/vpp/+/42074>`_ [A 206]: dns: dns api, cli and vat resolve interface implements
  | `42110 <https:////gerrit.fd.io/r/c/vpp/+/42110>`_ [A 208]: dev: add cli show dev class
  | `42072 <https:////gerrit.fd.io/r/c/vpp/+/42072>`_ [A 210]: dns: dns resolution optimisation and bug fixes
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [A 230]: dns: did't shall resolve before enable
  | `42034 <https:////gerrit.fd.io/r/c/vpp/+/42034>`_ [A 231]: classify: cli filter support for dynamic delete
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [A 257]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [A 258]: svm: fix check bitmap logic error

**sonsumin** <itoodo12@gmail.com>:

  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [A 282]: nat: refactor argument order for nat44-ed static mapping
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [A 307]: refactor(nat44): change argument order and parsing format for static mapping

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
authors          62
maintainers      17
committers       3
abandoned        66
================ ===

