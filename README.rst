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
generated on Saturday 2022-12-10, 02:20:03
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

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECR 7]: srv6-mobile: Implement SRv6 mobile API funcs

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VECr 17]: acl: change the algorithm for cleaning the sessions from purgatory

build: **Damjan Marion** <damarion@cisco.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 7]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 17]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VECr 17]: classify: fix classify session cli.

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 4]: ipsec: add per-SA error counters
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 4]: pci: add option to force uio binding
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 7]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 7]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 0]: vxlan: convert vxlan to a plugin
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 4]: pci: add option to force uio binding

fib: **Neale Ranns** <neale@graphiant.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 7]: ip_session_redirect: add session redirect plugin

interface: **Dave Barach** <vpp@barachs.net>
  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VECr 4]: vppapigen: enable codegen for stream message types
  | `37666 <https:////gerrit.fd.io/r/c/vpp/+/37666>`_ [VECr 23]: interface: fix format_vnet_interface_output_trace
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VECr 30]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37690 <https:////gerrit.fd.io/r/c/vpp/+/37690>`_ [VECr 4]: ip: fix ip ACL traces

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 4]: ipsec: add per-SA error counters
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 21]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `37786 <https:////gerrit.fd.io/r/c/vpp/+/37786>`_ [VECr 0]: linux-cp: set severity of noisy message to debug

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 0]: vxlan: convert vxlan to a plugin
  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VECr 1]: stats: fix memory leak in stat_segment_dump_r()
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 7]: ip_session_redirect: add session redirect plugin
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 7]: fateshare: a plugin for managing child processes

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37788 <https:////gerrit.fd.io/r/c/vpp/+/37788>`_ [VECr 0]: nat: fix accidental o2i deletion/reuse
  | `37746 <https:////gerrit.fd.io/r/c/vpp/+/37746>`_ [VECr 5]: nat: disable nat44-ed/ei features on interface deletion
  | `37745 <https:////gerrit.fd.io/r/c/vpp/+/37745>`_ [VECr 6]: nat: fix incorrect using about sw_if_index in nat44-ed static mapping v2 api.
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 11]: nat: fix nat44_ed set_session_limit crash
  | `37683 <https:////gerrit.fd.io/r/c/vpp/+/37683>`_ [VECr 12]: nat: fix memory leak and refactor nat44-ed db init/free.
  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [VECr 13]: nat: make nat44 session limit api reinit flow_hash with new buckets.

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [VECr 0]: vxlan: convert vxlan to a plugin

pci: **Damjan Marion** <damarion@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 4]: pci: add option to force uio binding

policer: **Neale Ranns** <neale@graphiant.com>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 17]: policer: fix crash when delete interface policer classify.

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `37779 <https:////gerrit.fd.io/r/c/vpp/+/37779>`_ [VECr 1]: pppoe: fix memcpy out of bounds with gcc-11 on arm

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37788 <https:////gerrit.fd.io/r/c/vpp/+/37788>`_ [VECr 0]: nat: fix accidental o2i deletion/reuse
  | `37672 <https:////gerrit.fd.io/r/c/vpp/+/37672>`_ [VECr 4]: ipsec: fix SA names consistency in tests
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 4]: ipsec: add per-SA error counters
  | `37746 <https:////gerrit.fd.io/r/c/vpp/+/37746>`_ [VECr 5]: nat: disable nat44-ed/ei features on interface deletion
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 7]: ip_session_redirect: add session redirect plugin
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 11]: nat: fix nat44_ed set_session_limit crash
  | `37268 <https:////gerrit.fd.io/r/c/vpp/+/37268>`_ [VECr 15]: lb: add source ip based sticky load balancing
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 21]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation
  | `37654 <https:////gerrit.fd.io/r/c/vpp/+/37654>`_ [VECr 25]: tests: improve packet checksum functions

vapi: **Ole Troan** <ot@cisco.com>
  | `37787 <https:////gerrit.fd.io/r/c/vpp/+/37787>`_ [VECr 0]: vapi: implement vapi_wait() for reads

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 17]: misc: patch to test CI infra changes

virtio: **Mohsin Kazmi** <sykazmi@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37416 <https:////gerrit.fd.io/r/c/vpp/+/37416>`_ [VECr 4]: virtio: add option to bind interface to uio driver

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37777 <https:////gerrit.fd.io/r/c/vpp/+/37777>`_ [VECr 1]: stats: fix node name compare error when updating stats segment
  | `37776 <https:////gerrit.fd.io/r/c/vpp/+/37776>`_ [VECr 1]: vlib: fix macro define command not work in startup config exec script
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 4]: pci: add option to force uio binding
  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [VECr 4]: vlib: avoid non-mp-safe cli process node updates
  | `37691 <https:////gerrit.fd.io/r/c/vpp/+/37691>`_ [VECr 16]: vlib: fix vlib_log for elog

vmxnet3: **Steven Luong** <sluong@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 4]: pci: add option to force uio binding

vppapigen: **Ole Troan** <otroan@employees.org>
  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VECr 4]: vppapigen: enable codegen for stream message types

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37763 <https:////gerrit.fd.io/r/c/vpp/+/37763>`_ [VECr 0]: wireguard: add local variable
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 95]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 98]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VEc 0]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `31368 <https:////gerrit.fd.io/r/c/vpp/+/31368>`_ [Vec 170]: vlib: Sleep less in unix input if there were active signals recently

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37059 <https:////gerrit.fd.io/r/c/vpp/+/37059>`_ [VEc 4]: ipsec: new api for sa ips and ports updates
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 23]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 94]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `37742 <https:////gerrit.fd.io/r/c/vpp/+/37742>`_ [vEC 7]: nat: do not use nat session object after deletion
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 59]: build: add sanitizer option to configure script

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `36705 <https:////gerrit.fd.io/r/c/vpp/+/36705>`_ [VeC 134]: ip-neighbor: Fixed delay(1~2s) in neighbor-probe interval

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 97]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37767 <https:////gerrit.fd.io/r/c/vpp/+/37767>`_ [vEC 2]: build: don't overwrite quicly build/install logs
  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [VEc 22]: tests: remove intermittent failing tests on vpp_debug image

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 56]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 44]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 44]: nat: nat44-ed update timeout api
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 44]: nat: nat66 cli bug fix
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 44]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 44]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 44]: nat: nat64 fix add_del calls requirements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [VEc 0]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 44]: nat: nat44-ed get out2in workers failed for static mapping without port

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 73]: urpf: add show urpf cli
  | `34726 <https:////gerrit.fd.io/r/c/vpp/+/34726>`_ [VeC 126]: interface: add buffer stats api

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [VEc 6]: nat: fix crash when set nat44 session limit with nonexisted vrf.

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `36592 <https:////gerrit.fd.io/r/c/vpp/+/36592>`_ [VeC 157]: stats: handle interface renames properly
  | `36590 <https:////gerrit.fd.io/r/c/vpp/+/36590>`_ [VeC 157]: nat: fix handling checksum offload in nat44-ed

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 44]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 44]: nat: fix nat44-ed API
  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 100]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 62]: memif: fix uninitialized variable warning

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37073 <https:////gerrit.fd.io/r/c/vpp/+/37073>`_ [veC 95]: ip neighbor: fix debug log format output

**Mercury Noah** <mercury124185@gmail.com>:

  | `36492 <https:////gerrit.fd.io/r/c/vpp/+/36492>`_ [VeC 168]: ip6-nd: fix ip6-nd proxy issue

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [VEc 3]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 44]: nat: fix tcp session reopen in nat44-ed

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 58]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 64]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 70]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 70]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 70]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 70]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 70]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 70]: cnat: flag to disable rsession
  | `35805 <https:////gerrit.fd.io/r/c/vpp/+/35805>`_ [VeC 70]: dpdk: add intf tag to dev{} subinput
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 70]: memif: add support for ns abstract sockets
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VeC 144]: memif: autogenerate socket_ids

**Naveen Joy** <najoy@cisco.com>:

  | `37374 <https:////gerrit.fd.io/r/c/vpp/+/37374>`_ [VEc 21]: tests: tapv2, tunv2 and af_packet interface tests for vpp

**Neale Ranns** <neale@graphiant.com>:

  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 120]: vlib: "sh errors" shows error severity counters

**Ole Troan** <otroan@employees.org>:

  | `37766 <https:////gerrit.fd.io/r/c/vpp/+/37766>`_ [vEC 1]: papi: vla list of fixed strings

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `37678 <https:////gerrit.fd.io/r/c/vpp/+/37678>`_ [VEc 21]: fib: partial fix to a deadlock during CSIT tests execution

**RADHA KRISHNA SARAGADAM** <krishna_srk2003@yahoo.com>:

  | `36711 <https:////gerrit.fd.io/r/c/vpp/+/36711>`_ [Vec 136]: ebuild: upgrade vagrant ubuntu version to 20.04

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 44]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 95]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 108]: ip6-nd: add fixed flag

**Ted Chen** <znscnchen@gmail.com>:

  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VeC 44]: nat: fix the wrong unformat type
  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 71]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 83]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vec 42]: dpdk: fix interface name w/ the same PCI bus/slot/function
  | `36488 <https:////gerrit.fd.io/r/c/vpp/+/36488>`_ [VeC 165]: tests: fix wireguard test failure under heavy load

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 44]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 44]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VeC 44]: nat: fix nat44-ed outside address distribution
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 72]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 78]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 78]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 86]: avf: tolerate socket events in avf_process_request
  | `27972 <https:////gerrit.fd.io/r/c/vpp/+/27972>`_ [VeC 163]: sr: Fix deletion if target SR list is not found
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 163]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [VEc 13]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 44]: nat: auto forward inbound packet for local server session app with snat
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 49]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 54]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 61]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 62]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 102]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 119]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 120]: cjson: json realloced output truncated if actual lenght more then 256

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 99]: ip: fixup crash when reassemble a lots of fragments.

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [vEC 7]: af_xdp: optimizing send performance
  | `37274 <https:////gerrit.fd.io/r/c/vpp/+/37274>`_ [Vec 49]: af_xdp: fix xdp socket create fail

**Yong Liu** <yong.liu@intel.com>:

  | `37731 <https:////gerrit.fd.io/r/c/vpp/+/37731>`_ [vEC 10]: memif: support dma option
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VeC 35]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VeC 35]: dma_intel: add native dsa device driver
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VeC 35]: vlib: support dma map extended memory

**ai hua** <51931196@qq.com>:

  | `37498 <https:////gerrit.fd.io/r/c/vpp/+/37498>`_ [VeC 46]: vppinfra:fix pcap write large file(> 0x80000000) error.

**f00182600** <fangtong2007@163.com>:

  | `36453 <https:////gerrit.fd.io/r/c/vpp/+/36453>`_ [veC 158]: interface: fix the issue of show hardware-interface with invalid if-idx can caused vpp crash.
  | `35963 <https:////gerrit.fd.io/r/c/vpp/+/35963>`_ [veC 176]: dns: fix the isssue of memory leak.
  | `35862 <https:////gerrit.fd.io/r/c/vpp/+/35862>`_ [VeC 176]: nat: Delete the operation of repeatedly releasing Nat44 ei port resources

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 85]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [VEc 24]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [VEc 27]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [vEC 12]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 32]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [Vec 44]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 58]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 123]: bonding: Add failover-mac active support

**xujunjie-cover** <xujunjielxx@163.com>:

  | `36494 <https:////gerrit.fd.io/r/c/vpp/+/36494>`_ [VeC 165]: lb: fix make l4 lb function work

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
authors          97
maintainers      34
committers       1
abandoned        0
================ ===

