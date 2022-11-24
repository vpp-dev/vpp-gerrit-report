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
generated on Thursday 2022-11-24, 02:37:14
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

  | `37516 <https:////gerrit.fd.io/r/c/vpp/+/37516>`_ [VECR 2]: ipsec: remove redundant policy array in fast path spd

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VECr 1]: acl: change the algorithm for cleaning the sessions from purgatory

classify: **Dave Barach** <vpp@barachs.net>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 1]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VECr 1]: classify: fix classify session cli.

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [VECr 26]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 2]: ipsec: add per-SA error counters

devices: **Damjan Marion** <damarion@cisco.com>
  | `37674 <https:////gerrit.fd.io/r/c/vpp/+/37674>`_ [VECr 5]: interface: remove the pending interrupt from deleting interface

dma_intel: **Marvin Liu** <yong.liu@intel.com>
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VECr 19]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 19]: dma_intel: add native dsa device driver

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin

fib: **Neale Ranns** <neale@graphiant.com>
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 28]: nat: fix nat44-ed outside address selection

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `37687 <https:////gerrit.fd.io/r/c/vpp/+/37687>`_ [VECr 0]: hs-test: auto register test actions

interface: **Dave Barach** <vpp@barachs.net>
  | `37674 <https:////gerrit.fd.io/r/c/vpp/+/37674>`_ [VECr 5]: interface: remove the pending interrupt from deleting interface
  | `37666 <https:////gerrit.fd.io/r/c/vpp/+/37666>`_ [VECr 7]: interface: fix format_vnet_interface_output_trace
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VECr 14]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VECr 1]: arp: fix arp request for ip4-glean node

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37690 <https:////gerrit.fd.io/r/c/vpp/+/37690>`_ [VECr 1]: ip: fix ip ACL traces
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VECr 1]: arp: fix arp request for ip4-glean node
  | `37655 <https:////gerrit.fd.io/r/c/vpp/+/37655>`_ [VECr 9]: vnet: fix trace flag copying in icmp4
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 28]: nat: add nat44-ed session filtering by fib table

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 2]: ipsec: add per-SA error counters
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 5]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 14]: sr: srv6 path tracing api
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37683 <https:////gerrit.fd.io/r/c/vpp/+/37683>`_ [VECr 0]: nat: fix memory leak when config nat44 session limit.
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 28]: nat: nat66 cli bug fix
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VECr 28]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VECr 28]: nat: nat64 fix add_del calls requirements
  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VECr 28]: nat: DET: Allow unknown protocol translation
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 28]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 28]: nat: det44 map configuration improvements + tests
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VECr 28]: nat: auto forward inbound packet for local server session app with snat
  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [VECr 28]: nat: add local addresses correctly in nat lb static mapping
  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VECr 28]: nat: fix the wrong unformat type
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 28]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 28]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 28]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 28]: nat: fix tcp session reopen in nat44-ed
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VECr 28]: nat: fix nat44-ed API
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 28]: nat: nat44-ed get out2in workers failed for static mapping without port

policer: **Neale Ranns** <neale@graphiant.com>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 1]: policer: fix crash when delete interface policer classify.

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 14]: sr: srv6 path tracing api

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 6]: srv6-mobile: Implement SRv6 mobile API funcs

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 2]: ipsec: add per-SA error counters
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 5]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation
  | `37672 <https:////gerrit.fd.io/r/c/vpp/+/37672>`_ [VECr 7]: ipsec: fix SA names consistency in tests
  | `37654 <https:////gerrit.fd.io/r/c/vpp/+/37654>`_ [VECr 9]: tests: improve packet checksum functions
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 16]: ip_session_redirect: add session redirect plugin
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 28]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 28]: nat: det44 map configuration improvements + tests
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 28]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 28]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 28]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 28]: nat: fix tcp session reopen in nat44-ed

udp: **Florin Coras** <fcoras@cisco.com>
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [VECr 2]: udp: hand off packet to right session thread
  | `37680 <https:////gerrit.fd.io/r/c/vpp/+/37680>`_ [VECr 4]: udp: preallocate ports sparse vec map

vapi: **Ole Troan** <ot@cisco.com>
  | `37608 <https:////gerrit.fd.io/r/c/vpp/+/37608>`_ [VECr 14]: vapi: write enumflag types to vapi headers

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 1]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37691 <https:////gerrit.fd.io/r/c/vpp/+/37691>`_ [VECr 0]: vlib: fix vlib_log for elog
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VECr 19]: vlib: support dma map extended memory

vpp: **Dave Barach** <vpp@barachs.net>
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 19]: dma_intel: add native dsa device driver

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37498 <https:////gerrit.fd.io/r/c/vpp/+/37498>`_ [VECr 30]: vppinfra:fix pcap write large file(> 0x80000000) error.

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37518 <https:////gerrit.fd.io/r/c/vpp/+/37518>`_ [VECr 5]: wireguard: compute checksum for outer ipv6 header

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 79]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 82]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `37536 <https:////gerrit.fd.io/r/c/vpp/+/37536>`_ [vEC 28]: misc: VPP 22.10 Release Notes
  | `37129 <https:////gerrit.fd.io/r/c/vpp/+/37129>`_ [VeC 33]: vlib: clib_panic if sysconf() can't determine page size on startup
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [veC 33]: fateshare: a plugin for managing child processes
  | `31368 <https:////gerrit.fd.io/r/c/vpp/+/31368>`_ [Vec 154]: vlib: Sleep less in unix input if there were active signals recently
  | `36377 <https:////gerrit.fd.io/r/c/vpp/+/36377>`_ [VeC 167]: tests: add libmemif tests

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37059 <https:////gerrit.fd.io/r/c/vpp/+/37059>`_ [VEc 6]: ipsec: new api for sa ips and ports updates
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 7]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 78]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VeC 37]: pci: add option to force uio binding
  | `37416 <https:////gerrit.fd.io/r/c/vpp/+/37416>`_ [VeC 40]: virtio: add option to bind interface to uio driver
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 43]: build: add sanitizer option to configure script

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `36705 <https:////gerrit.fd.io/r/c/vpp/+/36705>`_ [VeC 118]: ip-neighbor: Fixed delay(1~2s) in neighbor-probe interval

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 81]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [VEc 6]: tests: remove intermittent failing tests on vpp_debug image

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 40]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <filipvarga89@gmail.com>:

  | `37695 <https:////gerrit.fd.io/r/c/vpp/+/37695>`_ [vEC 0]: nat: fixed return values of enable/disable call

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [vEC 28]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [vEC 28]: nat: nat44-ed update timeout api
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [vEC 28]: nat: det44 map configuration improvements

**Florin Coras** <florin.coras@gmail.com>:

  | `36252 <https:////gerrit.fd.io/r/c/vpp/+/36252>`_ [VeC 177]: svm: multi chunk allocs if requests larger than max chunk

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37361 <https:////gerrit.fd.io/r/c/vpp/+/37361>`_ [VEc 29]: wireguard: add atomic mutex

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 57]: urpf: add show urpf cli
  | `34726 <https:////gerrit.fd.io/r/c/vpp/+/34726>`_ [VeC 110]: interface: add buffer stats api

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `36592 <https:////gerrit.fd.io/r/c/vpp/+/36592>`_ [VeC 141]: stats: handle interface renames properly
  | `36590 <https:////gerrit.fd.io/r/c/vpp/+/36590>`_ [VeC 141]: nat: fix handling checksum offload in nat44-ed

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 84]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 46]: memif: fix uninitialized variable warning

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37073 <https:////gerrit.fd.io/r/c/vpp/+/37073>`_ [veC 79]: ip neighbor: fix debug log format output

**Mercury Noah** <mercury124185@gmail.com>:

  | `36492 <https:////gerrit.fd.io/r/c/vpp/+/36492>`_ [VeC 152]: ip6-nd: fix ip6-nd proxy issue

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 42]: vlib: introduce an inter worker interrupts efds

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 48]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 54]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 54]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 54]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 54]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 54]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 54]: cnat: flag to disable rsession
  | `35805 <https:////gerrit.fd.io/r/c/vpp/+/35805>`_ [VeC 54]: dpdk: add intf tag to dev{} subinput
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 54]: memif: add support for ns abstract sockets
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VeC 128]: memif: autogenerate socket_ids

**Naveen Joy** <najoy@cisco.com>:

  | `37374 <https:////gerrit.fd.io/r/c/vpp/+/37374>`_ [VEc 5]: tests: tapv2, tunv2 and af_packet interface tests for vpp

**Neale Ranns** <neale@graphiant.com>:

  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 104]: vlib: "sh errors" shows error severity counters

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `37268 <https:////gerrit.fd.io/r/c/vpp/+/37268>`_ [vEC 0]: lb: add source ip based sticky load balancing

**Peter Skvarka** <pskvarka@frinx.io>:

  | `30177 <https:////gerrit.fd.io/r/c/vpp/+/30177>`_ [vec 174]: flowprobe: memory leak unreleased frame

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `37678 <https:////gerrit.fd.io/r/c/vpp/+/37678>`_ [VEc 5]: fib: partial fix to a deadlock during CSIT tests execution

**RADHA KRISHNA SARAGADAM** <krishna_srk2003@yahoo.com>:

  | `36711 <https:////gerrit.fd.io/r/c/vpp/+/36711>`_ [Vec 120]: ebuild: upgrade vagrant ubuntu version to 20.04

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VeC 69]: vppapigen: enable codegen for stream message types
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 79]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 92]: ip6-nd: add fixed flag

**Ted Chen** <znscnchen@gmail.com>:

  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 55]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 67]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vEc 26]: dpdk: fix interface name w/ the same PCI bus/slot/function
  | `36488 <https:////gerrit.fd.io/r/c/vpp/+/36488>`_ [VeC 149]: tests: fix wireguard test failure under heavy load

**Ting Xu** <ting.xu@intel.com>:

  | `37563 <https:////gerrit.fd.io/r/c/vpp/+/37563>`_ [vEC 1]: avf: support generic flow

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37315 <https:////gerrit.fd.io/r/c/vpp/+/37315>`_ [VeC 51]: buffers: fix buffer leak on enqueue to bad thread
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 56]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 62]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 62]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 70]: avf: tolerate socket events in avf_process_request
  | `27972 <https:////gerrit.fd.io/r/c/vpp/+/27972>`_ [VeC 147]: sr: Fix deletion if target SR list is not found
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 147]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 33]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 38]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 45]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 46]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 86]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 103]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 104]: cjson: json realloced output truncated if actual lenght more then 256

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 83]: ip: fixup crash when reassemble a lots of fragments.

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [vEC 0]: af_xdp: optimizing send performance
  | `37274 <https:////gerrit.fd.io/r/c/vpp/+/37274>`_ [Vec 33]: af_xdp: fix xdp socket create fail

**f00182600** <fangtong2007@163.com>:

  | `36453 <https:////gerrit.fd.io/r/c/vpp/+/36453>`_ [veC 142]: interface: fix the issue of show hardware-interface with invalid if-idx can caused vpp crash.
  | `35963 <https:////gerrit.fd.io/r/c/vpp/+/35963>`_ [veC 160]: dns: fix the isssue of memory leak.
  | `35862 <https:////gerrit.fd.io/r/c/vpp/+/35862>`_ [VeC 160]: nat: Delete the operation of repeatedly releasing Nat44 ei port resources

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 69]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [VEc 8]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [VEc 11]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [vEC 16]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [VEc 28]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37488 <https:////gerrit.fd.io/r/c/vpp/+/37488>`_ [vEC 8]: vhost: convert vhost device driver to a plugin
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [vEC 9]: vxlan: convert vxlan to a plugin
  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 42]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 107]: bonding: Add failover-mac active support

**xujunjie-cover** <xujunjielxx@163.com>:

  | `36494 <https:////gerrit.fd.io/r/c/vpp/+/36494>`_ [VeC 149]: lb: fix make l4 lb function work

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**steven luong** <sluong@cisco.com>:

  | `36250 <https:////gerrit.fd.io/r/c/vpp/+/36250>`_ [A 180]: classify: sanity check table index for update

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
authors          86
maintainers      44
committers       1
abandoned        1
================ ===

