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
generated on Tuesday 2022-11-22, 12:41:48
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

  | `37516 <https:////gerrit.fd.io/r/c/vpp/+/37516>`_ [VECR 0]: ipsec: remove redundant policy array in fast path spd

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `37663 <https:////gerrit.fd.io/r/c/vpp/+/37663>`_ [VECr 6]: acl: fix set acl-plugin cli unformat free.
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VECr 17]: acl: change the algorithm for cleaning the sessions from purgatory

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 8]: af_xdp: optimizing send performance

classify: **Dave Barach** <vpp@barachs.net>
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VECr 7]: classify: fix classify session cli.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 7]: policer: fix crash when delete interface policer classify.

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [VECr 24]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters

devices: **Damjan Marion** <damarion@cisco.com>
  | `37674 <https:////gerrit.fd.io/r/c/vpp/+/37674>`_ [VECr 3]: interface: remove the pending interrupt from deleting interface

dma_intel: **Marvin Liu** <yong.liu@intel.com>
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VECr 18]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 18]: dma_intel: add native dsa device driver

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `37675 <https:////gerrit.fd.io/r/c/vpp/+/37675>`_ [VECr 0]: policer: adding documentation
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 14]: ip_session_redirect: add session redirect plugin

fib: **Neale Ranns** <neale@graphiant.com>
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 26]: nat: fix nat44-ed outside address selection

interface: **Dave Barach** <vpp@barachs.net>
  | `37674 <https:////gerrit.fd.io/r/c/vpp/+/37674>`_ [VECr 3]: interface: remove the pending interrupt from deleting interface
  | `37666 <https:////gerrit.fd.io/r/c/vpp/+/37666>`_ [VECr 6]: interface: fix format_vnet_interface_output_trace
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VECr 13]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VECr 3]: arp: fix arp request for ip4-glean node

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [VECr 3]: arp: fix arp request for ip4-glean node
  | `37655 <https:////gerrit.fd.io/r/c/vpp/+/37655>`_ [VECr 8]: vnet: fix trace flag copying in icmp4
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 26]: nat: add nat44-ed session filtering by fib table

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 4]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `37657 <https:////gerrit.fd.io/r/c/vpp/+/37657>`_ [VECr 7]: linux-cp: fix FIB_ENTRY_FLAG_ATTACHED

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 13]: sr: srv6 path tracing api
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 14]: ip_session_redirect: add session redirect plugin

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37683 <https:////gerrit.fd.io/r/c/vpp/+/37683>`_ [VECr 0]: nat: fix memory leak when config nat44 session limit.
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 26]: nat: nat66 cli bug fix
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VECr 26]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VECr 26]: nat: nat64 fix add_del calls requirements
  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VECr 26]: nat: DET: Allow unknown protocol translation
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 26]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 26]: nat: det44 map configuration improvements + tests
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VECr 26]: nat: auto forward inbound packet for local server session app with snat
  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [VECr 26]: nat: add local addresses correctly in nat lb static mapping
  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VECr 26]: nat: fix the wrong unformat type
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 26]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 26]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 26]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 26]: nat: fix tcp session reopen in nat44-ed
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VECr 26]: nat: fix nat44-ed API
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 26]: nat: nat44-ed get out2in workers failed for static mapping without port

policer: **Neale Ranns** <neale@graphiant.com>
  | `37675 <https:////gerrit.fd.io/r/c/vpp/+/37675>`_ [VECr 0]: policer: adding documentation
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 7]: policer: fix crash when delete interface policer classify.

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 13]: sr: srv6 path tracing api

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 4]: srv6-mobile: Implement SRv6 mobile API funcs

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37673 <https:////gerrit.fd.io/r/c/vpp/+/37673>`_ [VECr 0]: ipsec: add per-SA error counters
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 4]: ipsec: fix transpose local ip range position with remote ip range in fast path implementation
  | `37672 <https:////gerrit.fd.io/r/c/vpp/+/37672>`_ [VECr 5]: ipsec: fix SA names consistency in tests
  | `37654 <https:////gerrit.fd.io/r/c/vpp/+/37654>`_ [VECr 8]: tests: improve packet checksum functions
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 14]: ip_session_redirect: add session redirect plugin
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 26]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 26]: nat: det44 map configuration improvements + tests
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 26]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 26]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 26]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 26]: nat: fix tcp session reopen in nat44-ed

udp: **Florin Coras** <fcoras@cisco.com>
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [VECr 0]: udp: hand off packet to right session thread
  | `37680 <https:////gerrit.fd.io/r/c/vpp/+/37680>`_ [VECr 3]: udp: preallocate ports sparse vec map

vapi: **Ole Troan** <ot@cisco.com>
  | `37608 <https:////gerrit.fd.io/r/c/vpp/+/37608>`_ [VECr 12]: vapi: write enumflag types to vapi headers

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 0]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VECr 18]: vlib: support dma map extended memory

vpp: **Dave Barach** <vpp@barachs.net>
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 18]: dma_intel: add native dsa device driver

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37498 <https:////gerrit.fd.io/r/c/vpp/+/37498>`_ [VECr 29]: vppinfra:fix pcap write large file(> 0x80000000) error.

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37518 <https:////gerrit.fd.io/r/c/vpp/+/37518>`_ [VECr 4]: wireguard: compute checksum for outer ipv6 header

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 78]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 80]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `37536 <https:////gerrit.fd.io/r/c/vpp/+/37536>`_ [vEC 26]: misc: VPP 22.10 Release Notes
  | `37129 <https:////gerrit.fd.io/r/c/vpp/+/37129>`_ [VeC 31]: vlib: clib_panic if sysconf() can't determine page size on startup
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [veC 31]: fateshare: a plugin for managing child processes
  | `31368 <https:////gerrit.fd.io/r/c/vpp/+/31368>`_ [Vec 152]: vlib: Sleep less in unix input if there were active signals recently
  | `36377 <https:////gerrit.fd.io/r/c/vpp/+/36377>`_ [VeC 165]: tests: add libmemif tests

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `37059 <https:////gerrit.fd.io/r/c/vpp/+/37059>`_ [VEc 4]: ipsec: new api for sa ips and ports updates
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 6]: ip: add support for buffer offload metadata in ip midchain

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 77]: ikev2: accept rekey request for IKE SA

**Benoît Ganne** <bganne@cisco.com>:

  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VeC 35]: pci: add option to force uio binding
  | `37416 <https:////gerrit.fd.io/r/c/vpp/+/37416>`_ [VeC 39]: virtio: add option to bind interface to uio driver
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 42]: build: add sanitizer option to configure script

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `36705 <https:////gerrit.fd.io/r/c/vpp/+/36705>`_ [VeC 117]: ip-neighbor: Fixed delay(1~2s) in neighbor-probe interval

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 80]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [VEc 4]: tests: remove intermittent failing tests on vpp_debug image

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 39]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [vEC 26]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [vEC 26]: nat: nat44-ed update timeout api
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [vEC 26]: nat: det44 map configuration improvements

**Florin Coras** <florin.coras@gmail.com>:

  | `36252 <https:////gerrit.fd.io/r/c/vpp/+/36252>`_ [VeC 175]: svm: multi chunk allocs if requests larger than max chunk

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37361 <https:////gerrit.fd.io/r/c/vpp/+/37361>`_ [VEc 27]: wireguard: add atomic mutex

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 56]: urpf: add show urpf cli
  | `34726 <https:////gerrit.fd.io/r/c/vpp/+/34726>`_ [VeC 109]: interface: add buffer stats api

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `36592 <https:////gerrit.fd.io/r/c/vpp/+/36592>`_ [VeC 139]: stats: handle interface renames properly
  | `36590 <https:////gerrit.fd.io/r/c/vpp/+/36590>`_ [VeC 139]: nat: fix handling checksum offload in nat44-ed

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 82]: vppapigen: fix json build error

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 45]: memif: fix uninitialized variable warning

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37073 <https:////gerrit.fd.io/r/c/vpp/+/37073>`_ [veC 77]: ip neighbor: fix debug log format output

**Mercury Noah** <mercury124185@gmail.com>:

  | `36492 <https:////gerrit.fd.io/r/c/vpp/+/36492>`_ [VeC 151]: ip6-nd: fix ip6-nd proxy issue

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `33726 <https:////gerrit.fd.io/r/c/vpp/+/33726>`_ [VeC 40]: vlib: introduce an inter worker interrupts efds

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `37505 <https:////gerrit.fd.io/r/c/vpp/+/37505>`_ [veC 31]: gso: add gso documentation
  | `37497 <https:////gerrit.fd.io/r/c/vpp/+/37497>`_ [veC 32]: devices: make the gso and qdisc-bypass default
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VeC 53]: gso: use the header offsets from buffer metadata
  | `36725 <https:////gerrit.fd.io/r/c/vpp/+/36725>`_ [Vec 117]: virtio: add support for tx-queue-size
  | `36513 <https:////gerrit.fd.io/r/c/vpp/+/36513>`_ [VeC 146]: libmemif: add the binaries in the packaging
  | `36484 <https:////gerrit.fd.io/r/c/vpp/+/36484>`_ [VeC 152]: libmemif: add testing application
  | `36296 <https:////gerrit.fd.io/r/c/vpp/+/36296>`_ [veC 175]: pg: fix the use of hdr offsets in buffer metadata

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 47]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 53]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 53]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 53]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 53]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 53]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 53]: cnat: flag to disable rsession
  | `35805 <https:////gerrit.fd.io/r/c/vpp/+/35805>`_ [VeC 53]: dpdk: add intf tag to dev{} subinput
  | `32271 <https:////gerrit.fd.io/r/c/vpp/+/32271>`_ [VeC 53]: memif: add support for ns abstract sockets
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VeC 127]: memif: autogenerate socket_ids

**Naveen Joy** <najoy@cisco.com>:

  | `37374 <https:////gerrit.fd.io/r/c/vpp/+/37374>`_ [VEc 3]: tests: tapv2, tunv2 and af_packet interface tests for vpp

**Neale Ranns** <neale@graphiant.com>:

  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 102]: vlib: "sh errors" shows error severity counters

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `37268 <https:////gerrit.fd.io/r/c/vpp/+/37268>`_ [VeC 40]: lb: add source ip based sticky load balancing

**Peter Skvarka** <pskvarka@frinx.io>:

  | `30177 <https:////gerrit.fd.io/r/c/vpp/+/30177>`_ [vec 172]: flowprobe: memory leak unreleased frame

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `37678 <https:////gerrit.fd.io/r/c/vpp/+/37678>`_ [VEc 3]: fib: partial fix to a deadlock during CSIT tests execution

**RADHA KRISHNA SARAGADAM** <krishna_srk2003@yahoo.com>:

  | `36711 <https:////gerrit.fd.io/r/c/vpp/+/36711>`_ [Vec 118]: ebuild: upgrade vagrant ubuntu version to 20.04

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VeC 67]: vppapigen: enable codegen for stream message types
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 77]: virtio: allocate frame per interface

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 90]: ip6-nd: add fixed flag

**Ted Chen** <znscnchen@gmail.com>:

  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 54]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 66]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vEc 25]: dpdk: fix interface name w/ the same PCI bus/slot/function
  | `36488 <https:////gerrit.fd.io/r/c/vpp/+/36488>`_ [VeC 148]: tests: fix wireguard test failure under heavy load

**Ting Xu** <ting.xu@intel.com>:

  | `37563 <https:////gerrit.fd.io/r/c/vpp/+/37563>`_ [vEC 0]: avf: support generic flow

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37315 <https:////gerrit.fd.io/r/c/vpp/+/37315>`_ [VeC 49]: buffers: fix buffer leak on enqueue to bad thread
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 55]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 60]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 60]: papi: fix socket api max message id calculation

**Vratko Polak** <vrpolak@cisco.com>:

  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 69]: avf: tolerate socket events in avf_process_request
  | `27972 <https:////gerrit.fd.io/r/c/vpp/+/27972>`_ [VeC 145]: sr: Fix deletion if target SR list is not found
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 145]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 31]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [veC 37]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 44]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 45]: ipsec: fix ipsec linked key not freed when sa deleted
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 84]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 102]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 102]: cjson: json realloced output truncated if actual lenght more then 256

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 81]: ip: fixup crash when reassemble a lots of fragments.

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37274 <https:////gerrit.fd.io/r/c/vpp/+/37274>`_ [Vec 32]: af_xdp: fix xdp socket create fail

**f00182600** <fangtong2007@163.com>:

  | `36453 <https:////gerrit.fd.io/r/c/vpp/+/36453>`_ [veC 140]: interface: fix the issue of show hardware-interface with invalid if-idx can caused vpp crash.
  | `35963 <https:////gerrit.fd.io/r/c/vpp/+/35963>`_ [veC 158]: dns: fix the isssue of memory leak.
  | `35862 <https:////gerrit.fd.io/r/c/vpp/+/35862>`_ [VeC 158]: nat: Delete the operation of repeatedly releasing Nat44 ei port resources

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 68]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [VEc 7]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [VEc 9]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [vEC 15]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [VEc 26]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**steven luong** <sluong@cisco.com>:

  | `37488 <https:////gerrit.fd.io/r/c/vpp/+/37488>`_ [vEC 6]: vhost: convert vhost device driver to a plugin
  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [vEC 7]: vxlan: convert vxlan to a plugin
  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 40]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 105]: bonding: Add failover-mac active support
  | `36250 <https:////gerrit.fd.io/r/c/vpp/+/36250>`_ [VeC 178]: classify: sanity check table index for update

**xujunjie-cover** <xujunjielxx@163.com>:

  | `36494 <https:////gerrit.fd.io/r/c/vpp/+/36494>`_ [VeC 148]: lb: fix make l4 lb function work

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Aleksander Djuric** <aleksander.djuric@gmail.com>:

  | `24306 <https:////gerrit.fd.io/r/c/vpp/+/24306>`_ [A 917]: dhcp: add nodns and nodefault params
  | `24309 <https:////gerrit.fd.io/r/c/vpp/+/24309>`_ [A 1020]: ip: ip4/ip6 local ping support
  | `24341 <https:////gerrit.fd.io/r/c/vpp/+/24341>`_ [A 1034]: fib: fib entry post install fix
  | `24424 <https:////gerrit.fd.io/r/c/vpp/+/24424>`_ [A 1034]: ip: fib headers refactoring
  | `23146 <https:////gerrit.fd.io/r/c/vpp/+/23146>`_ [A 1117]: vlib: add event-logger params delta/no-delta/date-time

**Alexander Gryanko** <xpahos@gmail.com>:

  | `13361 <https:////gerrit.fd.io/r/c/vpp/+/13361>`_ [A 1453]: VOM: Add flush method to dump_cmd

**Alexander Kabaev** <kan@freebsd.org>:

  | `22272 <https:////gerrit.fd.io/r/c/vpp/+/22272>`_ [A 1119]: vlib: allow configuration for default rate limit

**Aloys Augustin** <aloaugus@cisco.com>:

  | `34844 <https:////gerrit.fd.io/r/c/vpp/+/34844>`_ [A 0]: misc: fix physmem allocation error handling
  | `27474 <https:////gerrit.fd.io/r/c/vpp/+/27474>`_ [A 895]: ip: expose API to enable IP4 on an interface
  | `27460 <https:////gerrit.fd.io/r/c/vpp/+/27460>`_ [A 897]: quic: WIP: improve scheduling
  | `27127 <https:////gerrit.fd.io/r/c/vpp/+/27127>`_ [A 910]: ipsec: WIP: IPsec SA pinning experiment
  | `25996 <https:////gerrit.fd.io/r/c/vpp/+/25996>`_ [A 977]: tap: improve default rx scheduling

**Anatoly Nikulin** <trotux@gmail.com>:

  | `31917 <https:////gerrit.fd.io/r/c/vpp/+/31917>`_ [A 593]: acl: fix enabling interface counters

**Andreas Schultz** <aschultz@warp10.net>:

  | `27097 <https:////gerrit.fd.io/r/c/vpp/+/27097>`_ [A 920]: misc: pass NULL instead off 0 for pointer in variadic functions
  | `15798 <https:////gerrit.fd.io/r/c/vpp/+/15798>`_ [A 946]: upf: Initial implementation of 3GPP TS 23.214 GTP-U UPF
  | `26038 <https:////gerrit.fd.io/r/c/vpp/+/26038>`_ [A 976]: tcp: move options parse to separate reusable function
  | `25223 <https:////gerrit.fd.io/r/c/vpp/+/25223>`_ [A 999]: docs: document alternate compression tools for core files
  | `16092 <https:////gerrit.fd.io/r/c/vpp/+/16092>`_ [A 1461]: handle invalid session in tcp shutdown procedures

**Andrej Kozemcak** <andrej.kozemcak@pantheon.tech>:

  | `20489 <https:////gerrit.fd.io/r/c/vpp/+/20489>`_ [A 1237]: DO_NOT_MERGE: Test build VOM packaged.
  | `16818 <https:////gerrit.fd.io/r/c/vpp/+/16818>`_ [A 1400]: Fix asserting in ip4_tcp_udp_compute_checksum.

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `34635 <https:////gerrit.fd.io/r/c/vpp/+/34635>`_ [A 0]: ip: punt socket - take the tags in Ethernet header into consideration
  | `28083 <https:////gerrit.fd.io/r/c/vpp/+/28083>`_ [A 0]: acl: acl-plugin custom policies
  | `35955 <https:////gerrit.fd.io/r/c/vpp/+/35955>`_ [A 0]: api: do not attempt to pass the null queue pointer from vl_api_can_send_msg
  | `28513 <https:////gerrit.fd.io/r/c/vpp/+/28513>`_ [A 0]: capo: Calico Policies plugin
  | `36142 <https:////gerrit.fd.io/r/c/vpp/+/36142>`_ [A 0]: build: add a check that "Fix" commits also refer to the commit that they are fixing
  | `26945 <https:////gerrit.fd.io/r/c/vpp/+/26945>`_ [A 928]: (to be edited) expectations on tests for the test framework

**Andrey "Zed" Zaikin** <zmail11@gmail.com>:

  | `12748 <https:////gerrit.fd.io/r/c/vpp/+/12748>`_ [A 1641]: lb: add missing vip/as indexes to trace strings

**Arthas Kang** <arthas.kang@163.com>:

  | `31084 <https:////gerrit.fd.io/r/c/vpp/+/31084>`_ [A 658]: plugin lb Fixed NAT4 SNAT invalid src_port ; Add NAT4 TCP SNAT support; Fixed NAT4 add SNAT map with protocol 0;

**Asumu Takikawa** <asumu@igalia.com>:

  | `16387 <https:////gerrit.fd.io/r/c/vpp/+/16387>`_ [A 1439]: nat: fix issues in MAP-E port allocation mode
  | `16388 <https:////gerrit.fd.io/r/c/vpp/+/16388>`_ [A 1446]: CSIT-541: add lwB4 functionality for lw4o6

**Atzm Watanabe** <atzmism@gmail.com>:

  | `35224 <https:////gerrit.fd.io/r/c/vpp/+/35224>`_ [A 0]: ikev2: fix profile_index for ikev2_sa_dump API

**Avinash Gonsalves** <avinash.gonsalves@nokia.com>:

  | `15084 <https:////gerrit.fd.io/r/c/vpp/+/15084>`_ [A 650]: ipsec: add multicore crypto scheduler support

**Baruch Siach** <baruch@siach.name>:

  | `33935 <https:////gerrit.fd.io/r/c/vpp/+/33935>`_ [A 415]: vppinfra: decode aarch64 PC in signal handler
  | `33934 <https:////gerrit.fd.io/r/c/vpp/+/33934>`_ [A 415]: vppinfra: remove redundant local variables initialization

**Berenger Foucher** <berenger.foucher@stagiaires.ssi.gouv.fr>:

  | `14578 <https:////gerrit.fd.io/r/c/vpp/+/14578>`_ [A 1544]: Add X509 authentication support to IKEv2 in VPP

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `35927 <https:////gerrit.fd.io/r/c/vpp/+/35927>`_ [A 0]: fib: enhancement to support change table-id associated with fib-table

**Brant Lin** <brant.lin@ericsson.com>:

  | `14902 <https:////gerrit.fd.io/r/c/vpp/+/14902>`_ [A 1524]: Fix the crash when creating the vapi context

**Carl Baldwin** <carl@ecbaldwin.net>:

  | `23528 <https:////gerrit.fd.io/r/c/vpp/+/23528>`_ [A 1099]: docs: Remove redundancy on building VPP page

**Carl Smith** <carl.smith@alliedtelesis.co.nz>:

  | `23634 <https:////gerrit.fd.io/r/c/vpp/+/23634>`_ [A 1092]: ipip: return existing if_index if tunnel already exists.

**Chinmaya Agarwal** <chinmaya.agarwal@hsc.com>:

  | `33635 <https:////gerrit.fd.io/r/c/vpp/+/33635>`_ [A 446]: sr: fix added for returning correct value for behavior field in API message

**Chris Luke** <chris_luke@comcast.com>:

  | `9483 <https:////gerrit.fd.io/r/c/vpp/+/9483>`_ [A 1678]: PAPI unserializer for reply_in_shmem data (VPP-136)
  | `9482 <https:////gerrit.fd.io/r/c/vpp/+/9482>`_ [A 1678]: Add fetching shmem support to vpp_papi (VPP-136)

**Christian Hopps** <chopps@chopps.org>:

  | `28657 <https:////gerrit.fd.io/r/c/vpp/+/28657>`_ [A 809]: misc: vpp_get_stats: add dump-machine formatting
  | `22353 <https:////gerrit.fd.io/r/c/vpp/+/22353>`_ [A 1118]: vlib: add option to use stderr instead of syslog.

**Clement Durand** <clement.durand@polytechnique.edu>:

  | `6274 <https:////gerrit.fd.io/r/c/vpp/+/6274>`_ [A 1740]: elog: Text-format dump of event logs.

**Damjan Marion** <dmarion@0xa5.net>:

  | `35155 <https:////gerrit.fd.io/r/c/vpp/+/35155>`_ [A 0]: vppinfra: universal splats and aligned loads/stores
  | `36067 <https:////gerrit.fd.io/r/c/vpp/+/36067>`_ [A 0]: vppinfra: move cJSON and jsonformat to vlibmemory
  | `34856 <https:////gerrit.fd.io/r/c/vpp/+/34856>`_ [A 317]: ethernet: promisc refactor
  | `34845 <https:////gerrit.fd.io/r/c/vpp/+/34845>`_ [A 318]: ethernet: add_del_mac and change_mac are ethernet specific

**Daniel Beres** <daniel.beres@pantheon.tech>:

  | `34628 <https:////gerrit.fd.io/r/c/vpp/+/34628>`_ [A 316]: dns: support AAAA over IPV4

**Dave Wallace** <dwallacelf@gmail.com>:

  | `33727 <https:////gerrit.fd.io/r/c/vpp/+/33727>`_ [A 0]: tests: relicense
  | `33707 <https:////gerrit.fd.io/r/c/vpp/+/33707>`_ [A 0]: papi: relicense

**David Johnson** <davijoh3@cisco.com>:

  | `16670 <https:////gerrit.fd.io/r/c/vpp/+/16670>`_ [A 1396]: Fix various -Wmaybe-uninitialized and -Wstrict-overflow warnings

**Dmitry Vakhrushev** <dmitry@netgate.com>:

  | `25502 <https:////gerrit.fd.io/r/c/vpp/+/25502>`_ [A 552]: interface: getting interface device specific info

**Dmitry Valter** <dvalter@protonmail.com>:

  | `34800 <https:////gerrit.fd.io/r/c/vpp/+/34800>`_ [A 0]: vppinfra: fix non-zero offsets to NULL pointer
  | `34694 <https:////gerrit.fd.io/r/c/vpp/+/34694>`_ [A 0]: vlib: remove process restart cli

**Ed Kern** <ejk@cisco.com>:

  | `20442 <https:////gerrit.fd.io/r/c/vpp/+/20442>`_ [A 1239]: build: do not merge

**Ed Warnicke** <hagbard@gmail.com>:

  | `14394 <https:////gerrit.fd.io/r/c/vpp/+/14394>`_ [A 1553]: Update docker files to reflect best pratices.

**Faicker Mo** <faicker.mo@ucloud.cn>:

  | `18207 <https:////gerrit.fd.io/r/c/vpp/+/18207>`_ [A 1347]: dpdk: Fix tx queue overflow when multi workers are used

**Feng Gao** <davidfgao@tencent.com>:

  | `26296 <https:////gerrit.fd.io/r/c/vpp/+/26296>`_ [A 964]: ipsec: Correct inconsistent alignment for crypto_op

**Florin Coras** <florin.coras@gmail.com>:

  | `23529 <https:////gerrit.fd.io/r/c/vpp/+/23529>`_ [A 440]: tcp: fin on data packets

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `36133 <https:////gerrit.fd.io/r/c/vpp/+/36133>`_ [A 0]: vapi: add a new api for ipsec for collecting date
  | `32655 <https:////gerrit.fd.io/r/c/vpp/+/32655>`_ [A 529]: crypto: fix possible frame resize

**Gary Boon** <gboon@cisco.com>:

  | `30522 <https:////gerrit.fd.io/r/c/vpp/+/30522>`_ [A 700]: Add callback support for the dispatch node.
  | `30239 <https:////gerrit.fd.io/r/c/vpp/+/30239>`_ [A 719]: Add a new function to the MCAP logic that allows a custom header to be added on top of the data in a vlib buffer.
  | `25517 <https:////gerrit.fd.io/r/c/vpp/+/25517>`_ [A 998]: vlib: check for null handoff queue element in vlib_buffer_enqueue_to_thread

**Gerard Keown** <gerard.keown@enea.com>:

  | `24369 <https:////gerrit.fd.io/r/c/vpp/+/24369>`_ [A 1041]: cores: mismatching "worker" & "corelist-workers" parameters can cause coredump

**Govindarajan Mohandoss** <govindarajan.mohandoss@arm.com>:

  | `28164 <https:////gerrit.fd.io/r/c/vpp/+/28164>`_ [A 832]: acl: ACL Plugin performance improvement for both SF and SL modes
  | `27167 <https:////gerrit.fd.io/r/c/vpp/+/27167>`_ [A 908]: acl: ACL Plugin performance improvement for both SF and SL modes

**Hemant Singh** <hemant@mnkcg.com>:

  | `32077 <https:////gerrit.fd.io/r/c/vpp/+/32077>`_ [A 473]: fixstyle
  | `32023 <https:////gerrit.fd.io/r/c/vpp/+/32023>`_ [A 579]: ip-neighbor: Add ip_neighbor_find_entry with ip+interface key

**IJsbrand Wijnands** <iwijnand@cisco.com>:

  | `25696 <https:////gerrit.fd.io/r/c/vpp/+/25696>`_ [A 991]: mpls: add user defined name tag to mpls tunnels
  | `25678 <https:////gerrit.fd.io/r/c/vpp/+/25678>`_ [A 991]: tap: tap dev_name and default value for bin api
  | `25677 <https:////gerrit.fd.io/r/c/vpp/+/25677>`_ [A 991]: tap: tap dev_name and default value for bin api

**Ignas Bačius** <ignas@noia.network>:

  | `22733 <https:////gerrit.fd.io/r/c/vpp/+/22733>`_ [A 1114]: gre: allow to delete tunnel by sw_if_index
  | `22666 <https:////gerrit.fd.io/r/c/vpp/+/22666>`_ [A 1135]: ip: fix possible use of uninitialized variable

**Igor Mikhailov** <imichail@cisco.com>:

  | `15131 <https:////gerrit.fd.io/r/c/vpp/+/15131>`_ [A 1477]: Ensure VPP library version has 2 digits separated by dot.

**Ilia Abashin** <abashinos@gmail.com>:

  | `20234 <https:////gerrit.fd.io/r/c/vpp/+/20234>`_ [A 1251]: Updated vpp_if_stats to latest version, including fresh documentation

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `28085 <https:////gerrit.fd.io/r/c/vpp/+/28085>`_ [A 846]: hsa: fix proxy crash upon failed connect

**Jack Xu** <jack.c.xu@ericsson.com>:

  | `18406 <https:////gerrit.fd.io/r/c/vpp/+/18406>`_ [A 1340]: fix multi-enable bug of enable feature function

**Jakub Grajciar** <jgrajcia@cisco.com>:

  | `30575 <https:////gerrit.fd.io/r/c/vpp/+/30575>`_ [A 405]: libmemif: add shm debug APIs
  | `28175 <https:////gerrit.fd.io/r/c/vpp/+/28175>`_ [A 551]: api: implement api for api trace
  | `29526 <https:////gerrit.fd.io/r/c/vpp/+/29526>`_ [A 584]: api: python object model
  | `30216 <https:////gerrit.fd.io/r/c/vpp/+/30216>`_ [A 718]: tests: remove sr_mpls from vpp_papi_provider and add sr_mpls object models
  | `30125 <https:////gerrit.fd.io/r/c/vpp/+/30125>`_ [A 720]: tests: remove igmp from vpp_papi_provider and refactor igmp object models

**Jakub Havas** <jakub.havas@pantheon.tech>:

  | `33130 <https:////gerrit.fd.io/r/c/vpp/+/33130>`_ [A 495]: udp: create an api to dump decaps
  | `32948 <https:////gerrit.fd.io/r/c/vpp/+/32948>`_ [A 510]: ipfix-export: replace cli command with an implemented api function

**Jan Cavojsky** <jan.cavojsky@pantheon.tech>:

  | `28899 <https:////gerrit.fd.io/r/c/vpp/+/28899>`_ [A 655]: flowprobe: add API dump of params and list of interfaces for recording
  | `25992 <https:////gerrit.fd.io/r/c/vpp/+/25992>`_ [A 713]: libmemif: update example applications and documentation
  | `28988 <https:////gerrit.fd.io/r/c/vpp/+/28988>`_ [A 791]: vat: avoid crash vpp after command ip_table_dump

**Jason Zhang** <jason.zhang2@arm.com>:

  | `22355 <https:////gerrit.fd.io/r/c/vpp/+/22355>`_ [A 1116]: vppinfra: change CLIB_MEMORY_BARRIER to use C11 built-in atomic APIs

**Jasvinder Singh** <jasvinder.singh@intel.com>:

  | `16839 <https:////gerrit.fd.io/r/c/vpp/+/16839>`_ [A 1369]: HQoS: update scheduler to support mbuf sched field change

**Jawahar Gundapaneni** <jgundapa@cisco.com>:

  | `25995 <https:////gerrit.fd.io/r/c/vpp/+/25995>`_ [A 700]: interface: Upstream TAP I/fs with ADMIN_UP
  | `26121 <https:////gerrit.fd.io/r/c/vpp/+/26121>`_ [A 964]: memif: CLI to debug memif buffer contents

**Jessica Tallon** <tsyesika@igalia.com>:

  | `15500 <https:////gerrit.fd.io/r/c/vpp/+/15500>`_ [A 1453]: VPP-923: Add trace filtering enhancement

**Jing Liu** <liu.jing5@zte.com.cn>:

  | `14335 <https:////gerrit.fd.io/r/c/vpp/+/14335>`_ [A 1544]: Add Memory barrier while calling clib_cpu_time_now

**Jing Peng** <pj.hades@gmail.com>:

  | `36042 <https:////gerrit.fd.io/r/c/vpp/+/36042>`_ [A 0]: vppinfra: add bihash update interface
  | `36062 <https:////gerrit.fd.io/r/c/vpp/+/36062>`_ [A 0]: vppinfra: fix duplicate bihash stat update
  | `36186 <https:////gerrit.fd.io/r/c/vpp/+/36186>`_ [A 0]: nat: fix nat44 fib reference count bookkeeping

**John Lo** <lojultra2020@outlook.com>:

  | `14858 <https:////gerrit.fd.io/r/c/vpp/+/14858>`_ [A 1505]: Bring back original l2-output node function

**Jordy You** <jordy.you@ericsson.com>:

  | `13016 <https:////gerrit.fd.io/r/c/vpp/+/13016>`_ [A 1523]: fix ip checksum issue for odd start address
  | `13002 <https:////gerrit.fd.io/r/c/vpp/+/13002>`_ [A 1624]: fix ip checksum issue for odd start address if the input data is starting with an odd address,then the calcuation will be error

**Julius Milan** <julius.milan@pantheon.tech>:

  | `29050 <https:////gerrit.fd.io/r/c/vpp/+/29050>`_ [A 653]: papi: fix name vector stats entry dump
  | `29030 <https:////gerrit.fd.io/r/c/vpp/+/29030>`_ [A 713]: nat: add per host counters into det44
  | `29029 <https:////gerrit.fd.io/r/c/vpp/+/29029>`_ [A 790]: stats: enable setting of name vectors for plugins
  | `29028 <https:////gerrit.fd.io/r/c/vpp/+/29028>`_ [A 790]: stats: fix dump of null data entries
  | `25785 <https:////gerrit.fd.io/r/c/vpp/+/25785>`_ [A 970]: vppinfra: add bitmap search next bit on interval

**Junfeng Wang** <drenfong.wang@intel.com>:

  | `33607 <https:////gerrit.fd.io/r/c/vpp/+/33607>`_ [A 0]: wireguard:avx512 blake3 for wireguard
  | `31581 <https:////gerrit.fd.io/r/c/vpp/+/31581>`_ [A 613]: pppoe: init the variable of result0 result1
  | `29975 <https:////gerrit.fd.io/r/c/vpp/+/29975>`_ [A 727]: l2: l2output avx512
  | `30117 <https:////gerrit.fd.io/r/c/vpp/+/30117>`_ [A 727]: l2: test

**Keith Burns** <alagalah@gmail.com>:

  | `22368 <https:////gerrit.fd.io/r/c/vpp/+/22368>`_ [A 1150]: vat : VLAN subif formatter accepting 'vlan'       instead of 'vlan_id'

**Kevin Wang** <kevin.wang@arm.com>:

  | `10293 <https:////gerrit.fd.io/r/c/vpp/+/10293>`_ [A 1757]: vppinfra: use __atomic_fetch_add instead of __sync_fetch_and_add builtins

**King Ma** <kinma@cisco.com>:

  | `20390 <https:////gerrit.fd.io/r/c/vpp/+/20390>`_ [A 946]: ip: make reassembled packet to preserve ip.fib_index

**Kingwel Xie** <kingwel.xie@ericsson.com>:

  | `16617 <https:////gerrit.fd.io/r/c/vpp/+/16617>`_ [A 1352]: perfmon: improvement, HW_CACHE events
  | `16910 <https:////gerrit.fd.io/r/c/vpp/+/16910>`_ [A 1402]: pg: improved unformat_user to show accurate error message

**Kiran Shastri** <shastrinator@gmail.com>:

  | `20445 <https:////gerrit.fd.io/r/c/vpp/+/20445>`_ [A 1232]: Fix git usage in vom build scripts

**Klement Sekera** <klement.sekera@gmail.com>:

  | `33507 <https:////gerrit.fd.io/r/c/vpp/+/33507>`_ [A 0]: nat: properly handle truncated packets
  | `32435 <https:////gerrit.fd.io/r/c/vpp/+/32435>`_ [A 0]: nat: enhance test - make sure all workers are hit
  | `35218 <https:////gerrit.fd.io/r/c/vpp/+/35218>`_ [A 0]: tests: prevent running as root
  | `35739 <https:////gerrit.fd.io/r/c/vpp/+/35739>`_ [A 0]: tests: refactor assert*counter_equal APIs
  | `27083 <https:////gerrit.fd.io/r/c/vpp/+/27083>`_ [A 921]: nat: "users" dump for ED-NAT

**Korian Edeline** <korian.edeline@ulg.ac.be>:

  | `14083 <https:////gerrit.fd.io/r/c/vpp/+/14083>`_ [A 1566]: consistent output for bitmap next_set&next_clear

**Kyeong Min Park** <pak2536@gmail.com>:

  | `30960 <https:////gerrit.fd.io/r/c/vpp/+/30960>`_ [A 656]: memif: fix invalid next_index selection

**Leung Lai Yung** <benkerbuild@gmail.com>:

  | `36128 <https:////gerrit.fd.io/r/c/vpp/+/36128>`_ [A 0]: vppinfra: remove unused line

**Mauricio Solis** <mauricio.solisjr@tno.nl>:

  | `29862 <https:////gerrit.fd.io/r/c/vpp/+/29862>`_ [A 0]: ip6 ioam: updated iOAM plugin based on https://github.com/inband-oam/ietf/blob/master/drafts/versions/03/draft-ietf-ippm-ioam-ipv6-options-03.txt and https://tools.ietf.org/html/draft-ietf-ippm-ioam-data-10

**Maxime Peim** <mpeim@cisco.com>:

  | `33019 <https:////gerrit.fd.io/r/c/vpp/+/33019>`_ [A 481]: vlib: adaptive mode switching algorithm modification

**Mercury Noah** <mercury124185@gmail.com>:

  | `35916 <https:////gerrit.fd.io/r/c/vpp/+/35916>`_ [A 0]: arp: fix the arp proxy issue

**Michael Yu** <michael.a.yu@nokia-sbell.com>:

  | `30454 <https:////gerrit.fd.io/r/c/vpp/+/30454>`_ [A 705]: devices: fix af-packet device TX stuck issue

**Michal Kalderon** <mkalderon@marvell.com>:

  | `34795 <https:////gerrit.fd.io/r/c/vpp/+/34795>`_ [A 329]: svm: Fix chunk allocation when data_size is larger than max chunk size

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `34873 <https:////gerrit.fd.io/r/c/vpp/+/34873>`_ [A 0]: nat: reliable TCP conn close in NAT44-ed
  | `34851 <https:////gerrit.fd.io/r/c/vpp/+/34851>`_ [A 318]: nat: reliable TCP conn establishment in NAT44-ed

**Mohammed Alshohayeb** <mshohayeb@wirefilter.com>:

  | `16470 <https:////gerrit.fd.io/r/c/vpp/+/16470>`_ [A 1419]: docs: clarify doxygen vec _align behaviour.

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `35912 <https:////gerrit.fd.io/r/c/vpp/+/35912>`_ [A 0]: interface: fix the processing levels
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [A 0]: devices: add cli support to enable disable qdisc bypass
  | `34517 <https:////gerrit.fd.io/r/c/vpp/+/34517>`_ [A 371]: hash: fix the Extension Header for ipv6 in crc32_5tuples
  | `33954 <https:////gerrit.fd.io/r/c/vpp/+/33954>`_ [A 410]: process: vpp process privileges and capabilities
  | `32837 <https:////gerrit.fd.io/r/c/vpp/+/32837>`_ [A 518]: gso: improve interface handling
  | `32470 <https:////gerrit.fd.io/r/c/vpp/+/32470>`_ [A 543]: virtio: fix the number of rxqs
  | `31700 <https:////gerrit.fd.io/r/c/vpp/+/31700>`_ [A 609]: interface: rename runtime data func
  | `31115 <https:////gerrit.fd.io/r/c/vpp/+/31115>`_ [A 649]: virtio: add multi-txq support for vhost user

**Nathan Moos** <nmoos@cisco.com>:

  | `30792 <https:////gerrit.fd.io/r/c/vpp/+/30792>`_ [A 665]: build: add config option for LD_PRELOAD

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `35756 <https:////gerrit.fd.io/r/c/vpp/+/35756>`_ [A 0]: cnat: expose flow hash config in tr
  | `34552 <https:////gerrit.fd.io/r/c/vpp/+/34552>`_ [A 319]: cnat: add single lookup

**Naveen Joy** <najoy@cisco.com>:

  | `33000 <https:////gerrit.fd.io/r/c/vpp/+/33000>`_ [A 507]: tests: alternative log directory for unittest logs
  | `31937 <https:////gerrit.fd.io/r/c/vpp/+/31937>`_ [A 584]: tests: enable make test to be run inside a VM
  | `29921 <https:////gerrit.fd.io/r/c/vpp/+/29921>`_ [A 733]: tests: run tests against an existing VPP instance
  | `18602 <https:////gerrit.fd.io/r/c/vpp/+/18602>`_ [A 1131]: tests: fixes test_bier_e2e_64 for python3
  | `22817 <https:////gerrit.fd.io/r/c/vpp/+/22817>`_ [A 1131]: tests: fix scapy error when using python3
  | `18606 <https:////gerrit.fd.io/r/c/vpp/+/18606>`_ [A 1330]: fixes TypeError raised by the framework when using python3
  | `18128 <https:////gerrit.fd.io/r/c/vpp/+/18128>`_ [A 1354]: make-test: apply common PEP8 style conventions

**Neale Ranns** <neale@graphiant.com>:

  | `35436 <https:////gerrit.fd.io/r/c/vpp/+/35436>`_ [A 0]: qos: Dual loop the QoS record node
  | `34686 <https:////gerrit.fd.io/r/c/vpp/+/34686>`_ [A 348]: dependency: Create the dependency graph tracking infra. A simple cut-n-paste of what is already present in FIB
  | `34687 <https:////gerrit.fd.io/r/c/vpp/+/34687>`_ [A 349]: fib: Remove the fib graph dependency code
  | `34688 <https:////gerrit.fd.io/r/c/vpp/+/34688>`_ [A 350]: dependency: Dpendency tracking improvements
  | `34689 <https:////gerrit.fd.io/r/c/vpp/+/34689>`_ [A 351]: interface: Add a dependency node to a SW interface fib: update the adjacnecy subsystem to use interface dependency tracking
  | `33510 <https:////gerrit.fd.io/r/c/vpp/+/33510>`_ [A 462]: tests: Test for ARP behaviour on links with a /32 configured
  | `32770 <https:////gerrit.fd.io/r/c/vpp/+/32770>`_ [A 469]: ip: A weak host mode for IPv6
  | `26811 <https:////gerrit.fd.io/r/c/vpp/+/26811>`_ [A 475]: ipsec: Make Add/Del SA MP safe
  | `32760 <https:////gerrit.fd.io/r/c/vpp/+/32760>`_ [A 509]: fib: tunnel: Pin a tunnel's egress interface to its source
  | `30412 <https:////gerrit.fd.io/r/c/vpp/+/30412>`_ [A 552]: ethernet: Ether types on the API
  | `27086 <https:////gerrit.fd.io/r/c/vpp/+/27086>`_ [A 552]: ip: ip6 rewrite performance bump
  | `31428 <https:////gerrit.fd.io/r/c/vpp/+/31428>`_ [A 580]: ipsec: Remove the backend infra
  | `31397 <https:////gerrit.fd.io/r/c/vpp/+/31397>`_ [A 584]: vppapigen: Support an 'mpsafe' keyword on the API
  | `31695 <https:////gerrit.fd.io/r/c/vpp/+/31695>`_ [A 599]: teib: Fix fib-index for nh and peer
  | `31780 <https:////gerrit.fd.io/r/c/vpp/+/31780>`_ [A 602]: dpdk: Fix the handling of failed burst enqueues for crypto ops
  | `31788 <https:////gerrit.fd.io/r/c/vpp/+/31788>`_ [A 603]: ip: Repeat ip4 prefetch strategy for ip6 in rewrite
  | `30141 <https:////gerrit.fd.io/r/c/vpp/+/30141>`_ [A 721]: tests: Sum stats over all threads
  | `29494 <https:////gerrit.fd.io/r/c/vpp/+/29494>`_ [A 763]: devices: NULL device
  | `29310 <https:////gerrit.fd.io/r/c/vpp/+/29310>`_ [A 774]: pg: Coverity warning of uninitialised variable
  | `28966 <https:////gerrit.fd.io/r/c/vpp/+/28966>`_ [A 791]: misc: lawful-intercept Move to plugin
  | `27271 <https:////gerrit.fd.io/r/c/vpp/+/27271>`_ [A 909]: ipsec: Dual loop tunnel lookup node
  | `26693 <https:////gerrit.fd.io/r/c/vpp/+/26693>`_ [A 941]: ip: Dedicated ip[46] rewrite nodes for tagged traffic
  | `25973 <https:////gerrit.fd.io/r/c/vpp/+/25973>`_ [A 979]: tests: Do not use randomly named directories for test results
  | `24135 <https:////gerrit.fd.io/r/c/vpp/+/24135>`_ [A 1061]: ip: Vectorized mtrie lookup
  | `18739 <https:////gerrit.fd.io/r/c/vpp/+/18739>`_ [A 1320]: Copyright update check
  | `17086 <https:////gerrit.fd.io/r/c/vpp/+/17086>`_ [A 1395]: L2-FIB: make the result 16 bytes
  | `9336 <https:////gerrit.fd.io/r/c/vpp/+/9336>`_ [A 1572]: L3 Span

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `26617 <https:////gerrit.fd.io/r/c/vpp/+/26617>`_ [A 906]: gtpu geneve vxlan vxlan-gpe vxlan-gbp: DPO leak
  | `25691 <https:////gerrit.fd.io/r/c/vpp/+/25691>`_ [A 920]: gtpu: fix encap_vrf_id conversion in binapi handler

**Nitin Saxena** <nsaxena@marvell.com>:

  | `28643 <https:////gerrit.fd.io/r/c/vpp/+/28643>`_ [A 810]: interface: Fix possible memleaks in standard APIs

**Ole Troan** <otroan@employees.org>:

  | `33819 <https:////gerrit.fd.io/r/c/vpp/+/33819>`_ [A 400]: api: binary-api-json command to call api from vpp cli
  | `33518 <https:////gerrit.fd.io/r/c/vpp/+/33518>`_ [A 426]: vat: disable vat linked into vpp by default
  | `31656 <https:////gerrit.fd.io/r/c/vpp/+/31656>`_ [A 545]: vpp: api to get connection information
  | `30484 <https:////gerrit.fd.io/r/c/vpp/+/30484>`_ [A 546]: api: crcchecker list messages marked deprecated that can be removed
  | `28822 <https:////gerrit.fd.io/r/c/vpp/+/28822>`_ [A 602]: api: show api message-table deprecated

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `16356 <https:////gerrit.fd.io/r/c/vpp/+/16356>`_ [A 1434]: Python 3 supporting PAPI rpm

**Parham Fisher** <s3m2e1.6star@gmail.com>:

  | `16201 <https:////gerrit.fd.io/r/c/vpp/+/16201>`_ [A 946]: ip_reassembly_enable_disable vat command is added.
  | `20308 <https:////gerrit.fd.io/r/c/vpp/+/20308>`_ [A 1239]: nat: If a feature like abf is enabled,      the next node of nat44-out2in is not ip4-lookup.      so I find next node using vnet_feature_next.
  | `15173 <https:////gerrit.fd.io/r/c/vpp/+/15173>`_ [A 1506]: initialize next0, because of following compile error: ‘next0’ may be used uninitialized in this function [-Werror=maybe-uninitialized]
  | `14848 <https:////gerrit.fd.io/r/c/vpp/+/14848>`_ [A 1526]: speed and duplex must set when link is up, otherwise the value of them is unknown.

**Paul Vinciguerra** <pvinci@vinciconsulting.com>:

  | `24082 <https:////gerrit.fd.io/r/c/vpp/+/24082>`_ [A 544]: vlib: log - fix input handling of 'default' subclass
  | `30545 <https:////gerrit.fd.io/r/c/vpp/+/30545>`_ [A 546]: tests: refactor gbp tests
  | `26832 <https:////gerrit.fd.io/r/c/vpp/+/26832>`_ [A 546]: vxlan-gpe: update api defaults/fix protocol
  | `26150 <https:////gerrit.fd.io/r/c/vpp/+/26150>`_ [A 552]: build: fix make 'install-deps' on fresh container
  | `31997 <https:////gerrit.fd.io/r/c/vpp/+/31997>`_ [A 552]: build: fix missing clang dependency in make install-dep
  | `27349 <https:////gerrit.fd.io/r/c/vpp/+/27349>`_ [A 552]: libmemif:  don't redefine _GNU_SOURCE
  | `27351 <https:////gerrit.fd.io/r/c/vpp/+/27351>`_ [A 552]: libmemif: fix dockerfile for examples
  | `31999 <https:////gerrit.fd.io/r/c/vpp/+/31999>`_ [A 555]: acl:  remove VppAclPlugin from vpp_acl.py
  | `32199 <https:////gerrit.fd.io/r/c/vpp/+/32199>`_ [A 567]: tests: fix IndexError in framework.py
  | `32198 <https:////gerrit.fd.io/r/c/vpp/+/32198>`_ [A 567]: tests: fix resource leaks in vpp_pg_interface.py
  | `32117 <https:////gerrit.fd.io/r/c/vpp/+/32117>`_ [A 567]: tests: move ip neighbor code from vpp_papi_provider
  | `32119 <https:////gerrit.fd.io/r/c/vpp/+/32119>`_ [A 574]: tests: clean up ipfix_exporter from vpp_papi_provider
  | `32118 <https:////gerrit.fd.io/r/c/vpp/+/32118>`_ [A 574]: tests: cleanup udp_encap from vpp_papi_provider
  | `32005 <https:////gerrit.fd.io/r/c/vpp/+/32005>`_ [A 585]: api:  set missing default values for is_add fields
  | `31998 <https:////gerrit.fd.io/r/c/vpp/+/31998>`_ [A 585]: arping: fix vat_help typo in api file
  | `27353 <https:////gerrit.fd.io/r/c/vpp/+/27353>`_ [A 643]: build: add make targets for vom/libmemif
  | `31296 <https:////gerrit.fd.io/r/c/vpp/+/31296>`_ [A 644]: misc: whitespace changes from clang-format-10
  | `31295 <https:////gerrit.fd.io/r/c/vpp/+/31295>`_ [A 644]: misc: remove indent-on linter
  | `26178 <https:////gerrit.fd.io/r/c/vpp/+/26178>`_ [A 646]: api: add msg_id to 'client input queue is stuffed...' message
  | `30546 <https:////gerrit.fd.io/r/c/vpp/+/30546>`_ [A 647]: vxlan-gbp: add interface_name to dump/details to use VppVxlanGbpTunnel
  | `26873 <https:////gerrit.fd.io/r/c/vpp/+/26873>`_ [A 647]: misc: vom - fix variable name in dhcp_client_cmds bind_cmd
  | `24570 <https:////gerrit.fd.io/r/c/vpp/+/24570>`_ [A 647]: gbp: set VNID_INVALID to last value in range
  | `23018 <https:////gerrit.fd.io/r/c/vpp/+/23018>`_ [A 647]: devices: add context around console messages
  | `26871 <https:////gerrit.fd.io/r/c/vpp/+/26871>`_ [A 647]: misc: vom - cleanup typos for doxygen
  | `26833 <https:////gerrit.fd.io/r/c/vpp/+/26833>`_ [A 647]: tests: refactor VppInterface
  | `26872 <https:////gerrit.fd.io/r/c/vpp/+/26872>`_ [A 647]: misc: vom - fix typo in gbp-endpoint-create: to_string
  | `26291 <https:////gerrit.fd.io/r/c/vpp/+/26291>`_ [A 647]: tests: add tests for ip.api
  | `30551 <https:////gerrit.fd.io/r/c/vpp/+/30551>`_ [A 647]: misc: fix typo in foreach_vnet_api_error
  | `30361 <https:////gerrit.fd.io/r/c/vpp/+/30361>`_ [A 647]: papi: refactor client to decouple dependency on transport
  | `30401 <https:////gerrit.fd.io/r/c/vpp/+/30401>`_ [A 647]: papi: only build python3 binary distributions
  | `30350 <https:////gerrit.fd.io/r/c/vpp/+/30350>`_ [A 647]: papi: calculate function properties once
  | `30360 <https:////gerrit.fd.io/r/c/vpp/+/30360>`_ [A 647]: papi: mark apifiles option of VPPApiClient as non-optional
  | `30220 <https:////gerrit.fd.io/r/c/vpp/+/30220>`_ [A 647]: vapi: cleanup nits in vapi doc
  | `24131 <https:////gerrit.fd.io/r/c/vpp/+/24131>`_ [A 691]: vlib: add LSB standard exit codes if vpp doesn't start properly
  | `21208 <https:////gerrit.fd.io/r/c/vpp/+/21208>`_ [A 705]: tests: don't pin python dependencies
  | `30435 <https:////gerrit.fd.io/r/c/vpp/+/30435>`_ [A 706]: tests: fix node variant tests
  | `30080 <https:////gerrit.fd.io/r/c/vpp/+/30080>`_ [A 707]: vppapigen:  WIP -- make vppapigen importable as a python module
  | `30343 <https:////gerrit.fd.io/r/c/vpp/+/30343>`_ [A 713]: api: remove [backwards_compatable] option and bump semver
  | `30289 <https:////gerrit.fd.io/r/c/vpp/+/30289>`_ [A 717]: tests:  split wireguard tests from configuation classes
  | `26703 <https:////gerrit.fd.io/r/c/vpp/+/26703>`_ [A 717]: tests: fix memif ping
  | `29938 <https:////gerrit.fd.io/r/c/vpp/+/29938>`_ [A 720]: tests: refactor debug_internal into subclass of VppTestCase
  | `18694 <https:////gerrit.fd.io/r/c/vpp/+/18694>`_ [A 726]: papi: Add an option to build vpp_papi with same version as VPP.
  | `30078 <https:////gerrit.fd.io/r/c/vpp/+/30078>`_ [A 730]: tests: vpp_papi EXPERIMENT Do not merge!!!
  | `25727 <https:////gerrit.fd.io/r/c/vpp/+/25727>`_ [A 920]: papi: build setup under python3
  | `26886 <https:////gerrit.fd.io/r/c/vpp/+/26886>`_ [A 930]: vom: update .clang-format
  | `26358 <https:////gerrit.fd.io/r/c/vpp/+/26358>`_ [A 948]: tests: SonarCloud refactor cli string literals
  | `26225 <https:////gerrit.fd.io/r/c/vpp/+/26225>`_ [A 968]: vppapigen: for vat plugins, use local_logger
  | `24573 <https:////gerrit.fd.io/r/c/vpp/+/24573>`_ [A 1029]: ethernet: create unique default loopback mac-addresses
  | `24132 <https:////gerrit.fd.io/r/c/vpp/+/24132>`_ [A 1047]: tests:  improve checks for test_tap
  | `23555 <https:////gerrit.fd.io/r/c/vpp/+/23555>`_ [A 1049]: tests: ensure host has enough cores for test
  | `24189 <https:////gerrit.fd.io/r/c/vpp/+/24189>`_ [A 1053]: tests: refactor QUICAppWorker
  | `24107 <https:////gerrit.fd.io/r/c/vpp/+/24107>`_ [A 1054]: tests: Experiment - log info in case of startUpClass failure
  | `24159 <https:////gerrit.fd.io/r/c/vpp/+/24159>`_ [A 1054]: tests: vlib - remove set pmc instructions-per-clock
  | `23755 <https:////gerrit.fd.io/r/c/vpp/+/23755>`_ [A 1054]: papi tests: add ability for test to connect via vapi socket
  | `23349 <https:////gerrit.fd.io/r/c/vpp/+/23349>`_ [A 1060]: build: add python imports to 'make checkstyle'
  | `24114 <https:////gerrit.fd.io/r/c/vpp/+/24114>`_ [A 1060]: tests:  use flake8 for 'make test-checkstyle'
  | `20228 <https:////gerrit.fd.io/r/c/vpp/+/20228>`_ [A 1061]: misc: run verify jobs against debug images
  | `24087 <https:////gerrit.fd.io/r/c/vpp/+/24087>`_ [A 1068]: tests: ip6 add comments in SLAAC test
  | `23030 <https:////gerrit.fd.io/r/c/vpp/+/23030>`_ [A 1068]: tests: enable dpdk plugin
  | `23488 <https:////gerrit.fd.io/r/c/vpp/+/23488>`_ [A 1076]: tests: don't try to remove vpp_config without conn to api.
  | `23951 <https:////gerrit.fd.io/r/c/vpp/+/23951>`_ [A 1076]: vppapigen: fix for explicit types
  | `23664 <https:////gerrit.fd.io/r/c/vpp/+/23664>`_ [A 1085]: tests:  skip test if can't run worker executable
  | `23491 <https:////gerrit.fd.io/r/c/vpp/+/23491>`_ [A 1087]: tests: fix run_test exception
  | `23697 <https:////gerrit.fd.io/r/c/vpp/+/23697>`_ [A 1088]: tests: change vapi_response_timeout in cli test
  | `23490 <https:////gerrit.fd.io/r/c/vpp/+/23490>`_ [A 1089]: tests: framework VppDiedError - handle vpp hung
  | `23521 <https:////gerrit.fd.io/r/c/vpp/+/23521>`_ [A 1090]: tests: vpp_pg_interface.py don't let OSError impact subsequent tests
  | `17251 <https:////gerrit.fd.io/r/c/vpp/+/17251>`_ [A 1092]: Dependencies test: Do not commit!
  | `23487 <https:////gerrit.fd.io/r/c/vpp/+/23487>`_ [A 1096]: tests: don't introduce changes that link VppTestCase and run_tests.py
  | `23531 <https:////gerrit.fd.io/r/c/vpp/+/23531>`_ [A 1099]: tests: test_neighbor.py refactor verify_arp
  | `23492 <https:////gerrit.fd.io/r/c/vpp/+/23492>`_ [A 1100]: tests: no longer allow bare "except:"'s
  | `23314 <https:////gerrit.fd.io/r/c/vpp/+/23314>`_ [A 1110]: vpp: update 'ip virtual' short help to match parser
  | `20229 <https:////gerrit.fd.io/r/c/vpp/+/20229>`_ [A 1111]: misc: run EXTENDED_TESTS=1 test-debug in CI
  | `23125 <https:////gerrit.fd.io/r/c/vpp/+/23125>`_ [A 1116]: crypto-openssl: show opennssl version name
  | `23068 <https:////gerrit.fd.io/r/c/vpp/+/23068>`_ [A 1118]: pg: expand interface name in show packet-generator
  | `23031 <https:////gerrit.fd.io/r/c/vpp/+/23031>`_ [A 1118]: tests: remove python2isms from framework.py
  | `20292 <https:////gerrit.fd.io/r/c/vpp/+/20292>`_ [A 1160]: tests: have test_flowprobe.py use existing api calls
  | `20185 <https:////gerrit.fd.io/r/c/vpp/+/20185>`_ [A 1198]: papi: make UnexpectedApiReturnValueError friendlier
  | `20632 <https:////gerrit.fd.io/r/c/vpp/+/20632>`_ [A 1199]: tests: improve ipsec test performance
  | `20945 <https:////gerrit.fd.io/r/c/vpp/+/20945>`_ [A 1210]: vapi: fix vapi_c_gen.py suport for defaults
  | `19522 <https:////gerrit.fd.io/r/c/vpp/+/19522>`_ [A 1210]: api:  return errorcode cli_inband
  | `20266 <https:////gerrit.fd.io/r/c/vpp/+/20266>`_ [A 1216]: tests: refactor CliFailedCommandError
  | `20484 <https:////gerrit.fd.io/r/c/vpp/+/20484>`_ [A 1216]: misc: add dependency info to commit template
  | `20570 <https:////gerrit.fd.io/r/c/vpp/+/20570>`_ [A 1223]: tests: limit time for VppTestCase to end after SIGTERM
  | `20619 <https:////gerrit.fd.io/r/c/vpp/+/20619>`_ [A 1229]: tests: create PROFILE=1 CI job.
  | `20616 <https:////gerrit.fd.io/r/c/vpp/+/20616>`_ [A 1229]: tests: fix VppGbpContractRule
  | `20326 <https:////gerrit.fd.io/r/c/vpp/+/20326>`_ [A 1235]: tests: - experiment--identify dup. object creation in tests.
  | `20160 <https:////gerrit.fd.io/r/c/vpp/+/20160>`_ [A 1235]: gbp: add test for test_api_gbp_bridge_domain_add
  | `20414 <https:////gerrit.fd.io/r/c/vpp/+/20414>`_ [A 1240]: build:  Update .gitignore
  | `20202 <https:////gerrit.fd.io/r/c/vpp/+/20202>`_ [A 1242]: mpls: mpls_sw_interface_enable_disable should return error
  | `20171 <https:////gerrit.fd.io/r/c/vpp/+/20171>`_ [A 1252]: mpls: fix coredump if disabling mpls on non-mpls int. via api
  | `20200 <https:////gerrit.fd.io/r/c/vpp/+/20200>`_ [A 1252]: interface: return an error if sw_interface_set_unnumbered fails.
  | `18166 <https:////gerrit.fd.io/r/c/vpp/+/18166>`_ [A 1347]: Tests: test/vpp_interface.py. Compute static properties once.
  | `18020 <https:////gerrit.fd.io/r/c/vpp/+/18020>`_ [A 1356]: Do Not Commit! test_Reassembly.
  | `16642 <https:////gerrit.fd.io/r/c/vpp/+/16642>`_ [A 1369]: Tests: Stop swallowing exceptions. Bare exceptions.
  | `17093 <https:////gerrit.fd.io/r/c/vpp/+/17093>`_ [A 1385]: VTL: Fix Segment routing API tests.
  | `16991 <https:////gerrit.fd.io/r/c/vpp/+/16991>`_ [A 1399]: VTL: Change classify_add_del_session vpp_papi_provider.py logic to support 'skip_n_vectors'.
  | `16769 <https:////gerrit.fd.io/r/c/vpp/+/16769>`_ [A 1405]: DO NOT MERGE! Demonstrate VTL VppObjectRegistry contract violations.
  | `16724 <https:////gerrit.fd.io/r/c/vpp/+/16724>`_ [A 1412]: Add bug reporting framework to tests.
  | `16660 <https:////gerrit.fd.io/r/c/vpp/+/16660>`_ [A 1418]: test framework.py Handle missing docstring gracefully.
  | `16616 <https:////gerrit.fd.io/r/c/vpp/+/16616>`_ [A 1419]: tests: Rework vpp config generation.
  | `16270 <https:////gerrit.fd.io/r/c/vpp/+/16270>`_ [A 1452]: Fix typo.  vpp_papi/vpp_serializer.py
  | `16285 <https:////gerrit.fd.io/r/c/vpp/+/16285>`_ [A 1452]: test/framework.py: add exception handling to Worker.
  | `16158 <https:////gerrit.fd.io/r/c/vpp/+/16158>`_ [A 1453]: Alternative to Fix test framework keepalive

**Pavel Kotucek** <pavel.kotucek@pantheon.tech>:

  | `28019 <https:////gerrit.fd.io/r/c/vpp/+/28019>`_ [A 853]: misc: (NAT) eBPF traceability
  | `17565 <https:////gerrit.fd.io/r/c/vpp/+/17565>`_ [A 1372]: Fix VPP-1506

**Pengjieyou** <pangkityau@gmail.com>:

  | `33528 <https:////gerrit.fd.io/r/c/vpp/+/33528>`_ [A 459]: acl: fix ipv6 address match of acl_plugin

**Peter Skvarka** <pskvarka@frinx.io>:

  | `29493 <https:////gerrit.fd.io/r/c/vpp/+/29493>`_ [A 726]: flowprobe: memory leak unreleased frame

**Pierre Pfister** <ppfister@cisco.com>:

  | `14358 <https:////gerrit.fd.io/r/c/vpp/+/14358>`_ [A 1357]: Add vat plugin path to run-vat
  | `14782 <https:////gerrit.fd.io/r/c/vpp/+/14782>`_ [A 1531]: Fix 'show lb vips' CLI command

**Ping Yu** <ping.yu@intel.com>:

  | `26310 <https:////gerrit.fd.io/r/c/vpp/+/26310>`_ [A 963]: dpdk: fix an issue that hw offload
  | `24903 <https:////gerrit.fd.io/r/c/vpp/+/24903>`_ [A 1015]: tls: handle TCP reset in TLS stack
  | `24336 <https:////gerrit.fd.io/r/c/vpp/+/24336>`_ [A 1042]: tls: openssl handle closure alert
  | `24138 <https:////gerrit.fd.io/r/c/vpp/+/24138>`_ [A 1060]: svm: fix a dead wait for svm message
  | `21213 <https:////gerrit.fd.io/r/c/vpp/+/21213>`_ [A 1198]: tls: enable openssl master build
  | `16798 <https:////gerrit.fd.io/r/c/vpp/+/16798>`_ [A 1407]: Fix build issue if using openssl 3.0.0 dev branch
  | `16640 <https:////gerrit.fd.io/r/c/vpp/+/16640>`_ [A 1423]: fix an issue for vfio auto detection
  | `13765 <https:////gerrit.fd.io/r/c/vpp/+/13765>`_ [A 1578]: Add a flag for user to build openssl with a new interface

**Piotr Kleski** <piotrx.kleski@intel.com>:

  | `30383 <https:////gerrit.fd.io/r/c/vpp/+/30383>`_ [A 644]: ipsec: async mode restrictions

**Radu Nicolau** <radu.nicolau@intel.com>:

  | `31702 <https:////gerrit.fd.io/r/c/vpp/+/31702>`_ [A 552]: avf: performance improvement
  | `30974 <https:////gerrit.fd.io/r/c/vpp/+/30974>`_ [A 622]: vlib: startup multi-arch variant configuration fix for interfaces

**Rajesh Saluja** <rajsaluj@cisco.com>:

  | `31016 <https:////gerrit.fd.io/r/c/vpp/+/31016>`_ [A 662]: estimated mtu should be derived from max_fragment_length
  | `20415 <https:////gerrit.fd.io/r/c/vpp/+/20415>`_ [A 957]: ip: calculate TCP/UDP checksum before fragmenting the packet if VNET_BUFFER_F_OFFLOAD_xxx_CKSUM flag is set

**Rajith Ramakrishna** <rajith@rtbrick.com>:

  | `35227 <https:////gerrit.fd.io/r/c/vpp/+/35227>`_ [A 0]: fib: fix fib path pool expand cases fib_path_create, fib_path_create_special are not thread safe when the fib path pool expand.
  | `35289 <https:////gerrit.fd.io/r/c/vpp/+/35289>`_ [A 0]: fib: fix the crash in worker when fib_path_list_pool expands
  | `35291 <https:////gerrit.fd.io/r/c/vpp/+/35291>`_ [A 0]: ip6: fix packet drop of NS message for link local destination.

**Ryan King** <ryanking8215@gmail.com>:

  | `20078 <https:////gerrit.fd.io/r/c/vpp/+/20078>`_ [A 1252]: fix client making cpu high after vpp restart

**Ryujiro Shibuya** <ryujiro.shibuya@owmobility.com>:

  | `27790 <https:////gerrit.fd.io/r/c/vpp/+/27790>`_ [A 868]: tcp: rework on rcv wnd adjustment
  | `23979 <https:////gerrit.fd.io/r/c/vpp/+/23979>`_ [A 1068]: svm: add an option to keep margin in the fifo

**Sachin Saxena** <sachin.saxena18@gmail.com>:

  | `13189 <https:////gerrit.fd.io/r/c/vpp/+/13189>`_ [A 1569]: arm: Added option to include DPDK armv8_crypto library
  | `12932 <https:////gerrit.fd.io/r/c/vpp/+/12932>`_ [A 1574]: dpdk: Add Virtual addressing support in IOVA dmamap

**Sergey Matov** <sergey.matov@travelping.com>:

  | `30099 <https:////gerrit.fd.io/r/c/vpp/+/30099>`_ [A 493]: vppinfra: Refactor sparse_vec_free
  | `31433 <https:////gerrit.fd.io/r/c/vpp/+/31433>`_ [A 635]: vlib: Avoid counter overflow

**Shiva Shankar** <shivaashankar1204@gmail.com>:

  | `29707 <https:////gerrit.fd.io/r/c/vpp/+/29707>`_ [A 744]: ethernet: coverity fix #214973

**Shmuel Hazan** <shmuel.h@siklu.com>:

  | `34775 <https:////gerrit.fd.io/r/c/vpp/+/34775>`_ [A 329]: dpdk: don't remove unupdated hw flags

**Simon Zhang** <yuwei1.zhang@intel.com>:

  | `25754 <https:////gerrit.fd.io/r/c/vpp/+/25754>`_ [A 987]: tls: fix the wrong usage of svm_fifo_dequeue function in Picotls engine
  | `25584 <https:////gerrit.fd.io/r/c/vpp/+/25584>`_ [A 994]: tls: fix tls hang issue
  | `20519 <https:////gerrit.fd.io/r/c/vpp/+/20519>`_ [A 1236]: Allocate appropriate number of vlib_buffer_t for buffer chain scenario.

**Sirshak Das** <sirshak.das@arm.com>:

  | `12955 <https:////gerrit.fd.io/r/c/vpp/+/12955>`_ [A 1623]: Enable PMU cycle counter for graph node cycles

**Sivaprasad Tummala** <sivaprasad.tummala@intel.com>:

  | `34899 <https:////gerrit.fd.io/r/c/vpp/+/34899>`_ [A 0]: snort: flow steering to multiple daqs
  | `34897 <https:////gerrit.fd.io/r/c/vpp/+/34897>`_ [A 0]: snort: restrict daq instance to single thread
  | `34898 <https:////gerrit.fd.io/r/c/vpp/+/34898>`_ [A 0]: acl: fixed incorrect action code

**Sudhir C R** <sudhir@rtbrick.com>:

  | `35352 <https:////gerrit.fd.io/r/c/vpp/+/35352>`_ [A 0]: ping: This avoids assertion on disabling interface during a ping when ping is going on in one terminal and we disable interface from other terminal sometimes causes assertion type: fix
  | `35353 <https:////gerrit.fd.io/r/c/vpp/+/35353>`_ [A 0]: ping: This avoids assertion on disabling interface during a ping
  | `35355 <https:////gerrit.fd.io/r/c/vpp/+/35355>`_ [A 0]: ping: assertion on disabling interface during a ping
  | `35364 <https:////gerrit.fd.io/r/c/vpp/+/35364>`_ [A 0]: devices: fix the crash in worker when interface pool expands
  | `35367 <https:////gerrit.fd.io/r/c/vpp/+/35367>`_ [A 0]: ip: fragmentation issue with ttl 1

**Swarup Nayak** <swarupnpvt@gmail.com>:

  | `9815 <https:////gerrit.fd.io/r/c/vpp/+/9815>`_ [A 1453]: VPP-1098 Fix delete tap sw_if_index X (when X is not exist)

**Swati Kher** <swatikher@gmail.com>:

  | `20939 <https:////gerrit.fd.io/r/c/vpp/+/20939>`_ [A 1204]: Support for python3 - testcase compatibility for python3

**Tan Haiyang** <haiyangtan@tencent.com>:

  | `16643 <https:////gerrit.fd.io/r/c/vpp/+/16643>`_ [A 1423]: gbp: fix ipv6 type checking

**Tianyu Li** <tianyu.li@arm.com>:

  | `35680 <https:////gerrit.fd.io/r/c/vpp/+/35680>`_ [A 0]: ip: ip frag node multi arch support
  | `35707 <https:////gerrit.fd.io/r/c/vpp/+/35707>`_ [A 0]: ip: reassembly add prefetch to improve throughput
  | `32420 <https:////gerrit.fd.io/r/c/vpp/+/32420>`_ [A 537]: memif: unroll tx loop to increase performance
  | `32447 <https:////gerrit.fd.io/r/c/vpp/+/32447>`_ [A 544]: memif: using atomic_relaxed for shared data load

**Tianyu Li** <tianyulee@gmail.com>:

  | `16641 <https:////gerrit.fd.io/r/c/vpp/+/16641>`_ [A 1424]: Change show buffer output format to unsigned int

**Timothee Chauvin** <timchauv@cisco.com>:

  | `28136 <https:////gerrit.fd.io/r/c/vpp/+/28136>`_ [A 840]: misc: out-of-process fuzzing (AFL...) integration
  | `27678 <https:////gerrit.fd.io/r/c/vpp/+/27678>`_ [A 875]: misc: fix usage of lcov in extras/lcov/lcov_*

**Tom Seidenberg** <tseidenb@cisco.com>:

  | `24515 <https:////gerrit.fd.io/r/c/vpp/+/24515>`_ [A 1022]: virtio: Defensive fix for erroneous multisegment packets.

**Tony Samuels** <vegizombie@gmail.com>:

  | `17630 <https:////gerrit.fd.io/r/c/vpp/+/17630>`_ [A 1372]: Fix broken link in README. This is caused by the link being longer than the default line length of 80 characters.

**Vengada Govindan** <venggovi@cisco.com>:

  | `31906 <https:////gerrit.fd.io/r/c/vpp/+/31906>`_ [A 593]: nsh: resolve Coverity error in nsh_api.c

**Vladimir Isaev** <visaev@netgate.com>:

  | `29445 <https:////gerrit.fd.io/r/c/vpp/+/29445>`_ [A 571]: nat: do not translate packets from outside intfc

**Vladislav Grishenko** <themiron@mail.ru>:

  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [A 0]: vlib: avoid non-mp-safe cli process node updates
  | `35914 <https:////gerrit.fd.io/r/c/vpp/+/35914>`_ [A 0]: linux-cp: refactor sw_if_index bool vector to bitmap

**Wai Chan** <weichen@astri.org>:

  | `19429 <https:////gerrit.fd.io/r/c/vpp/+/19429>`_ [A 1294]: api: fix crash error that receive get_node_graph cmd from vat
  | `18542 <https:////gerrit.fd.io/r/c/vpp/+/18542>`_ [A 1335]: [VPPInfra]: Fix the issue that worker thread will access invalid memory when update thread do vector resize.

**Weiguo Li** <liwg06@foxmail.com>:

  | `34779 <https:////gerrit.fd.io/r/c/vpp/+/34779>`_ [A 335]: misc: fix incorrect return value checking

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `34866 <https:////gerrit.fd.io/r/c/vpp/+/34866>`_ [A 0]: ip6-nd: fix ethernet head building error for NA msg
  | `35361 <https:////gerrit.fd.io/r/c/vpp/+/35361>`_ [A 0]: vppinfra: fix asan issue for hash_memory64
  | `35563 <https:////gerrit.fd.io/r/c/vpp/+/35563>`_ [A 0]: ipsec: no need to check for sa integ_op_id when building async frame
  | `33578 <https:////gerrit.fd.io/r/c/vpp/+/33578>`_ [A 347]: ipsec: skip fragmented packet for ipsec4-input-feature node
  | `32899 <https:////gerrit.fd.io/r/c/vpp/+/32899>`_ [A 515]: dispatch-trace: fix "pcap dispatch trace on" command has no effect

**Xie Long** <barryxie@tencent.com>:

  | `30270 <https:////gerrit.fd.io/r/c/vpp/+/30270>`_ [A 715]: fib: fixup some fib nodes in node-graph are not been notified by fib_walk_sync/fib_walk_async

**Xu Wen** <wenx05124561@163.com>:

  | `14095 <https:////gerrit.fd.io/r/c/vpp/+/14095>`_ [A 1561]: nat64: nat64_out2in not translate when dst_address is on the interface
  | `14128 <https:////gerrit.fd.io/r/c/vpp/+/14128>`_ [A 1565]: nat64: nat64_out2in not translate when dst_address is on the interface
  | `13599 <https:////gerrit.fd.io/r/c/vpp/+/13599>`_ [A 1583]: nat64: make nat64 node runs_after acl nodes

**YI-SUNG Chiu** <steven30801@gmail.com>:

  | `34470 <https:////gerrit.fd.io/r/c/vpp/+/34470>`_ [A 337]: policer: enable handoff action in policer formatting

**Yohan Pipereau** <ypiperea@cisco.com>:

  | `20978 <https:////gerrit.fd.io/r/c/vpp/+/20978>`_ [A 1208]: vom: Support srv6 localsids
  | `20678 <https:////gerrit.fd.io/r/c/vpp/+/20678>`_ [A 1218]: vom: Separate RPM package for VOM

**Yong Liu** <yong.liu@intel.com>:

  | `31097 <https:////gerrit.fd.io/r/c/vpp/+/31097>`_ [A 624]: virtio: enhance packed ring status check

**Yucai Gu** <yucgu@cisco.com>:

  | `30321 <https:////gerrit.fd.io/r/c/vpp/+/30321>`_ [A 714]: VPP DPDK load balance feature This PR is to add a DPDK device load balance feature in the VPP base code. The idea of adding this feature is to resolve a worker CPU balance issue when the traffic is high.

**Zhiyong Yang** <zhiyong.yang@intel.com>:

  | `26226 <https:////gerrit.fd.io/r/c/vpp/+/26226>`_ [A 553]: vlib: add avx512 support for two vlib_get_buffer related functions
  | `27213 <https:////gerrit.fd.io/r/c/vpp/+/27213>`_ [A 742]: l2: performance enhancement in l2output
  | `26415 <https:////gerrit.fd.io/r/c/vpp/+/26415>`_ [A 958]: dpdk: prefetching second cacheline only when tx_offload enabled
  | `20838 <https:////gerrit.fd.io/r/c/vpp/+/20838>`_ [A 1208]: misc: avoid probable twice assignments in cop
  | `19206 <https:////gerrit.fd.io/r/c/vpp/+/19206>`_ [A 1302]: ipsec_output_inline: leverage vlib_get_buffers
  | `13666 <https:////gerrit.fd.io/r/c/vpp/+/13666>`_ [A 1453]: gre tunnel optimization
  | `13853 <https:////gerrit.fd.io/r/c/vpp/+/13853>`_ [A 1523]: ip4_rewrite: improve prefetching of packet header data on IA
  | `14389 <https:////gerrit.fd.io/r/c/vpp/+/14389>`_ [A 1546]: dpdk_input: remove duplicated assignment
  | `14134 <https:////gerrit.fd.io/r/c/vpp/+/14134>`_ [A 1555]: rewrite IP checksum on IA
  | `14306 <https:////gerrit.fd.io/r/c/vpp/+/14306>`_ [A 1558]: vxlan-gpe: quad-loop optimization
  | `13769 <https:////gerrit.fd.io/r/c/vpp/+/13769>`_ [A 1565]: rewrite _ip_incremental_checksum
  | `13803 <https:////gerrit.fd.io/r/c/vpp/+/13803>`_ [A 1574]: using ip_csum in ip4_header_checksum
  | `13140 <https:////gerrit.fd.io/r/c/vpp/+/13140>`_ [A 1604]: dpdk: force i40e to use avx2 optimized datapath when machine supports avx2
  | `12776 <https:////gerrit.fd.io/r/c/vpp/+/12776>`_ [A 1635]: dpdk: use initial-exec model for thread local variable on IA
  | `12733 <https:////gerrit.fd.io/r/c/vpp/+/12733>`_ [A 1640]: dpdk: makefile optimization

**alex ni** <alex.ni@mavenir.com>:

  | `18731 <https:////gerrit.fd.io/r/c/vpp/+/18731>`_ [A 1324]: delete the unnecessary code in ip4_frag_do_fragment: as max has been computed and &~0x7, it is unnecessary to compute it again

**arikachen** <eaglesora@gmail.com>:

  | `34561 <https:////gerrit.fd.io/r/c/vpp/+/34561>`_ [A 337]: af_xdp: fix free rxq buffers while delete if

**bindiya k** <bindiyakurle@gmail.com>:

  | `10394 <https:////gerrit.fd.io/r/c/vpp/+/10394>`_ [A 1751]: arp resolution does not when classifier table index attached to interface. Fixed this by always checking entry which has source as INTERFACE.

**dengfeng liu** <liudf0716@gmail.com>:

  | `30922 <https:////gerrit.fd.io/r/c/vpp/+/30922>`_ [A 665]: ip: replace type_by_name with type_and_code_by_name param Type: fix
  | `29376 <https:////gerrit.fd.io/r/c/vpp/+/29376>`_ [A 771]: ipsec: sort spd polices after delete a spd policy

**duojiao mu** <mu.duojiao@zte.com.cn>:

  | `19216 <https:////gerrit.fd.io/r/c/vpp/+/19216>`_ [A 1302]: VPP-1664:Get wrong extern head by ip6_ext_header_find_t.
  | `16370 <https:////gerrit.fd.io/r/c/vpp/+/16370>`_ [A 1373]: VPP-1516:when ip fib dump,connect route will display error.

**eyal bari** <royalbee@gmail.com>:

  | `15596 <https:////gerrit.fd.io/r/c/vpp/+/15596>`_ [A 1223]: l2_flood:bvi:use a full buffer copy

**guanghua zhang** <zhangguanghua2011@163.com>:

  | `22142 <https:////gerrit.fd.io/r/c/vpp/+/22142>`_ [A 1079]: tcp: tcp_check_tx_offload get sw_if_index in a another way.
  | `21628 <https:////gerrit.fd.io/r/c/vpp/+/21628>`_ [A 1180]: vlib: fix pcap dispatch trace command issue.

**han wu** <wuhan9084@163.com>:

  | `34684 <https:////gerrit.fd.io/r/c/vpp/+/34684>`_ [A 0]: ping: fix the wrong usage of vec_del1 which may cause unpredictable situation vrrp: fix the wrong usage of vec_del1 which may cause unpredictable situation wireguard: fix the wrong usage of vec_del1 which may cause unpredictable situation

**hu jihui** <hu.jihui@zte.com.cn>:

  | `30638 <https:////gerrit.fd.io/r/c/vpp/+/30638>`_ [A 685]: VPP-1960: vpp crash when del export fib entry
  | `19731 <https:////gerrit.fd.io/r/c/vpp/+/19731>`_ [A 1281]: VPP-1682 the 'curr_key' and 'next_key' members of struct 'bfd_session_t' could become wild pointer.

**jinshaohui jinshaohui** <jinshaohui789@163.com>:

  | `25595 <https:////gerrit.fd.io/r/c/vpp/+/25595>`_ [A 994]: vppinfra: fix memory issue in mhash
  | `25590 <https:////gerrit.fd.io/r/c/vpp/+/25590>`_ [A 994]: vppinfra: fix memory issue in mhash

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `34919 <https:////gerrit.fd.io/r/c/vpp/+/34919>`_ [A 0]: dpdk: number of tx queues can not larger than the physical max tx queues
  | `34963 <https:////gerrit.fd.io/r/c/vpp/+/34963>`_ [A 0]: interface:Format output with one more % C, terminal print gibberish
  | `32497 <https:////gerrit.fd.io/r/c/vpp/+/32497>`_ [A 541]: policer: cli policer bind name xxx <workers> failed              policer bind unbind name xxx  failed
  | `32496 <https:////gerrit.fd.io/r/c/vpp/+/32496>`_ [A 541]: policer: cli policer bind name xxx <workers> failed          policer bind unbind name xxx  failed
  | `32495 <https:////gerrit.fd.io/r/c/vpp/+/32495>`_ [A 541]: policer: cli policer bind name xxx <workers> failed            policer bind unbind name xxx  failed
  | `30930 <https:////gerrit.fd.io/r/c/vpp/+/30930>`_ [A 665]: vppinfra: fix memory issue in mhash

**juan dong** <dong.juan1@zte.com.cn>:

  | `30654 <https:////gerrit.fd.io/r/c/vpp/+/30654>`_ [A 679]: vlib: nm_clone node_by_name re-assign to avoid coredump
  | `19746 <https:////gerrit.fd.io/r/c/vpp/+/19746>`_ [A 1244]: nat: use different random seed
  | `19767 <https:////gerrit.fd.io/r/c/vpp/+/19767>`_ [A 1244]: nat: goto get_local may trigger exception when num_workers > 1

**kai zhang** <zhangkaiheb@126.com>:

  | `34806 <https:////gerrit.fd.io/r/c/vpp/+/34806>`_ [A 328]: nat44-ed: fix port endian of load-balancing static mapping

**khemendra kumar** <khemendra.kumar13@gmail.com>:

  | `12462 <https:////gerrit.fd.io/r/c/vpp/+/12462>`_ [A 1050]: VPP-1126 use restrict keyword so that compiler can          generate optimized code on aarch64

**liu anhua** <liu.anhua@ericsson.com>:

  | `13134 <https:////gerrit.fd.io/r/c/vpp/+/13134>`_ [A 0]: gtpu: Add gtpu path management and change single teid to bidirectional teid.
  | `13043 <https:////gerrit.fd.io/r/c/vpp/+/13043>`_ [A 1523]: Add to configure the tx queue len of TUN device.
  | `13040 <https:////gerrit.fd.io/r/c/vpp/+/13040>`_ [A 1604]: The parameter must be point of vec header while checking the heap object in funtion vlib_get_node_by_name.

**lollita liu** <lollita.liu@ericsson.com>:

  | `18310 <https:////gerrit.fd.io/r/c/vpp/+/18310>`_ [A 1347]: cli: fix the deadloop bug of inputting wrong node name in "show node" CLI

**maqi ke** <maqi.z.ke@ericsson.com>:

  | `18543 <https:////gerrit.fd.io/r/c/vpp/+/18543>`_ [A 1321]: cli:fix show node

**marek zavodsky** <mazavods@gmail.com>:

  | `31642 <https:////gerrit.fd.io/r/c/vpp/+/31642>`_ [A 616]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31628 <https:////gerrit.fd.io/r/c/vpp/+/31628>`_ [A 620]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31615 <https:////gerrit.fd.io/r/c/vpp/+/31615>`_ [A 620]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31608 <https:////gerrit.fd.io/r/c/vpp/+/31608>`_ [A 621]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31593 <https:////gerrit.fd.io/r/c/vpp/+/31593>`_ [A 623]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31438 <https:////gerrit.fd.io/r/c/vpp/+/31438>`_ [A 634]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31430 <https:////gerrit.fd.io/r/c/vpp/+/31430>`_ [A 635]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31426 <https:////gerrit.fd.io/r/c/vpp/+/31426>`_ [A 635]: dns: Failing to get DNS AAAA records (and A records in one case)

**pippo zhang** <pippo.zhang@ericsson.com>:

  | `16762 <https:////gerrit.fd.io/r/c/vpp/+/16762>`_ [A 1404]: add command: show statistics heap

**s5ci-nomad pilot** <ayourtch@icloud.com>:

  | `31429 <https:////gerrit.fd.io/r/c/vpp/+/31429>`_ [A 321]: misc: refresh the pinning of test dependencies by running make test-refresh-deps

**shaochun chen** <cscnull@gmail.com>:

  | `24150 <https:////gerrit.fd.io/r/c/vpp/+/24150>`_ [A 1055]: vmxnet3: translate etherType from network-order to host-order

**steven luong** <sluong@cisco.com>:

  | `35157 <https:////gerrit.fd.io/r/c/vpp/+/35157>`_ [A 0]: fib: remove all routes when vrf table is deleted
  | `35212 <https:////gerrit.fd.io/r/c/vpp/+/35212>`_ [A 0]: fib: crash at vnet_rewrite_set_data_internal
  | `35234 <https:////gerrit.fd.io/r/c/vpp/+/35234>`_ [A 0]: fib: ip table del checks
  | `36089 <https:////gerrit.fd.io/r/c/vpp/+/36089>`_ [A 0]: ip: Display show ip table without truncation
  | `33169 <https:////gerrit.fd.io/r/c/vpp/+/33169>`_ [A 493]: bonding: send GARP upon first member becomes active in bond
  | `32536 <https:////gerrit.fd.io/r/c/vpp/+/32536>`_ [A 537]: bonding: create bond process on demand
  | `32486 <https:////gerrit.fd.io/r/c/vpp/+/32486>`_ [A 542]: vhost: launch vhost process on demand
  | `32083 <https:////gerrit.fd.io/r/c/vpp/+/32083>`_ [A 546]: interface: error checking and returning for set interface rx-mode
  | `31452 <https:////gerrit.fd.io/r/c/vpp/+/31452>`_ [A 634]: nat: remove ASSERT in nat_6t_flow_ip4_translate
  | `31000 <https:////gerrit.fd.io/r/c/vpp/+/31000>`_ [A 662]: vlib: add trace trajectory for debugging
  | `29396 <https:////gerrit.fd.io/r/c/vpp/+/29396>`_ [A 770]: bonding: automatically set interface to promiscuos for LACP bonding
  | `28105 <https:////gerrit.fd.io/r/c/vpp/+/28105>`_ [A 845]: dpdk: allocate rx_queues and tx_queues early
  | `20189 <https:////gerrit.fd.io/r/c/vpp/+/20189>`_ [A 1252]: acl interface vlib: memory leaks
  | `17947 <https:////gerrit.fd.io/r/c/vpp/+/17947>`_ [A 1356]: c11 safeC replacement for strncpy and strcpy

**sunitha naram reddy** <snaramre@cisco.com>:

  | `23417 <https:////gerrit.fd.io/r/c/vpp/+/23417>`_ [A 716]: tests: scapy 2.4.3 changes
  | `23131 <https:////gerrit.fd.io/r/c/vpp/+/23131>`_ [A 1118]: tests: make test changes for scapy 2.4.3
  | `21621 <https:////gerrit.fd.io/r/c/vpp/+/21621>`_ [A 1180]: python3 string to byte conversions for udp tests

**vijayakumar rajamanickam** <vijayakumar.rajamanickam@nokia.com>:

  | `19829 <https:////gerrit.fd.io/r/c/vpp/+/19829>`_ [A 946]: reassembly: Ipv4 reassembly timeout  error counter

**wanghanlin wanghanlin** <wanghanlin@corp.netease.com>:

  | `34318 <https:////gerrit.fd.io/r/c/vpp/+/34318>`_ [A 382]: vcl: fix inaccuracy wait rpc response timeout
  | `33012 <https:////gerrit.fd.io/r/c/vpp/+/33012>`_ [A 504]: dpdk: add DEV_TX_OFFLOAD_IPV4_CKSUM support
  | `32963 <https:////gerrit.fd.io/r/c/vpp/+/32963>`_ [A 504]: dpdk: support TX CKSUM offload for mlx5
  | `32962 <https:////gerrit.fd.io/r/c/vpp/+/32962>`_ [A 504]: vppinfra: add timestamp for positioning problem
  | `28703 <https:////gerrit.fd.io/r/c/vpp/+/28703>`_ [A 657]: vcl: support kernel stack based on localhost IPV4 address

**xujunjie-cover** <xujunjielxx@163.com>:

  | `34703 <https:////gerrit.fd.io/r/c/vpp/+/34703>`_ [A 348]: dns: cache: fix show dns cache Unlock missing after show dns cache with name.

**yacan liu** <liuyacan@corp.netease.com>:

  | `32949 <https:////gerrit.fd.io/r/c/vpp/+/32949>`_ [A 507]: vcl: support packetdrill test framework

**yang mo** <srsdellsound@yahoo.com>:

  | `32754 <https:////gerrit.fd.io/r/c/vpp/+/32754>`_ [A 479]: sr: make srv6 ad flow support multi thread

**ye donggang** <yedg@wangsu.com>:

  | `29814 <https:////gerrit.fd.io/r/c/vpp/+/29814>`_ [A 713]: acl:  fix acl endless loop without session
  | `28603 <https:////gerrit.fd.io/r/c/vpp/+/28603>`_ [A 723]: ipsec: sort polices when del
  | `30082 <https:////gerrit.fd.io/r/c/vpp/+/30082>`_ [A 730]: interface:  fix show interface addr error
  | `28606 <https:////gerrit.fd.io/r/c/vpp/+/28606>`_ [A 815]: ipsec: use icv size to hmac in aead algo

**力茂 张** <zhanglimao0017@gmail.com>:

  | `18455 <https:////gerrit.fd.io/r/c/vpp/+/18455>`_ [A 1341]: configure classify table occur Segmentation fault

**郑 德伦** <xszhengdelun@gmail.com>:

  | `27193 <https:////gerrit.fd.io/r/c/vpp/+/27193>`_ [A 909]: interface: fix pcap trace filter error

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
authors          92
maintainers      45
committers       1
abandoned        459
================ ===

