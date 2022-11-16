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
generated on Wednesday 2022-11-16, 02:58:40
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

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `37663 <https:////gerrit.fd.io/r/c/vpp/+/37663>`_ [VECr 0]: acl: fix set acl-plugin cli unformat free.

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VECr 1]: af_xdp: optimizing send performance

api: **Dave Barach** <vpp@barachs.net>
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 25]: api: fix memory error with pending_rpc_requests in multi-thread environment

classify: **Dave Barach** <vpp@barachs.net>
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VECr 0]: classify: fix classify session cli.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 0]: policer: fix crash when delete interface policer classify.

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [VECr 18]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

dma_intel: **Marvin Liu** <yong.liu@intel.com>
  | `37574 <https:////gerrit.fd.io/r/c/vpp/+/37574>`_ [VECr 11]: dma_intel: add cbdma device support
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 11]: dma_intel: add native dsa device driver

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 8]: ip_session_redirect: add session redirect plugin

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 29]: pci: add option to force uio binding

fib: **Neale Ranns** <neale@graphiant.com>
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 20]: nat: fix nat44-ed outside address selection

interface: **Dave Barach** <vpp@barachs.net>
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VECr 6]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37655 <https:////gerrit.fd.io/r/c/vpp/+/37655>`_ [VECr 1]: vnet: fix trace flag copying in icmp4
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 20]: nat: add nat44-ed session filtering by fib table

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37516 <https:////gerrit.fd.io/r/c/vpp/+/37516>`_ [VECr 21]: ipsec: remove redundant policy array in fast path spd
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 21]: ipsec: fast path - transpose local ip range position with remote ip range

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `37657 <https:////gerrit.fd.io/r/c/vpp/+/37657>`_ [VECr 1]: linux-cp: fix FIB_ENTRY_FLAG_ATTACHED

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 6]: sr: srv6 path tracing api
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 8]: ip_session_redirect: add session redirect plugin

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 20]: nat: nat66 cli bug fix
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VECr 20]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VECr 20]: nat: nat64 fix add_del calls requirements
  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VECr 20]: nat: DET: Allow unknown protocol translation
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 20]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 20]: nat: det44 map configuration improvements + tests
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VECr 20]: nat: auto forward inbound packet for local server session app with snat
  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [VECr 20]: nat: add local addresses correctly in nat lb static mapping
  | `37162 <https:////gerrit.fd.io/r/c/vpp/+/37162>`_ [VECr 20]: nat: fix the wrong unformat type
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 20]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 20]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 20]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 20]: nat: fix tcp session reopen in nat44-ed
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VECr 20]: nat: fix nat44-ed API
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 20]: nat: nat44-ed get out2in workers failed for static mapping without port

pci: **Damjan Marion** <damarion@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 29]: pci: add option to force uio binding

policer: **Neale Ranns** <neale@graphiant.com>
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VECr 0]: policer: fix crash when delete interface policer classify.

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `37593 <https:////gerrit.fd.io/r/c/vpp/+/37593>`_ [VECr 6]: sr: srv6 path tracing api

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37654 <https:////gerrit.fd.io/r/c/vpp/+/37654>`_ [VECr 1]: tests: improve packet checksum functions
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VECr 8]: ip_session_redirect: add session redirect plugin
  | `37374 <https:////gerrit.fd.io/r/c/vpp/+/37374>`_ [VECr 13]: tests: tapv2, tunv2 and af_packet interface tests for vpp
  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VECr 20]: nat: fix nat44-ed outside address selection
  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VECr 20]: nat: det44 map configuration improvements + tests
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 20]: nat: fix nat44_ed set_session_limit crash
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 20]: nat: add nat44-ed session filtering by fib table
  | `37264 <https:////gerrit.fd.io/r/c/vpp/+/37264>`_ [VECr 20]: nat: fix nat44-ed outside address distribution
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 20]: nat: fix tcp session reopen in nat44-ed
  | `37504 <https:////gerrit.fd.io/r/c/vpp/+/37504>`_ [VECr 21]: ipsec: fast path - transpose local ip range position with remote ip range

vapi: **Ole Troan** <ot@cisco.com>
  | `37608 <https:////gerrit.fd.io/r/c/vpp/+/37608>`_ [VECr 6]: vapi: write enumflag types to vapi headers

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `37572 <https:////gerrit.fd.io/r/c/vpp/+/37572>`_ [VECr 11]: vlib: support dma map extended memory
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VECr 25]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 29]: pci: add option to force uio binding

vmxnet3: **Steven Luong** <sluong@cisco.com>
  | `37417 <https:////gerrit.fd.io/r/c/vpp/+/37417>`_ [VECr 29]: pci: add option to force uio binding

vpp: **Dave Barach** <vpp@barachs.net>
  | `37573 <https:////gerrit.fd.io/r/c/vpp/+/37573>`_ [VECr 11]: dma_intel: add native dsa device driver

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37498 <https:////gerrit.fd.io/r/c/vpp/+/37498>`_ [VECr 22]: vppinfra:fix pcap write large file(> 0x80000000) error.
  | `37129 <https:////gerrit.fd.io/r/c/vpp/+/37129>`_ [VECr 25]: vlib: clib_panic if sysconf() can't determine page size on startup

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37518 <https:////gerrit.fd.io/r/c/vpp/+/37518>`_ [VECr 20]: wireguard: compute checksum for outer ipv6 header

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [veC 71]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".
  | `37068 <https:////gerrit.fd.io/r/c/vpp/+/37068>`_ [veC 74]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Aleksander Djuric** <aleksander.djuric@gmail.com>:

  | `24306 <https:////gerrit.fd.io/r/c/vpp/+/24306>`_ [veC 910]: dhcp: add nodns and nodefault params
  | `24309 <https:////gerrit.fd.io/r/c/vpp/+/24309>`_ [VeC 1014]: ip: ip4/ip6 local ping support
  | `24341 <https:////gerrit.fd.io/r/c/vpp/+/24341>`_ [VeC 1028]: fib: fib entry post install fix
  | `24424 <https:////gerrit.fd.io/r/c/vpp/+/24424>`_ [VeC 1028]: ip: fib headers refactoring
  | `23146 <https:////gerrit.fd.io/r/c/vpp/+/23146>`_ [VeC 1110]: vlib: add event-logger params delta/no-delta/date-time

**Alexander Gryanko** <xpahos@gmail.com>:

  | `13361 <https:////gerrit.fd.io/r/c/vpp/+/13361>`_ [veC 1447]: VOM: Add flush method to dump_cmd

**Alexander Kabaev** <kan@freebsd.org>:

  | `22272 <https:////gerrit.fd.io/r/c/vpp/+/22272>`_ [VeC 1113]: vlib: allow configuration for default rate limit

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEC 1]: arp: fix arp request for ip4-glean node

**Aloys Augustin** <aloaugus@cisco.com>:

  | `34844 <https:////gerrit.fd.io/r/c/vpp/+/34844>`_ [VeC 246]: misc: fix physmem allocation error handling
  | `27474 <https:////gerrit.fd.io/r/c/vpp/+/27474>`_ [veC 889]: ip: expose API to enable IP4 on an interface
  | `27460 <https:////gerrit.fd.io/r/c/vpp/+/27460>`_ [veC 891]: quic: WIP: improve scheduling
  | `27127 <https:////gerrit.fd.io/r/c/vpp/+/27127>`_ [veC 904]: ipsec: WIP: IPsec SA pinning experiment
  | `25996 <https:////gerrit.fd.io/r/c/vpp/+/25996>`_ [veC 971]: tap: improve default rx scheduling

**Anatoly Nikulin** <trotux@gmail.com>:

  | `31917 <https:////gerrit.fd.io/r/c/vpp/+/31917>`_ [veC 586]: acl: fix enabling interface counters

**Andreas Schultz** <aschultz@warp10.net>:

  | `27097 <https:////gerrit.fd.io/r/c/vpp/+/27097>`_ [VeC 914]: misc: pass NULL instead off 0 for pointer in variadic functions
  | `15798 <https:////gerrit.fd.io/r/c/vpp/+/15798>`_ [vec 939]: upf: Initial implementation of 3GPP TS 23.214 GTP-U UPF
  | `26038 <https:////gerrit.fd.io/r/c/vpp/+/26038>`_ [veC 970]: tcp: move options parse to separate reusable function
  | `25223 <https:////gerrit.fd.io/r/c/vpp/+/25223>`_ [vec 993]: docs: document alternate compression tools for core files

**Andrej Kozemcak** <andrej.kozemcak@pantheon.tech>:

  | `20489 <https:////gerrit.fd.io/r/c/vpp/+/20489>`_ [veC 1230]: DO_NOT_MERGE: Test build VOM packaged.
  | `16818 <https:////gerrit.fd.io/r/c/vpp/+/16818>`_ [VeC 1394]: Fix asserting in ip4_tcp_udp_compute_checksum.

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `37536 <https:////gerrit.fd.io/r/c/vpp/+/37536>`_ [vEC 20]: misc: VPP 22.10 Release Notes
  | `31368 <https:////gerrit.fd.io/r/c/vpp/+/31368>`_ [Vec 146]: vlib: Sleep less in unix input if there were active signals recently
  | `36377 <https:////gerrit.fd.io/r/c/vpp/+/36377>`_ [VeC 159]: tests: add libmemif tests
  | `36142 <https:////gerrit.fd.io/r/c/vpp/+/36142>`_ [veC 177]: build: add a check that "Fix" commits also refer to the commit that they are fixing
  | `35955 <https:////gerrit.fd.io/r/c/vpp/+/35955>`_ [Vec 216]: api: do not attempt to pass the null queue pointer from vl_api_can_send_msg
  | `34635 <https:////gerrit.fd.io/r/c/vpp/+/34635>`_ [VeC 293]: ip: punt socket - take the tags in Ethernet header into consideration
  | `26945 <https:////gerrit.fd.io/r/c/vpp/+/26945>`_ [veC 922]: (to be edited) expectations on tests for the test framework

**Andrey "Zed" Zaikin** <zmail11@gmail.com>:

  | `12748 <https:////gerrit.fd.io/r/c/vpp/+/12748>`_ [VeC 1635]: lb: add missing vip/as indexes to trace strings

**Arthas Kang** <arthas.kang@163.com>:

  | `31084 <https:////gerrit.fd.io/r/c/vpp/+/31084>`_ [veC 651]: plugin lb Fixed NAT4 SNAT invalid src_port ; Add NAT4 TCP SNAT support; Fixed NAT4 add SNAT map with protocol 0;

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 0]: ip: add support for buffer offload metadata in ip midchain
  | `37059 <https:////gerrit.fd.io/r/c/vpp/+/37059>`_ [VEc 1]: ipsec: new api for sa ips and ports updates

**Asumu Takikawa** <asumu@igalia.com>:

  | `16387 <https:////gerrit.fd.io/r/c/vpp/+/16387>`_ [veC 1433]: nat: fix issues in MAP-E port allocation mode
  | `16388 <https:////gerrit.fd.io/r/c/vpp/+/16388>`_ [veC 1440]: CSIT-541: add lwB4 functionality for lw4o6

**Atzm Watanabe** <atzmism@gmail.com>:

  | `36935 <https:////gerrit.fd.io/r/c/vpp/+/36935>`_ [VeC 70]: ikev2: accept rekey request for IKE SA
  | `35224 <https:////gerrit.fd.io/r/c/vpp/+/35224>`_ [VeC 281]: ikev2: fix profile_index for ikev2_sa_dump API

**Avinash Gonsalves** <avinash.gonsalves@nokia.com>:

  | `15084 <https:////gerrit.fd.io/r/c/vpp/+/15084>`_ [veC 644]: ipsec: add multicore crypto scheduler support

**Baruch Siach** <baruch@siach.name>:

  | `33935 <https:////gerrit.fd.io/r/c/vpp/+/33935>`_ [veC 408]: vppinfra: decode aarch64 PC in signal handler
  | `33934 <https:////gerrit.fd.io/r/c/vpp/+/33934>`_ [veC 408]: vppinfra: remove redundant local variables initialization

**Benoît Ganne** <bganne@cisco.com>:

  | `37416 <https:////gerrit.fd.io/r/c/vpp/+/37416>`_ [VeC 32]: virtio: add option to bind interface to uio driver
  | `37313 <https:////gerrit.fd.io/r/c/vpp/+/37313>`_ [VeC 35]: build: add sanitizer option to configure script

**Berenger Foucher** <berenger.foucher@stagiaires.ssi.gouv.fr>:

  | `14578 <https:////gerrit.fd.io/r/c/vpp/+/14578>`_ [veC 1537]: Add X509 authentication support to IKEv2 in VPP

**Bhishma Acharya** <bhishma@rtbrick.com>:

  | `36705 <https:////gerrit.fd.io/r/c/vpp/+/36705>`_ [VeC 110]: ip-neighbor: Fixed delay(1~2s) in neighbor-probe interval
  | `35927 <https:////gerrit.fd.io/r/c/vpp/+/35927>`_ [VeC 217]: fib: enhancement to support change table-id associated with fib-table

**Brant Lin** <brant.lin@ericsson.com>:

  | `14902 <https:////gerrit.fd.io/r/c/vpp/+/14902>`_ [veC 1517]: Fix the crash when creating the vapi context

**Carl Baldwin** <carl@ecbaldwin.net>:

  | `23528 <https:////gerrit.fd.io/r/c/vpp/+/23528>`_ [vec 1093]: docs: Remove redundancy on building VPP page

**Carl Smith** <carl.smith@alliedtelesis.co.nz>:

  | `23634 <https:////gerrit.fd.io/r/c/vpp/+/23634>`_ [VeC 1085]: ipip: return existing if_index if tunnel already exists.

**Chinmaya Agarwal** <chinmaya.agarwal@hsc.com>:

  | `33635 <https:////gerrit.fd.io/r/c/vpp/+/33635>`_ [VeC 439]: sr: fix added for returning correct value for behavior field in API message

**Chris Luke** <chris_luke@comcast.com>:

  | `9483 <https:////gerrit.fd.io/r/c/vpp/+/9483>`_ [VeC 1672]: PAPI unserializer for reply_in_shmem data (VPP-136)

**Christian Hopps** <chopps@chopps.org>:

  | `28657 <https:////gerrit.fd.io/r/c/vpp/+/28657>`_ [VeC 803]: misc: vpp_get_stats: add dump-machine formatting
  | `22353 <https:////gerrit.fd.io/r/c/vpp/+/22353>`_ [VeC 1112]: vlib: add option to use stderr instead of syslog.

**Clement Durand** <clement.durand@polytechnique.edu>:

  | `6274 <https:////gerrit.fd.io/r/c/vpp/+/6274>`_ [veC 1734]: elog: Text-format dump of event logs.

**Damjan Marion** <dmarion@0xa5.net>:

  | `36067 <https:////gerrit.fd.io/r/c/vpp/+/36067>`_ [VeC 196]: vppinfra: move cJSON and jsonformat to vlibmemory
  | `35155 <https:////gerrit.fd.io/r/c/vpp/+/35155>`_ [veC 278]: vppinfra: universal splats and aligned loads/stores
  | `34856 <https:////gerrit.fd.io/r/c/vpp/+/34856>`_ [veC 311]: ethernet: promisc refactor
  | `34845 <https:////gerrit.fd.io/r/c/vpp/+/34845>`_ [veC 312]: ethernet: add_del_mac and change_mac are ethernet specific

**Daniel Beres** <daniel.beres@pantheon.tech>:

  | `34628 <https:////gerrit.fd.io/r/c/vpp/+/34628>`_ [VeC 309]: dns: support AAAA over IPV4

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 73]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37420 <https:////gerrit.fd.io/r/c/vpp/+/37420>`_ [VEc 10]: tests: remove intermittent failing tests on vpp_debug image

**David Johnson** <davijoh3@cisco.com>:

  | `16670 <https:////gerrit.fd.io/r/c/vpp/+/16670>`_ [veC 1390]: Fix various -Wmaybe-uninitialized and -Wstrict-overflow warnings

**Dmitry Vakhrushev** <dmitry@netgate.com>:

  | `25502 <https:////gerrit.fd.io/r/c/vpp/+/25502>`_ [Vec 546]: interface: getting interface device specific info

**Dmitry Valter** <dvalter@protonmail.com>:

  | `34694 <https:////gerrit.fd.io/r/c/vpp/+/34694>`_ [VeC 221]: vlib: remove process restart cli
  | `34800 <https:////gerrit.fd.io/r/c/vpp/+/34800>`_ [VeC 229]: vppinfra: fix non-zero offsets to NULL pointer

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 32]: dpdk: use adapter MTU in max_frame_size setting

**Ed Kern** <ejk@cisco.com>:

  | `20442 <https:////gerrit.fd.io/r/c/vpp/+/20442>`_ [veC 1233]: build: do not merge

**Feng Gao** <davidfgao@tencent.com>:

  | `26296 <https:////gerrit.fd.io/r/c/vpp/+/26296>`_ [veC 957]: ipsec: Correct inconsistent alignment for crypto_op

**Filip Tehlar** <ftehlar@cisco.com>:

  | `37646 <https:////gerrit.fd.io/r/c/vpp/+/37646>`_ [VEc 1]: tests: add VCL Thru Host Stack TLS in interrupt mode

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [vEC 20]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [vEC 20]: nat: nat44-ed update timeout api
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [vEC 20]: nat: det44 map configuration improvements

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37361 <https:////gerrit.fd.io/r/c/vpp/+/37361>`_ [VEc 21]: wireguard: add atomic mutex
  | `32655 <https:////gerrit.fd.io/r/c/vpp/+/32655>`_ [VeC 522]: crypto: fix possible frame resize

**Gary Boon** <gboon@cisco.com>:

  | `30522 <https:////gerrit.fd.io/r/c/vpp/+/30522>`_ [veC 694]: Add callback support for the dispatch node.
  | `30239 <https:////gerrit.fd.io/r/c/vpp/+/30239>`_ [veC 713]: Add a new function to the MCAP logic that allows a custom header to be added on top of the data in a vlib buffer.
  | `25517 <https:////gerrit.fd.io/r/c/vpp/+/25517>`_ [VeC 992]: vlib: check for null handoff queue element in vlib_buffer_enqueue_to_thread

**Gerard Keown** <gerard.keown@enea.com>:

  | `24369 <https:////gerrit.fd.io/r/c/vpp/+/24369>`_ [veC 1034]: cores: mismatching "worker" & "corelist-workers" parameters can cause coredump

**Govindarajan Mohandoss** <govindarajan.mohandoss@arm.com>:

  | `28164 <https:////gerrit.fd.io/r/c/vpp/+/28164>`_ [veC 826]: acl: ACL Plugin performance improvement for both SF and SL modes
  | `27167 <https:////gerrit.fd.io/r/c/vpp/+/27167>`_ [veC 902]: acl: ACL Plugin performance improvement for both SF and SL modes

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `37248 <https:////gerrit.fd.io/r/c/vpp/+/37248>`_ [VeC 49]: urpf: add show urpf cli
  | `34726 <https:////gerrit.fd.io/r/c/vpp/+/34726>`_ [VeC 102]: interface: add buffer stats api

**Hemant Singh** <hemant@mnkcg.com>:

  | `32077 <https:////gerrit.fd.io/r/c/vpp/+/32077>`_ [veC 466]: fixstyle
  | `32023 <https:////gerrit.fd.io/r/c/vpp/+/32023>`_ [veC 573]: ip-neighbor: Add ip_neighbor_find_entry with ip+interface key

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37585 <https:////gerrit.fd.io/r/c/vpp/+/37585>`_ [VEc 0]: classify: fix crash when delete classify table used by interface.

**IJsbrand Wijnands** <iwijnand@cisco.com>:

  | `25696 <https:////gerrit.fd.io/r/c/vpp/+/25696>`_ [veC 985]: mpls: add user defined name tag to mpls tunnels
  | `25678 <https:////gerrit.fd.io/r/c/vpp/+/25678>`_ [veC 985]: tap: tap dev_name and default value for bin api
  | `25677 <https:////gerrit.fd.io/r/c/vpp/+/25677>`_ [veC 985]: tap: tap dev_name and default value for bin api

**Ignas Bačius** <ignas@noia.network>:

  | `22733 <https:////gerrit.fd.io/r/c/vpp/+/22733>`_ [VeC 1107]: gre: allow to delete tunnel by sw_if_index
  | `22666 <https:////gerrit.fd.io/r/c/vpp/+/22666>`_ [VeC 1128]: ip: fix possible use of uninitialized variable

**Igor Mikhailov** <imichail@cisco.com>:

  | `15131 <https:////gerrit.fd.io/r/c/vpp/+/15131>`_ [VeC 1471]: Ensure VPP library version has 2 digits separated by dot.

**Ilia Abashin** <abashinos@gmail.com>:

  | `20234 <https:////gerrit.fd.io/r/c/vpp/+/20234>`_ [veC 1244]: Updated vpp_if_stats to latest version, including fresh documentation

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `36592 <https:////gerrit.fd.io/r/c/vpp/+/36592>`_ [VeC 133]: stats: handle interface renames properly
  | `36590 <https:////gerrit.fd.io/r/c/vpp/+/36590>`_ [VeC 133]: nat: fix handling checksum offload in nat44-ed
  | `28085 <https:////gerrit.fd.io/r/c/vpp/+/28085>`_ [Vec 840]: hsa: fix proxy crash upon failed connect

**Jack Xu** <jack.c.xu@ericsson.com>:

  | `18406 <https:////gerrit.fd.io/r/c/vpp/+/18406>`_ [veC 1333]: fix multi-enable bug of enable feature function

**Jakub Grajciar** <jgrajcia@cisco.com>:

  | `30575 <https:////gerrit.fd.io/r/c/vpp/+/30575>`_ [VeC 398]: libmemif: add shm debug APIs
  | `28175 <https:////gerrit.fd.io/r/c/vpp/+/28175>`_ [Vec 544]: api: implement api for api trace
  | `30216 <https:////gerrit.fd.io/r/c/vpp/+/30216>`_ [vec 712]: tests: remove sr_mpls from vpp_papi_provider and add sr_mpls object models
  | `30125 <https:////gerrit.fd.io/r/c/vpp/+/30125>`_ [Vec 714]: tests: remove igmp from vpp_papi_provider and refactor igmp object models

**Jakub Havas** <jakub.havas@pantheon.tech>:

  | `33130 <https:////gerrit.fd.io/r/c/vpp/+/33130>`_ [VeC 488]: udp: create an api to dump decaps
  | `32948 <https:////gerrit.fd.io/r/c/vpp/+/32948>`_ [veC 504]: ipfix-export: replace cli command with an implemented api function

**Jan Cavojsky** <jan.cavojsky@pantheon.tech>:

  | `28899 <https:////gerrit.fd.io/r/c/vpp/+/28899>`_ [veC 648]: flowprobe: add API dump of params and list of interfaces for recording
  | `25992 <https:////gerrit.fd.io/r/c/vpp/+/25992>`_ [veC 707]: libmemif: update example applications and documentation
  | `28988 <https:////gerrit.fd.io/r/c/vpp/+/28988>`_ [VeC 784]: vat: avoid crash vpp after command ip_table_dump

**Jason Zhang** <jason.zhang2@arm.com>:

  | `22355 <https:////gerrit.fd.io/r/c/vpp/+/22355>`_ [VeC 1110]: vppinfra: change CLIB_MEMORY_BARRIER to use C11 built-in atomic APIs

**Jasvinder Singh** <jasvinder.singh@intel.com>:

  | `16839 <https:////gerrit.fd.io/r/c/vpp/+/16839>`_ [VeC 1363]: HQoS: update scheduler to support mbuf sched field change

**Jawahar Gundapaneni** <jgundapa@cisco.com>:

  | `25995 <https:////gerrit.fd.io/r/c/vpp/+/25995>`_ [vec 693]: interface: Upstream TAP I/fs with ADMIN_UP
  | `26121 <https:////gerrit.fd.io/r/c/vpp/+/26121>`_ [vec 958]: memif: CLI to debug memif buffer contents

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 76]: vppapigen: fix json build error

**Jing Peng** <pj.hades@gmail.com>:

  | `36186 <https:////gerrit.fd.io/r/c/vpp/+/36186>`_ [VeC 179]: nat: fix nat44 fib reference count bookkeeping
  | `36062 <https:////gerrit.fd.io/r/c/vpp/+/36062>`_ [VeC 201]: vppinfra: fix duplicate bihash stat update
  | `36042 <https:////gerrit.fd.io/r/c/vpp/+/36042>`_ [VeC 203]: vppinfra: add bihash update interface

**John Lo** <lojultra2020@outlook.com>:

  | `14858 <https:////gerrit.fd.io/r/c/vpp/+/14858>`_ [veC 1499]: Bring back original l2-output node function

**Jordy You** <jordy.you@ericsson.com>:

  | `13016 <https:////gerrit.fd.io/r/c/vpp/+/13016>`_ [VeC 1517]: fix ip checksum issue for odd start address
  | `13002 <https:////gerrit.fd.io/r/c/vpp/+/13002>`_ [veC 1617]: fix ip checksum issue for odd start address if the input data is starting with an odd address,then the calcuation will be error

**Julius Milan** <julius.milan@pantheon.tech>:

  | `29050 <https:////gerrit.fd.io/r/c/vpp/+/29050>`_ [vec 647]: papi: fix name vector stats entry dump
  | `29030 <https:////gerrit.fd.io/r/c/vpp/+/29030>`_ [veC 707]: nat: add per host counters into det44
  | `29029 <https:////gerrit.fd.io/r/c/vpp/+/29029>`_ [VeC 783]: stats: enable setting of name vectors for plugins
  | `29028 <https:////gerrit.fd.io/r/c/vpp/+/29028>`_ [VeC 783]: stats: fix dump of null data entries
  | `25785 <https:////gerrit.fd.io/r/c/vpp/+/25785>`_ [veC 964]: vppinfra: add bitmap search next bit on interval

**Junfeng Wang** <drenfong.wang@intel.com>:

  | `31581 <https:////gerrit.fd.io/r/c/vpp/+/31581>`_ [veC 606]: pppoe: init the variable of result0 result1
  | `29975 <https:////gerrit.fd.io/r/c/vpp/+/29975>`_ [veC 720]: l2: l2output avx512
  | `30117 <https:////gerrit.fd.io/r/c/vpp/+/30117>`_ [veC 720]: l2: test

**Kai Luo** <kailuo.nk@gmail.com>:

  | `37269 <https:////gerrit.fd.io/r/c/vpp/+/37269>`_ [VeC 38]: memif: fix uninitialized variable warning

**Keith Burns** <alagalah@gmail.com>:

  | `22368 <https:////gerrit.fd.io/r/c/vpp/+/22368>`_ [VeC 1144]: vat : VLAN subif formatter accepting 'vlan'       instead of 'vlan_id'

**Kevin Wang** <kevin.wang@arm.com>:

  | `10293 <https:////gerrit.fd.io/r/c/vpp/+/10293>`_ [veC 1750]: vppinfra: use __atomic_fetch_add instead of __sync_fetch_and_add builtins

**King Ma** <kinma@cisco.com>:

  | `20390 <https:////gerrit.fd.io/r/c/vpp/+/20390>`_ [VeC 939]: ip: make reassembled packet to preserve ip.fib_index

**Kingwel Xie** <kingwel.xie@ericsson.com>:

  | `16617 <https:////gerrit.fd.io/r/c/vpp/+/16617>`_ [veC 1345]: perfmon: improvement, HW_CACHE events
  | `16910 <https:////gerrit.fd.io/r/c/vpp/+/16910>`_ [veC 1395]: pg: improved unformat_user to show accurate error message

**Kiran Shastri** <shastrinator@gmail.com>:

  | `20445 <https:////gerrit.fd.io/r/c/vpp/+/20445>`_ [veC 1226]: Fix git usage in vom build scripts

**Klement Sekera** <klement.sekera@gmail.com>:

  | `35739 <https:////gerrit.fd.io/r/c/vpp/+/35739>`_ [veC 237]: tests: refactor assert*counter_equal APIs
  | `35218 <https:////gerrit.fd.io/r/c/vpp/+/35218>`_ [veC 283]: tests: prevent running as root
  | `32435 <https:////gerrit.fd.io/r/c/vpp/+/32435>`_ [veC 288]: nat: enhance test - make sure all workers are hit
  | `33507 <https:////gerrit.fd.io/r/c/vpp/+/33507>`_ [VeC 294]: nat: properly handle truncated packets
  | `27083 <https:////gerrit.fd.io/r/c/vpp/+/27083>`_ [veC 915]: nat: "users" dump for ED-NAT

**Korian Edeline** <korian.edeline@ulg.ac.be>:

  | `14083 <https:////gerrit.fd.io/r/c/vpp/+/14083>`_ [veC 1560]: consistent output for bitmap next_set&next_clear

**Kyeong Min Park** <pak2536@gmail.com>:

  | `30960 <https:////gerrit.fd.io/r/c/vpp/+/30960>`_ [veC 650]: memif: fix invalid next_index selection

**Leung Lai Yung** <benkerbuild@gmail.com>:

  | `36128 <https:////gerrit.fd.io/r/c/vpp/+/36128>`_ [VeC 184]: vppinfra: remove unused line

**Luo Yaozu** <luoyaozu@foxmail.com>:

  | `37073 <https:////gerrit.fd.io/r/c/vpp/+/37073>`_ [veC 71]: ip neighbor: fix debug log format output

**Mauricio Solis** <mauricio.solisjr@tno.nl>:

  | `29862 <https:////gerrit.fd.io/r/c/vpp/+/29862>`_ [VeC 268]: ip6 ioam: updated iOAM plugin based on https://github.com/inband-oam/ietf/blob/master/drafts/versions/03/draft-ietf-ippm-ioam-ipv6-options-03.txt and https://tools.ietf.org/html/draft-ietf-ippm-ioam-data-10

**Mercury Noah** <mercury124185@gmail.com>:

  | `36492 <https:////gerrit.fd.io/r/c/vpp/+/36492>`_ [VeC 144]: ip6-nd: fix ip6-nd proxy issue
  | `35916 <https:////gerrit.fd.io/r/c/vpp/+/35916>`_ [VeC 216]: arp: fix the arp proxy issue

**Michael Yu** <michael.a.yu@nokia-sbell.com>:

  | `30454 <https:////gerrit.fd.io/r/c/vpp/+/30454>`_ [VeC 698]: devices: fix af-packet device TX stuck issue

**Michal Kalderon** <mkalderon@marvell.com>:

  | `34795 <https:////gerrit.fd.io/r/c/vpp/+/34795>`_ [vec 322]: svm: Fix chunk allocation when data_size is larger than max chunk size

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `34873 <https:////gerrit.fd.io/r/c/vpp/+/34873>`_ [VeC 309]: nat: reliable TCP conn close in NAT44-ed
  | `34851 <https:////gerrit.fd.io/r/c/vpp/+/34851>`_ [VeC 312]: nat: reliable TCP conn establishment in NAT44-ed

**Mohammed Alshohayeb** <mshohayeb@wirefilter.com>:

  | `16470 <https:////gerrit.fd.io/r/c/vpp/+/16470>`_ [veC 1413]: docs: clarify doxygen vec _align behaviour.

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `37505 <https:////gerrit.fd.io/r/c/vpp/+/37505>`_ [vEC 25]: gso: add gso documentation
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VeC 47]: gso: use the header offsets from buffer metadata
  | `36513 <https:////gerrit.fd.io/r/c/vpp/+/36513>`_ [VeC 140]: libmemif: add the binaries in the packaging
  | `36484 <https:////gerrit.fd.io/r/c/vpp/+/36484>`_ [VeC 146]: libmemif: add testing application
  | `36296 <https:////gerrit.fd.io/r/c/vpp/+/36296>`_ [veC 169]: pg: fix the use of hdr offsets in buffer metadata
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [veC 183]: devices: add cli support to enable disable qdisc bypass
  | `35912 <https:////gerrit.fd.io/r/c/vpp/+/35912>`_ [VeC 221]: interface: fix the processing levels
  | `34517 <https:////gerrit.fd.io/r/c/vpp/+/34517>`_ [Vec 365]: hash: fix the Extension Header for ipv6 in crc32_5tuples
  | `32837 <https:////gerrit.fd.io/r/c/vpp/+/32837>`_ [veC 511]: gso: improve interface handling
  | `31700 <https:////gerrit.fd.io/r/c/vpp/+/31700>`_ [VeC 603]: interface: rename runtime data func

**Nathan Moos** <nmoos@cisco.com>:

  | `30792 <https:////gerrit.fd.io/r/c/vpp/+/30792>`_ [Vec 659]: build: add config option for LD_PRELOAD

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 40]: vppinfra: improve & test abstract socket
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [veC 46]: cnat: dont compute offloaded cksums
  | `32820 <https:////gerrit.fd.io/r/c/vpp/+/32820>`_ [VeC 46]: cnat: better cnat snat-policy cli
  | `33264 <https:////gerrit.fd.io/r/c/vpp/+/33264>`_ [VeC 46]: pbl: Port based balancer
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 46]: cnat: add ip/client bihash
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 46]: cnat: remove rwlock on ts
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 46]: cnat: flag to disable rsession
  | `35805 <https:////gerrit.fd.io/r/c/vpp/+/35805>`_ [VeC 46]: dpdk: add intf tag to dev{} subinput
  | `34734 <https:////gerrit.fd.io/r/c/vpp/+/34734>`_ [VeC 120]: memif: autogenerate socket_ids
  | `34552 <https:////gerrit.fd.io/r/c/vpp/+/34552>`_ [VeC 313]: cnat: add single lookup

**Naveen Joy** <najoy@cisco.com>:

  | `33000 <https:////gerrit.fd.io/r/c/vpp/+/33000>`_ [VeC 501]: tests: alternative log directory for unittest logs
  | `31937 <https:////gerrit.fd.io/r/c/vpp/+/31937>`_ [vec 578]: tests: enable make test to be run inside a VM
  | `18602 <https:////gerrit.fd.io/r/c/vpp/+/18602>`_ [VeC 1125]: tests: fixes test_bier_e2e_64 for python3
  | `22817 <https:////gerrit.fd.io/r/c/vpp/+/22817>`_ [VeC 1125]: tests: fix scapy error when using python3
  | `18606 <https:////gerrit.fd.io/r/c/vpp/+/18606>`_ [veC 1324]: fixes TypeError raised by the framework when using python3
  | `18128 <https:////gerrit.fd.io/r/c/vpp/+/18128>`_ [VeC 1348]: make-test: apply common PEP8 style conventions

**Neale Ranns** <neale@graphiant.com>:

  | `36821 <https:////gerrit.fd.io/r/c/vpp/+/36821>`_ [VeC 96]: vlib: "sh errors" shows error severity counters
  | `35436 <https:////gerrit.fd.io/r/c/vpp/+/35436>`_ [VeC 256]: qos: Dual loop the QoS record node
  | `34686 <https:////gerrit.fd.io/r/c/vpp/+/34686>`_ [vec 342]: dependency: Create the dependency graph tracking infra. A simple cut-n-paste of what is already present in FIB
  | `34687 <https:////gerrit.fd.io/r/c/vpp/+/34687>`_ [VeC 342]: fib: Remove the fib graph dependency code
  | `34688 <https:////gerrit.fd.io/r/c/vpp/+/34688>`_ [VeC 343]: dependency: Dpendency tracking improvements
  | `34689 <https:////gerrit.fd.io/r/c/vpp/+/34689>`_ [veC 344]: interface: Add a dependency node to a SW interface fib: update the adjacnecy subsystem to use interface dependency tracking
  | `33510 <https:////gerrit.fd.io/r/c/vpp/+/33510>`_ [VeC 455]: tests: Test for ARP behaviour on links with a /32 configured
  | `32770 <https:////gerrit.fd.io/r/c/vpp/+/32770>`_ [VeC 462]: ip: A weak host mode for IPv6
  | `26811 <https:////gerrit.fd.io/r/c/vpp/+/26811>`_ [Vec 468]: ipsec: Make Add/Del SA MP safe
  | `32760 <https:////gerrit.fd.io/r/c/vpp/+/32760>`_ [VeC 502]: fib: tunnel: Pin a tunnel's egress interface to its source
  | `30412 <https:////gerrit.fd.io/r/c/vpp/+/30412>`_ [veC 545]: ethernet: Ether types on the API
  | `27086 <https:////gerrit.fd.io/r/c/vpp/+/27086>`_ [Vec 545]: ip: ip6 rewrite performance bump
  | `31428 <https:////gerrit.fd.io/r/c/vpp/+/31428>`_ [veC 573]: ipsec: Remove the backend infra
  | `31397 <https:////gerrit.fd.io/r/c/vpp/+/31397>`_ [VeC 578]: vppapigen: Support an 'mpsafe' keyword on the API
  | `31695 <https:////gerrit.fd.io/r/c/vpp/+/31695>`_ [veC 593]: teib: Fix fib-index for nh and peer
  | `31780 <https:////gerrit.fd.io/r/c/vpp/+/31780>`_ [Vec 595]: dpdk: Fix the handling of failed burst enqueues for crypto ops
  | `31788 <https:////gerrit.fd.io/r/c/vpp/+/31788>`_ [VeC 596]: ip: Repeat ip4 prefetch strategy for ip6 in rewrite
  | `30141 <https:////gerrit.fd.io/r/c/vpp/+/30141>`_ [veC 714]: tests: Sum stats over all threads
  | `29494 <https:////gerrit.fd.io/r/c/vpp/+/29494>`_ [veC 756]: devices: NULL device
  | `29310 <https:////gerrit.fd.io/r/c/vpp/+/29310>`_ [veC 768]: pg: Coverity warning of uninitialised variable
  | `28966 <https:////gerrit.fd.io/r/c/vpp/+/28966>`_ [veC 785]: misc: lawful-intercept Move to plugin
  | `26693 <https:////gerrit.fd.io/r/c/vpp/+/26693>`_ [veC 935]: ip: Dedicated ip[46] rewrite nodes for tagged traffic
  | `25973 <https:////gerrit.fd.io/r/c/vpp/+/25973>`_ [vec 972]: tests: Do not use randomly named directories for test results
  | `24135 <https:////gerrit.fd.io/r/c/vpp/+/24135>`_ [veC 1054]: ip: Vectorized mtrie lookup
  | `18739 <https:////gerrit.fd.io/r/c/vpp/+/18739>`_ [veC 1314]: Copyright update check
  | `17086 <https:////gerrit.fd.io/r/c/vpp/+/17086>`_ [veC 1388]: L2-FIB: make the result 16 bytes

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `26617 <https:////gerrit.fd.io/r/c/vpp/+/26617>`_ [Vec 900]: gtpu geneve vxlan vxlan-gpe vxlan-gbp: DPO leak
  | `25691 <https:////gerrit.fd.io/r/c/vpp/+/25691>`_ [vec 913]: gtpu: fix encap_vrf_id conversion in binapi handler

**Nitin Saxena** <nsaxena@marvell.com>:

  | `28643 <https:////gerrit.fd.io/r/c/vpp/+/28643>`_ [VeC 804]: interface: Fix possible memleaks in standard APIs

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `37268 <https:////gerrit.fd.io/r/c/vpp/+/37268>`_ [VeC 33]: lb: add source ip based sticky load balancing

**Ole Troan** <otroan@employees.org>:

  | `33819 <https:////gerrit.fd.io/r/c/vpp/+/33819>`_ [veC 393]: api: binary-api-json command to call api from vpp cli
  | `33518 <https:////gerrit.fd.io/r/c/vpp/+/33518>`_ [veC 419]: vat: disable vat linked into vpp by default
  | `31656 <https:////gerrit.fd.io/r/c/vpp/+/31656>`_ [VeC 538]: vpp: api to get connection information
  | `30484 <https:////gerrit.fd.io/r/c/vpp/+/30484>`_ [veC 540]: api: crcchecker list messages marked deprecated that can be removed
  | `28822 <https:////gerrit.fd.io/r/c/vpp/+/28822>`_ [veC 595]: api: show api message-table deprecated

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `16356 <https:////gerrit.fd.io/r/c/vpp/+/16356>`_ [veC 1427]: Python 3 supporting PAPI rpm

**Parham Fisher** <s3m2e1.6star@gmail.com>:

  | `16201 <https:////gerrit.fd.io/r/c/vpp/+/16201>`_ [VeC 939]: ip_reassembly_enable_disable vat command is added.
  | `20308 <https:////gerrit.fd.io/r/c/vpp/+/20308>`_ [veC 1233]: nat: If a feature like abf is enabled,      the next node of nat44-out2in is not ip4-lookup.      so I find next node using vnet_feature_next.
  | `15173 <https:////gerrit.fd.io/r/c/vpp/+/15173>`_ [veC 1499]: initialize next0, because of following compile error: ‘next0’ may be used uninitialized in this function [-Werror=maybe-uninitialized]
  | `14848 <https:////gerrit.fd.io/r/c/vpp/+/14848>`_ [veC 1520]: speed and duplex must set when link is up, otherwise the value of them is unknown.

**Paul Vinciguerra** <pvinci@vinciconsulting.com>:

  | `24082 <https:////gerrit.fd.io/r/c/vpp/+/24082>`_ [veC 537]: vlib: log - fix input handling of 'default' subclass
  | `30545 <https:////gerrit.fd.io/r/c/vpp/+/30545>`_ [veC 540]: tests: refactor gbp tests
  | `26832 <https:////gerrit.fd.io/r/c/vpp/+/26832>`_ [veC 540]: vxlan-gpe: update api defaults/fix protocol
  | `26150 <https:////gerrit.fd.io/r/c/vpp/+/26150>`_ [VeC 545]: build: fix make 'install-deps' on fresh container
  | `31997 <https:////gerrit.fd.io/r/c/vpp/+/31997>`_ [VeC 545]: build: fix missing clang dependency in make install-dep
  | `27349 <https:////gerrit.fd.io/r/c/vpp/+/27349>`_ [VeC 545]: libmemif:  don't redefine _GNU_SOURCE
  | `27351 <https:////gerrit.fd.io/r/c/vpp/+/27351>`_ [veC 545]: libmemif: fix dockerfile for examples
  | `31999 <https:////gerrit.fd.io/r/c/vpp/+/31999>`_ [veC 549]: acl:  remove VppAclPlugin from vpp_acl.py
  | `32199 <https:////gerrit.fd.io/r/c/vpp/+/32199>`_ [veC 560]: tests: fix IndexError in framework.py
  | `32198 <https:////gerrit.fd.io/r/c/vpp/+/32198>`_ [VeC 560]: tests: fix resource leaks in vpp_pg_interface.py
  | `32117 <https:////gerrit.fd.io/r/c/vpp/+/32117>`_ [VeC 561]: tests: move ip neighbor code from vpp_papi_provider
  | `32119 <https:////gerrit.fd.io/r/c/vpp/+/32119>`_ [veC 568]: tests: clean up ipfix_exporter from vpp_papi_provider
  | `32118 <https:////gerrit.fd.io/r/c/vpp/+/32118>`_ [veC 568]: tests: cleanup udp_encap from vpp_papi_provider
  | `32005 <https:////gerrit.fd.io/r/c/vpp/+/32005>`_ [veC 578]: api:  set missing default values for is_add fields
  | `31998 <https:////gerrit.fd.io/r/c/vpp/+/31998>`_ [VeC 579]: arping: fix vat_help typo in api file
  | `27353 <https:////gerrit.fd.io/r/c/vpp/+/27353>`_ [veC 637]: build: add make targets for vom/libmemif
  | `31296 <https:////gerrit.fd.io/r/c/vpp/+/31296>`_ [veC 637]: misc: whitespace changes from clang-format-10
  | `31295 <https:////gerrit.fd.io/r/c/vpp/+/31295>`_ [VeC 638]: misc: remove indent-on linter
  | `26178 <https:////gerrit.fd.io/r/c/vpp/+/26178>`_ [veC 640]: api: add msg_id to 'client input queue is stuffed...' message
  | `30546 <https:////gerrit.fd.io/r/c/vpp/+/30546>`_ [veC 641]: vxlan-gbp: add interface_name to dump/details to use VppVxlanGbpTunnel
  | `26873 <https:////gerrit.fd.io/r/c/vpp/+/26873>`_ [veC 641]: misc: vom - fix variable name in dhcp_client_cmds bind_cmd
  | `24570 <https:////gerrit.fd.io/r/c/vpp/+/24570>`_ [veC 641]: gbp: set VNID_INVALID to last value in range
  | `23018 <https:////gerrit.fd.io/r/c/vpp/+/23018>`_ [veC 641]: devices: add context around console messages
  | `26871 <https:////gerrit.fd.io/r/c/vpp/+/26871>`_ [veC 641]: misc: vom - cleanup typos for doxygen
  | `26833 <https:////gerrit.fd.io/r/c/vpp/+/26833>`_ [veC 641]: tests: refactor VppInterface
  | `26872 <https:////gerrit.fd.io/r/c/vpp/+/26872>`_ [veC 641]: misc: vom - fix typo in gbp-endpoint-create: to_string
  | `26291 <https:////gerrit.fd.io/r/c/vpp/+/26291>`_ [vec 641]: tests: add tests for ip.api
  | `30551 <https:////gerrit.fd.io/r/c/vpp/+/30551>`_ [vec 641]: misc: fix typo in foreach_vnet_api_error
  | `30361 <https:////gerrit.fd.io/r/c/vpp/+/30361>`_ [veC 641]: papi: refactor client to decouple dependency on transport
  | `30401 <https:////gerrit.fd.io/r/c/vpp/+/30401>`_ [Vec 641]: papi: only build python3 binary distributions
  | `30350 <https:////gerrit.fd.io/r/c/vpp/+/30350>`_ [veC 641]: papi: calculate function properties once
  | `30360 <https:////gerrit.fd.io/r/c/vpp/+/30360>`_ [veC 641]: papi: mark apifiles option of VPPApiClient as non-optional
  | `30220 <https:////gerrit.fd.io/r/c/vpp/+/30220>`_ [veC 641]: vapi: cleanup nits in vapi doc
  | `24131 <https:////gerrit.fd.io/r/c/vpp/+/24131>`_ [VeC 685]: vlib: add LSB standard exit codes if vpp doesn't start properly
  | `21208 <https:////gerrit.fd.io/r/c/vpp/+/21208>`_ [veC 699]: tests: don't pin python dependencies
  | `30435 <https:////gerrit.fd.io/r/c/vpp/+/30435>`_ [veC 699]: tests: fix node variant tests
  | `30343 <https:////gerrit.fd.io/r/c/vpp/+/30343>`_ [veC 707]: api: remove [backwards_compatable] option and bump semver
  | `30289 <https:////gerrit.fd.io/r/c/vpp/+/30289>`_ [veC 711]: tests:  split wireguard tests from configuation classes
  | `26703 <https:////gerrit.fd.io/r/c/vpp/+/26703>`_ [veC 711]: tests: fix memif ping
  | `29938 <https:////gerrit.fd.io/r/c/vpp/+/29938>`_ [VeC 714]: tests: refactor debug_internal into subclass of VppTestCase
  | `30078 <https:////gerrit.fd.io/r/c/vpp/+/30078>`_ [veC 723]: tests: vpp_papi EXPERIMENT Do not merge!!!
  | `25727 <https:////gerrit.fd.io/r/c/vpp/+/25727>`_ [VeC 913]: papi: build setup under python3
  | `26886 <https:////gerrit.fd.io/r/c/vpp/+/26886>`_ [veC 924]: vom: update .clang-format
  | `26225 <https:////gerrit.fd.io/r/c/vpp/+/26225>`_ [VeC 961]: vppapigen: for vat plugins, use local_logger
  | `24573 <https:////gerrit.fd.io/r/c/vpp/+/24573>`_ [VeC 1022]: ethernet: create unique default loopback mac-addresses
  | `24132 <https:////gerrit.fd.io/r/c/vpp/+/24132>`_ [VeC 1041]: tests:  improve checks for test_tap
  | `23555 <https:////gerrit.fd.io/r/c/vpp/+/23555>`_ [VeC 1042]: tests: ensure host has enough cores for test
  | `24189 <https:////gerrit.fd.io/r/c/vpp/+/24189>`_ [VeC 1047]: tests: refactor QUICAppWorker
  | `24107 <https:////gerrit.fd.io/r/c/vpp/+/24107>`_ [veC 1047]: tests: Experiment - log info in case of startUpClass failure
  | `24159 <https:////gerrit.fd.io/r/c/vpp/+/24159>`_ [veC 1048]: tests: vlib - remove set pmc instructions-per-clock
  | `23755 <https:////gerrit.fd.io/r/c/vpp/+/23755>`_ [vec 1048]: papi tests: add ability for test to connect via vapi socket
  | `23349 <https:////gerrit.fd.io/r/c/vpp/+/23349>`_ [veC 1054]: build: add python imports to 'make checkstyle'
  | `24114 <https:////gerrit.fd.io/r/c/vpp/+/24114>`_ [veC 1054]: tests:  use flake8 for 'make test-checkstyle'
  | `24087 <https:////gerrit.fd.io/r/c/vpp/+/24087>`_ [veC 1061]: tests: ip6 add comments in SLAAC test
  | `23030 <https:////gerrit.fd.io/r/c/vpp/+/23030>`_ [veC 1062]: tests: enable dpdk plugin
  | `23488 <https:////gerrit.fd.io/r/c/vpp/+/23488>`_ [veC 1070]: tests: don't try to remove vpp_config without conn to api.
  | `23951 <https:////gerrit.fd.io/r/c/vpp/+/23951>`_ [Vec 1070]: vppapigen: fix for explicit types
  | `23664 <https:////gerrit.fd.io/r/c/vpp/+/23664>`_ [veC 1079]: tests:  skip test if can't run worker executable
  | `23491 <https:////gerrit.fd.io/r/c/vpp/+/23491>`_ [veC 1081]: tests: fix run_test exception
  | `23697 <https:////gerrit.fd.io/r/c/vpp/+/23697>`_ [veC 1082]: tests: change vapi_response_timeout in cli test
  | `23490 <https:////gerrit.fd.io/r/c/vpp/+/23490>`_ [VeC 1083]: tests: framework VppDiedError - handle vpp hung
  | `23521 <https:////gerrit.fd.io/r/c/vpp/+/23521>`_ [veC 1084]: tests: vpp_pg_interface.py don't let OSError impact subsequent tests
  | `17251 <https:////gerrit.fd.io/r/c/vpp/+/17251>`_ [veC 1086]: Dependencies test: Do not commit!
  | `23487 <https:////gerrit.fd.io/r/c/vpp/+/23487>`_ [veC 1090]: tests: don't introduce changes that link VppTestCase and run_tests.py
  | `23492 <https:////gerrit.fd.io/r/c/vpp/+/23492>`_ [veC 1093]: tests: no longer allow bare "except:"'s
  | `23314 <https:////gerrit.fd.io/r/c/vpp/+/23314>`_ [veC 1104]: vpp: update 'ip virtual' short help to match parser
  | `23125 <https:////gerrit.fd.io/r/c/vpp/+/23125>`_ [veC 1110]: crypto-openssl: show opennssl version name
  | `23068 <https:////gerrit.fd.io/r/c/vpp/+/23068>`_ [veC 1111]: pg: expand interface name in show packet-generator
  | `23031 <https:////gerrit.fd.io/r/c/vpp/+/23031>`_ [veC 1112]: tests: remove python2isms from framework.py
  | `20292 <https:////gerrit.fd.io/r/c/vpp/+/20292>`_ [veC 1153]: tests: have test_flowprobe.py use existing api calls
  | `20632 <https:////gerrit.fd.io/r/c/vpp/+/20632>`_ [veC 1193]: tests: improve ipsec test performance
  | `20945 <https:////gerrit.fd.io/r/c/vpp/+/20945>`_ [VeC 1204]: vapi: fix vapi_c_gen.py suport for defaults
  | `19522 <https:////gerrit.fd.io/r/c/vpp/+/19522>`_ [Vec 1204]: api:  return errorcode cli_inband
  | `20266 <https:////gerrit.fd.io/r/c/vpp/+/20266>`_ [veC 1210]: tests: refactor CliFailedCommandError
  | `20484 <https:////gerrit.fd.io/r/c/vpp/+/20484>`_ [Vec 1210]: misc: add dependency info to commit template
  | `20619 <https:////gerrit.fd.io/r/c/vpp/+/20619>`_ [veC 1222]: tests: create PROFILE=1 CI job.
  | `20616 <https:////gerrit.fd.io/r/c/vpp/+/20616>`_ [veC 1223]: tests: fix VppGbpContractRule
  | `20326 <https:////gerrit.fd.io/r/c/vpp/+/20326>`_ [veC 1229]: tests: - experiment--identify dup. object creation in tests.
  | `20414 <https:////gerrit.fd.io/r/c/vpp/+/20414>`_ [VeC 1233]: build:  Update .gitignore
  | `20202 <https:////gerrit.fd.io/r/c/vpp/+/20202>`_ [veC 1236]: mpls: mpls_sw_interface_enable_disable should return error
  | `20171 <https:////gerrit.fd.io/r/c/vpp/+/20171>`_ [veC 1245]: mpls: fix coredump if disabling mpls on non-mpls int. via api
  | `20200 <https:////gerrit.fd.io/r/c/vpp/+/20200>`_ [veC 1245]: interface: return an error if sw_interface_set_unnumbered fails.
  | `18166 <https:////gerrit.fd.io/r/c/vpp/+/18166>`_ [veC 1341]: Tests: test/vpp_interface.py. Compute static properties once.
  | `18020 <https:////gerrit.fd.io/r/c/vpp/+/18020>`_ [VeC 1350]: Do Not Commit! test_Reassembly.
  | `17093 <https:////gerrit.fd.io/r/c/vpp/+/17093>`_ [veC 1379]: VTL: Fix Segment routing API tests.
  | `16991 <https:////gerrit.fd.io/r/c/vpp/+/16991>`_ [veC 1392]: VTL: Change classify_add_del_session vpp_papi_provider.py logic to support 'skip_n_vectors'.
  | `16724 <https:////gerrit.fd.io/r/c/vpp/+/16724>`_ [veC 1405]: Add bug reporting framework to tests.
  | `16660 <https:////gerrit.fd.io/r/c/vpp/+/16660>`_ [VeC 1412]: test framework.py Handle missing docstring gracefully.
  | `16616 <https:////gerrit.fd.io/r/c/vpp/+/16616>`_ [VeC 1413]: tests: Rework vpp config generation.
  | `16270 <https:////gerrit.fd.io/r/c/vpp/+/16270>`_ [veC 1446]: Fix typo.  vpp_papi/vpp_serializer.py
  | `16285 <https:////gerrit.fd.io/r/c/vpp/+/16285>`_ [veC 1446]: test/framework.py: add exception handling to Worker.
  | `16158 <https:////gerrit.fd.io/r/c/vpp/+/16158>`_ [VeC 1446]: Alternative to Fix test framework keepalive

**Pavel Kotucek** <pavel.kotucek@pantheon.tech>:

  | `28019 <https:////gerrit.fd.io/r/c/vpp/+/28019>`_ [VeC 846]: misc: (NAT) eBPF traceability
  | `17565 <https:////gerrit.fd.io/r/c/vpp/+/17565>`_ [VeC 1366]: Fix VPP-1506

**Pengjieyou** <pangkityau@gmail.com>:

  | `33528 <https:////gerrit.fd.io/r/c/vpp/+/33528>`_ [VeC 453]: acl: fix ipv6 address match of acl_plugin

**Peter Skvarka** <pskvarka@frinx.io>:

  | `30177 <https:////gerrit.fd.io/r/c/vpp/+/30177>`_ [vec 166]: flowprobe: memory leak unreleased frame
  | `29493 <https:////gerrit.fd.io/r/c/vpp/+/29493>`_ [veC 719]: flowprobe: memory leak unreleased frame

**Pierre Pfister** <ppfister@cisco.com>:

  | `14358 <https:////gerrit.fd.io/r/c/vpp/+/14358>`_ [veC 1350]: Add vat plugin path to run-vat
  | `14782 <https:////gerrit.fd.io/r/c/vpp/+/14782>`_ [veC 1525]: Fix 'show lb vips' CLI command

**Ping Yu** <ping.yu@intel.com>:

  | `26310 <https:////gerrit.fd.io/r/c/vpp/+/26310>`_ [VeC 957]: dpdk: fix an issue that hw offload
  | `24903 <https:////gerrit.fd.io/r/c/vpp/+/24903>`_ [vec 1009]: tls: handle TCP reset in TLS stack
  | `24336 <https:////gerrit.fd.io/r/c/vpp/+/24336>`_ [vec 1035]: tls: openssl handle closure alert
  | `24138 <https:////gerrit.fd.io/r/c/vpp/+/24138>`_ [veC 1054]: svm: fix a dead wait for svm message
  | `21213 <https:////gerrit.fd.io/r/c/vpp/+/21213>`_ [veC 1191]: tls: enable openssl master build
  | `16798 <https:////gerrit.fd.io/r/c/vpp/+/16798>`_ [veC 1400]: Fix build issue if using openssl 3.0.0 dev branch
  | `16640 <https:////gerrit.fd.io/r/c/vpp/+/16640>`_ [veC 1416]: fix an issue for vfio auto detection

**Piotr Kleski** <piotrx.kleski@intel.com>:

  | `30383 <https:////gerrit.fd.io/r/c/vpp/+/30383>`_ [VeC 638]: ipsec: async mode restrictions

**RADHA KRISHNA SARAGADAM** <krishna_srk2003@yahoo.com>:

  | `36711 <https:////gerrit.fd.io/r/c/vpp/+/36711>`_ [Vec 112]: ebuild: upgrade vagrant ubuntu version to 20.04

**Radu Nicolau** <radu.nicolau@intel.com>:

  | `31702 <https:////gerrit.fd.io/r/c/vpp/+/31702>`_ [vec 545]: avf: performance improvement
  | `30974 <https:////gerrit.fd.io/r/c/vpp/+/30974>`_ [vec 615]: vlib: startup multi-arch variant configuration fix for interfaces

**Rajesh Saluja** <rajsaluj@cisco.com>:

  | `31016 <https:////gerrit.fd.io/r/c/vpp/+/31016>`_ [veC 656]: estimated mtu should be derived from max_fragment_length

**Rajith Ramakrishna** <rajith@rtbrick.com>:

  | `35291 <https:////gerrit.fd.io/r/c/vpp/+/35291>`_ [vec 274]: ip6: fix packet drop of NS message for link local destination.
  | `35289 <https:////gerrit.fd.io/r/c/vpp/+/35289>`_ [VeC 276]: fib: fix the crash in worker when fib_path_list_pool expands
  | `35227 <https:////gerrit.fd.io/r/c/vpp/+/35227>`_ [VeC 280]: fib: fix fib path pool expand cases fib_path_create, fib_path_create_special are not thread safe when the fib path pool expand.

**Ryan King** <ryanking8215@gmail.com>:

  | `20078 <https:////gerrit.fd.io/r/c/vpp/+/20078>`_ [veC 1246]: fix client making cpu high after vpp restart

**Ryujiro Shibuya** <ryujiro.shibuya@owmobility.com>:

  | `27790 <https:////gerrit.fd.io/r/c/vpp/+/27790>`_ [Vec 862]: tcp: rework on rcv wnd adjustment
  | `23979 <https:////gerrit.fd.io/r/c/vpp/+/23979>`_ [veC 1061]: svm: add an option to keep margin in the fifo

**Sachin Saxena** <sachin.saxena18@gmail.com>:

  | `13189 <https:////gerrit.fd.io/r/c/vpp/+/13189>`_ [VeC 1562]: arm: Added option to include DPDK armv8_crypto library
  | `12932 <https:////gerrit.fd.io/r/c/vpp/+/12932>`_ [VeC 1568]: dpdk: Add Virtual addressing support in IOVA dmamap

**Sergey Matov** <sergey.matov@travelping.com>:

  | `30099 <https:////gerrit.fd.io/r/c/vpp/+/30099>`_ [VeC 487]: vppinfra: Refactor sparse_vec_free
  | `31433 <https:////gerrit.fd.io/r/c/vpp/+/31433>`_ [Vec 628]: vlib: Avoid counter overflow

**Shiva Shankar** <shivaashankar1204@gmail.com>:

  | `29707 <https:////gerrit.fd.io/r/c/vpp/+/29707>`_ [Vec 738]: ethernet: coverity fix #214973

**Shmuel Hazan** <shmuel.h@siklu.com>:

  | `34775 <https:////gerrit.fd.io/r/c/vpp/+/34775>`_ [VeC 323]: dpdk: don't remove unupdated hw flags

**Simon Zhang** <yuwei1.zhang@intel.com>:

  | `25754 <https:////gerrit.fd.io/r/c/vpp/+/25754>`_ [vec 981]: tls: fix the wrong usage of svm_fifo_dequeue function in Picotls engine
  | `25584 <https:////gerrit.fd.io/r/c/vpp/+/25584>`_ [vec 987]: tls: fix tls hang issue
  | `20519 <https:////gerrit.fd.io/r/c/vpp/+/20519>`_ [veC 1229]: Allocate appropriate number of vlib_buffer_t for buffer chain scenario.

**Sirshak Das** <sirshak.das@arm.com>:

  | `12955 <https:////gerrit.fd.io/r/c/vpp/+/12955>`_ [VeC 1616]: Enable PMU cycle counter for graph node cycles

**Sivaprasad Tummala** <sivaprasad.tummala@intel.com>:

  | `34897 <https:////gerrit.fd.io/r/c/vpp/+/34897>`_ [VeC 292]: snort: restrict daq instance to single thread
  | `34899 <https:////gerrit.fd.io/r/c/vpp/+/34899>`_ [VeC 292]: snort: flow steering to multiple daqs

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `36721 <https:////gerrit.fd.io/r/c/vpp/+/36721>`_ [VeC 61]: vppapigen: enable codegen for stream message types
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 71]: virtio: allocate frame per interface

**Sudhir C R** <sudhir@rtbrick.com>:

  | `35367 <https:////gerrit.fd.io/r/c/vpp/+/35367>`_ [VeC 270]: ip: fragmentation issue with ttl 1
  | `35364 <https:////gerrit.fd.io/r/c/vpp/+/35364>`_ [veC 270]: devices: fix the crash in worker when interface pool expands
  | `35355 <https:////gerrit.fd.io/r/c/vpp/+/35355>`_ [veC 271]: ping: assertion on disabling interface during a ping
  | `35353 <https:////gerrit.fd.io/r/c/vpp/+/35353>`_ [veC 271]: ping: This avoids assertion on disabling interface during a ping
  | `35352 <https:////gerrit.fd.io/r/c/vpp/+/35352>`_ [veC 271]: ping: This avoids assertion on disabling interface during a ping when ping is going on in one terminal and we disable interface from other terminal sometimes causes assertion type: fix

**Swati Kher** <swatikher@gmail.com>:

  | `20939 <https:////gerrit.fd.io/r/c/vpp/+/20939>`_ [veC 1198]: Support for python3 - testcase compatibility for python3

**Takanori Hirano** <me@hrntknr.net>:

  | `36781 <https:////gerrit.fd.io/r/c/vpp/+/36781>`_ [VeC 84]: ip6-nd: add fixed flag

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [vEC 0]: srv6-mobile: Implementing SRv6 mobile API funcs

**Tan Haiyang** <haiyangtan@tencent.com>:

  | `16643 <https:////gerrit.fd.io/r/c/vpp/+/16643>`_ [veC 1417]: gbp: fix ipv6 type checking

**Ted Chen** <znscnchen@gmail.com>:

  | `36790 <https:////gerrit.fd.io/r/c/vpp/+/36790>`_ [VeC 47]: map: lpm 128 lookup error.
  | `37143 <https:////gerrit.fd.io/r/c/vpp/+/37143>`_ [VeC 59]: classify: remove unnecessary reallocation

**Tianyu Li** <tianyu.li@arm.com>:

  | `37530 <https:////gerrit.fd.io/r/c/vpp/+/37530>`_ [vEc 18]: dpdk: fix interface name w/ the same PCI bus/slot/function
  | `36488 <https:////gerrit.fd.io/r/c/vpp/+/36488>`_ [VeC 141]: tests: fix wireguard test failure under heavy load
  | `35707 <https:////gerrit.fd.io/r/c/vpp/+/35707>`_ [VeC 239]: ip: reassembly add prefetch to improve throughput
  | `35680 <https:////gerrit.fd.io/r/c/vpp/+/35680>`_ [VeC 243]: ip: ip frag node multi arch support
  | `32420 <https:////gerrit.fd.io/r/c/vpp/+/32420>`_ [VeC 530]: memif: unroll tx loop to increase performance

**Tianyu Li** <tianyulee@gmail.com>:

  | `16641 <https:////gerrit.fd.io/r/c/vpp/+/16641>`_ [veC 1417]: Change show buffer output format to unsigned int

**Timothee Chauvin** <timchauv@cisco.com>:

  | `27678 <https:////gerrit.fd.io/r/c/vpp/+/27678>`_ [veC 868]: misc: fix usage of lcov in extras/lcov/lcov_*

**Ting Xu** <ting.xu@intel.com>:

  | `37563 <https:////gerrit.fd.io/r/c/vpp/+/37563>`_ [vEC 9]: avf: support generic flow

**Tom Seidenberg** <tseidenb@cisco.com>:

  | `24515 <https:////gerrit.fd.io/r/c/vpp/+/24515>`_ [VeC 1016]: virtio: Defensive fix for erroneous multisegment packets.

**Tony Samuels** <vegizombie@gmail.com>:

  | `17630 <https:////gerrit.fd.io/r/c/vpp/+/17630>`_ [VeC 1366]: Fix broken link in README. This is caused by the link being longer than the default line length of 80 characters.

**Vengada Govindan** <venggovi@cisco.com>:

  | `31906 <https:////gerrit.fd.io/r/c/vpp/+/31906>`_ [Vec 587]: nsh: resolve Coverity error in nsh_api.c

**Vladimir Isaev** <visaev@netgate.com>:

  | `29445 <https:////gerrit.fd.io/r/c/vpp/+/29445>`_ [Vec 565]: nat: do not translate packets from outside intfc

**Vladislav Grishenko** <themiron@mail.ru>:

  | `37315 <https:////gerrit.fd.io/r/c/vpp/+/37315>`_ [VeC 43]: buffers: fix buffer leak on enqueue to bad thread
  | `37270 <https:////gerrit.fd.io/r/c/vpp/+/37270>`_ [VeC 48]: vppinfra: fix pool free bitmap allocation
  | `35721 <https:////gerrit.fd.io/r/c/vpp/+/35721>`_ [VeC 54]: vlib: stop worker threads on main loop exit
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 54]: papi: fix socket api max message id calculation
  | `35914 <https:////gerrit.fd.io/r/c/vpp/+/35914>`_ [VeC 182]: linux-cp: refactor sw_if_index bool vector to bitmap
  | `35796 <https:////gerrit.fd.io/r/c/vpp/+/35796>`_ [VeC 222]: vlib: avoid non-mp-safe cli process node updates

**Vratko Polak** <vrpolak@cisco.com>:

  | `37083 <https:////gerrit.fd.io/r/c/vpp/+/37083>`_ [Vec 62]: avf: tolerate socket events in avf_process_request
  | `27972 <https:////gerrit.fd.io/r/c/vpp/+/27972>`_ [VeC 139]: sr: Fix deletion if target SR list is not found
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 139]: api: fix vl_socket_write_ready

**Wai Chan** <weichen@astri.org>:

  | `19429 <https:////gerrit.fd.io/r/c/vpp/+/19429>`_ [veC 1287]: api: fix crash error that receive get_node_graph cmd from vat
  | `18542 <https:////gerrit.fd.io/r/c/vpp/+/18542>`_ [VeC 1328]: [VPPInfra]: Fix the issue that worker thread will access invalid memory when update thread do vector resize.

**Weiguo Li** <liwg06@foxmail.com>:

  | `34779 <https:////gerrit.fd.io/r/c/vpp/+/34779>`_ [veC 329]: misc: fix incorrect return value checking

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37427 <https:////gerrit.fd.io/r/c/vpp/+/37427>`_ [vEC 30]: crypto: fix crypto dequeue handlers should be setted by VNET_CRYPTO_ASYNC_OP_XX
  | `37376 <https:////gerrit.fd.io/r/c/vpp/+/37376>`_ [VeC 37]: vlib: unix cli - fix input's buffer may be freed when using
  | `37375 <https:////gerrit.fd.io/r/c/vpp/+/37375>`_ [VeC 38]: ipsec: fix ipsec linked key not freed when sa deleted
  | `34817 <https:////gerrit.fd.io/r/c/vpp/+/34817>`_ [VeC 38]: ipsec: improve ipsec policy adding performance
  | `36808 <https:////gerrit.fd.io/r/c/vpp/+/36808>`_ [Vec 78]: arp: add support for Microsoft NLB unicast
  | `36880 <https:////gerrit.fd.io/r/c/vpp/+/36880>`_ [VeC 95]: ip: only set rx_sw_if_index when connection found to avoid following crash like tcp punt
  | `36812 <https:////gerrit.fd.io/r/c/vpp/+/36812>`_ [VeC 96]: cjson: json realloced output truncated if actual lenght more then 256
  | `35563 <https:////gerrit.fd.io/r/c/vpp/+/35563>`_ [Vec 252]: ipsec: no need to check for sa integ_op_id when building async frame
  | `35361 <https:////gerrit.fd.io/r/c/vpp/+/35361>`_ [VeC 270]: vppinfra: fix asan issue for hash_memory64
  | `34866 <https:////gerrit.fd.io/r/c/vpp/+/34866>`_ [Vec 307]: ip6-nd: fix ethernet head building error for NA msg
  | `33578 <https:////gerrit.fd.io/r/c/vpp/+/33578>`_ [veC 340]: ipsec: skip fragmented packet for ipsec4-input-feature node
  | `32899 <https:////gerrit.fd.io/r/c/vpp/+/32899>`_ [VeC 508]: dispatch-trace: fix "pcap dispatch trace on" command has no effect

**Xie Long** <barryxie@tencent.com>:

  | `30268 <https:////gerrit.fd.io/r/c/vpp/+/30268>`_ [veC 75]: ip: fixup crash when reassemble a lots of fragments.
  | `30270 <https:////gerrit.fd.io/r/c/vpp/+/30270>`_ [veC 708]: fib: fixup some fib nodes in node-graph are not been notified by fib_walk_sync/fib_walk_async

**Xu Wen** <wenx05124561@163.com>:

  | `14095 <https:////gerrit.fd.io/r/c/vpp/+/14095>`_ [VeC 1554]: nat64: nat64_out2in not translate when dst_address is on the interface
  | `14128 <https:////gerrit.fd.io/r/c/vpp/+/14128>`_ [veC 1558]: nat64: nat64_out2in not translate when dst_address is on the interface
  | `13599 <https:////gerrit.fd.io/r/c/vpp/+/13599>`_ [veC 1576]: nat64: make nat64 node runs_after acl nodes

**YI-SUNG Chiu** <steven30801@gmail.com>:

  | `34470 <https:////gerrit.fd.io/r/c/vpp/+/34470>`_ [VeC 330]: policer: enable handoff action in policer formatting

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37274 <https:////gerrit.fd.io/r/c/vpp/+/37274>`_ [VEc 25]: af_xdp: fix xdp socket create fail

**Yohan Pipereau** <ypiperea@cisco.com>:

  | `20678 <https:////gerrit.fd.io/r/c/vpp/+/20678>`_ [veC 1212]: vom: Separate RPM package for VOM

**Yong Liu** <yong.liu@intel.com>:

  | `31097 <https:////gerrit.fd.io/r/c/vpp/+/31097>`_ [vec 617]: virtio: enhance packed ring status check

**Yucai Gu** <yucgu@cisco.com>:

  | `30321 <https:////gerrit.fd.io/r/c/vpp/+/30321>`_ [veC 707]: VPP DPDK load balance feature This PR is to add a DPDK device load balance feature in the VPP base code. The idea of adding this feature is to resolve a worker CPU balance issue when the traffic is high.

**Zhiyong Yang** <zhiyong.yang@intel.com>:

  | `26226 <https:////gerrit.fd.io/r/c/vpp/+/26226>`_ [Vec 546]: vlib: add avx512 support for two vlib_get_buffer related functions
  | `27213 <https:////gerrit.fd.io/r/c/vpp/+/27213>`_ [vec 735]: l2: performance enhancement in l2output
  | `26415 <https:////gerrit.fd.io/r/c/vpp/+/26415>`_ [VeC 951]: dpdk: prefetching second cacheline only when tx_offload enabled
  | `20838 <https:////gerrit.fd.io/r/c/vpp/+/20838>`_ [veC 1202]: misc: avoid probable twice assignments in cop
  | `19206 <https:////gerrit.fd.io/r/c/vpp/+/19206>`_ [veC 1295]: ipsec_output_inline: leverage vlib_get_buffers
  | `13853 <https:////gerrit.fd.io/r/c/vpp/+/13853>`_ [veC 1517]: ip4_rewrite: improve prefetching of packet header data on IA
  | `14389 <https:////gerrit.fd.io/r/c/vpp/+/14389>`_ [veC 1539]: dpdk_input: remove duplicated assignment
  | `14134 <https:////gerrit.fd.io/r/c/vpp/+/14134>`_ [veC 1549]: rewrite IP checksum on IA
  | `14306 <https:////gerrit.fd.io/r/c/vpp/+/14306>`_ [veC 1551]: vxlan-gpe: quad-loop optimization
  | `13769 <https:////gerrit.fd.io/r/c/vpp/+/13769>`_ [veC 1558]: rewrite _ip_incremental_checksum
  | `13803 <https:////gerrit.fd.io/r/c/vpp/+/13803>`_ [veC 1567]: using ip_csum in ip4_header_checksum
  | `13140 <https:////gerrit.fd.io/r/c/vpp/+/13140>`_ [veC 1597]: dpdk: force i40e to use avx2 optimized datapath when machine supports avx2
  | `12776 <https:////gerrit.fd.io/r/c/vpp/+/12776>`_ [veC 1629]: dpdk: use initial-exec model for thread local variable on IA
  | `12733 <https:////gerrit.fd.io/r/c/vpp/+/12733>`_ [VeC 1634]: dpdk: makefile optimization

**alex ni** <alex.ni@mavenir.com>:

  | `18731 <https:////gerrit.fd.io/r/c/vpp/+/18731>`_ [veC 1317]: delete the unnecessary code in ip4_frag_do_fragment: as max has been computed and &~0x7, it is unnecessary to compute it again

**arikachen** <eaglesora@gmail.com>:

  | `34561 <https:////gerrit.fd.io/r/c/vpp/+/34561>`_ [Vec 330]: af_xdp: fix free rxq buffers while delete if

**bindiya k** <bindiyakurle@gmail.com>:

  | `10394 <https:////gerrit.fd.io/r/c/vpp/+/10394>`_ [veC 1744]: arp resolution does not when classifier table index attached to interface. Fixed this by always checking entry which has source as INTERFACE.

**dengfeng liu** <liudf0716@gmail.com>:

  | `30922 <https:////gerrit.fd.io/r/c/vpp/+/30922>`_ [veC 659]: ip: replace type_by_name with type_and_code_by_name param Type: fix
  | `29376 <https:////gerrit.fd.io/r/c/vpp/+/29376>`_ [vec 764]: ipsec: sort spd polices after delete a spd policy

**duojiao mu** <mu.duojiao@zte.com.cn>:

  | `19216 <https:////gerrit.fd.io/r/c/vpp/+/19216>`_ [veC 1296]: VPP-1664:Get wrong extern head by ip6_ext_header_find_t.
  | `16370 <https:////gerrit.fd.io/r/c/vpp/+/16370>`_ [veC 1366]: VPP-1516:when ip fib dump,connect route will display error.

**eyal bari** <royalbee@gmail.com>:

  | `15596 <https:////gerrit.fd.io/r/c/vpp/+/15596>`_ [veC 1217]: l2_flood:bvi:use a full buffer copy

**f00182600** <fangtong2007@163.com>:

  | `36453 <https:////gerrit.fd.io/r/c/vpp/+/36453>`_ [veC 134]: interface: fix the issue of show hardware-interface with invalid if-idx can caused vpp crash.
  | `35963 <https:////gerrit.fd.io/r/c/vpp/+/35963>`_ [veC 152]: dns: fix the isssue of memory leak.
  | `35862 <https:////gerrit.fd.io/r/c/vpp/+/35862>`_ [VeC 152]: nat: Delete the operation of repeatedly releasing Nat44 ei port resources

**guanghua zhang** <zhangguanghua2011@163.com>:

  | `22142 <https:////gerrit.fd.io/r/c/vpp/+/22142>`_ [veC 1073]: tcp: tcp_check_tx_offload get sw_if_index in a another way.
  | `21628 <https:////gerrit.fd.io/r/c/vpp/+/21628>`_ [veC 1173]: vlib: fix pcap dispatch trace command issue.

**han wu** <wuhan9084@163.com>:

  | `34684 <https:////gerrit.fd.io/r/c/vpp/+/34684>`_ [Vec 299]: ping: fix the wrong usage of vec_del1 which may cause unpredictable situation vrrp: fix the wrong usage of vec_del1 which may cause unpredictable situation wireguard: fix the wrong usage of vec_del1 which may cause unpredictable situation

**hu jihui** <hu.jihui@zte.com.cn>:

  | `30638 <https:////gerrit.fd.io/r/c/vpp/+/30638>`_ [veC 678]: VPP-1960: vpp crash when del export fib entry
  | `19731 <https:////gerrit.fd.io/r/c/vpp/+/19731>`_ [veC 1274]: VPP-1682 the 'curr_key' and 'next_key' members of struct 'bfd_session_t' could become wild pointer.

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `36901 <https:////gerrit.fd.io/r/c/vpp/+/36901>`_ [VeC 61]: interface: fix 4 or more interfaces equality comparison bug with xor operation using (a^a)^(b^b)

**jinshaohui jinshaohui** <jinshaohui789@163.com>:

  | `25595 <https:////gerrit.fd.io/r/c/vpp/+/25595>`_ [VeC 987]: vppinfra: fix memory issue in mhash
  | `25590 <https:////gerrit.fd.io/r/c/vpp/+/25590>`_ [VeC 987]: vppinfra: fix memory issue in mhash

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [VEc 0]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [VEc 3]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop
  | `34963 <https:////gerrit.fd.io/r/c/vpp/+/34963>`_ [VeC 300]: interface:Format output with one more % C, terminal print gibberish
  | `34919 <https:////gerrit.fd.io/r/c/vpp/+/34919>`_ [VeC 302]: dpdk: number of tx queues can not larger than the physical max tx queues
  | `32497 <https:////gerrit.fd.io/r/c/vpp/+/32497>`_ [veC 534]: policer: cli policer bind name xxx <workers> failed              policer bind unbind name xxx  failed
  | `32496 <https:////gerrit.fd.io/r/c/vpp/+/32496>`_ [veC 534]: policer: cli policer bind name xxx <workers> failed          policer bind unbind name xxx  failed
  | `32495 <https:////gerrit.fd.io/r/c/vpp/+/32495>`_ [veC 534]: policer: cli policer bind name xxx <workers> failed            policer bind unbind name xxx  failed
  | `30930 <https:////gerrit.fd.io/r/c/vpp/+/30930>`_ [VeC 658]: vppinfra: fix memory issue in mhash

**juan dong** <dong.juan1@zte.com.cn>:

  | `30654 <https:////gerrit.fd.io/r/c/vpp/+/30654>`_ [VeC 672]: vlib: nm_clone node_by_name re-assign to avoid coredump
  | `19746 <https:////gerrit.fd.io/r/c/vpp/+/19746>`_ [VeC 1237]: nat: use different random seed
  | `19767 <https:////gerrit.fd.io/r/c/vpp/+/19767>`_ [VeC 1237]: nat: goto get_local may trigger exception when num_workers > 1

**kai zhang** <zhangkaiheb@126.com>:

  | `34806 <https:////gerrit.fd.io/r/c/vpp/+/34806>`_ [veC 321]: nat44-ed: fix port endian of load-balancing static mapping

**khemendra kumar** <khemendra.kumar13@gmail.com>:

  | `12462 <https:////gerrit.fd.io/r/c/vpp/+/12462>`_ [VeC 1043]: VPP-1126 use restrict keyword so that compiler can          generate optimized code on aarch64

**liu anhua** <liu.anhua@ericsson.com>:

  | `13134 <https:////gerrit.fd.io/r/c/vpp/+/13134>`_ [vec 291]: gtpu: Add gtpu path management and change single teid to bidirectional teid.
  | `13043 <https:////gerrit.fd.io/r/c/vpp/+/13043>`_ [veC 1517]: Add to configure the tx queue len of TUN device.
  | `13040 <https:////gerrit.fd.io/r/c/vpp/+/13040>`_ [VeC 1597]: The parameter must be point of vec header while checking the heap object in funtion vlib_get_node_by_name.

**lollita liu** <lollita.liu@ericsson.com>:

  | `18310 <https:////gerrit.fd.io/r/c/vpp/+/18310>`_ [veC 1341]: cli: fix the deadloop bug of inputting wrong node name in "show node" CLI

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [vEC 8]: policer: add policer classify to output path
  | `34812 <https:////gerrit.fd.io/r/c/vpp/+/34812>`_ [VEc 20]: interface: more cleaning after set flags is failed in vnet_create_sw_interface

**maqi ke** <maqi.z.ke@ericsson.com>:

  | `18543 <https:////gerrit.fd.io/r/c/vpp/+/18543>`_ [VeC 1314]: cli:fix show node

**marek zavodsky** <mazavods@gmail.com>:

  | `31642 <https:////gerrit.fd.io/r/c/vpp/+/31642>`_ [veC 610]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31628 <https:////gerrit.fd.io/r/c/vpp/+/31628>`_ [veC 613]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31615 <https:////gerrit.fd.io/r/c/vpp/+/31615>`_ [veC 614]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31608 <https:////gerrit.fd.io/r/c/vpp/+/31608>`_ [veC 615]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31593 <https:////gerrit.fd.io/r/c/vpp/+/31593>`_ [veC 616]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31438 <https:////gerrit.fd.io/r/c/vpp/+/31438>`_ [veC 628]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31430 <https:////gerrit.fd.io/r/c/vpp/+/31430>`_ [veC 629]: dns: Failing to get DNS AAAA records (and A records in one case)
  | `31426 <https:////gerrit.fd.io/r/c/vpp/+/31426>`_ [vec 629]: dns: Failing to get DNS AAAA records (and A records in one case)

**pippo zhang** <pippo.zhang@ericsson.com>:

  | `16762 <https:////gerrit.fd.io/r/c/vpp/+/16762>`_ [veC 1398]: add command: show statistics heap

**s5ci-nomad pilot** <ayourtch@icloud.com>:

  | `31429 <https:////gerrit.fd.io/r/c/vpp/+/31429>`_ [veC 314]: misc: refresh the pinning of test dependencies by running make test-refresh-deps

**shaochun chen** <cscnull@gmail.com>:

  | `24150 <https:////gerrit.fd.io/r/c/vpp/+/24150>`_ [veC 1048]: vmxnet3: translate etherType from network-order to host-order

**steven luong** <sluong@cisco.com>:

  | `37511 <https:////gerrit.fd.io/r/c/vpp/+/37511>`_ [vEC 1]: vxlan: convert vxlan to a plugin
  | `37105 <https:////gerrit.fd.io/r/c/vpp/+/37105>`_ [VeC 34]: vppinfra: add time error counters to stats segment
  | `30866 <https:////gerrit.fd.io/r/c/vpp/+/30866>`_ [Vec 99]: bonding: Add failover-mac active support
  | `36250 <https:////gerrit.fd.io/r/c/vpp/+/36250>`_ [VeC 172]: classify: sanity check table index for update
  | `36089 <https:////gerrit.fd.io/r/c/vpp/+/36089>`_ [VeC 193]: ip: Display show ip table without truncation
  | `35234 <https:////gerrit.fd.io/r/c/vpp/+/35234>`_ [VeC 274]: fib: ip table del checks
  | `35212 <https:////gerrit.fd.io/r/c/vpp/+/35212>`_ [VeC 285]: fib: crash at vnet_rewrite_set_data_internal
  | `35157 <https:////gerrit.fd.io/r/c/vpp/+/35157>`_ [VeC 286]: fib: remove all routes when vrf table is deleted
  | `33169 <https:////gerrit.fd.io/r/c/vpp/+/33169>`_ [veC 487]: bonding: send GARP upon first member becomes active in bond
  | `32536 <https:////gerrit.fd.io/r/c/vpp/+/32536>`_ [veC 531]: bonding: create bond process on demand
  | `32486 <https:////gerrit.fd.io/r/c/vpp/+/32486>`_ [veC 536]: vhost: launch vhost process on demand
  | `32083 <https:////gerrit.fd.io/r/c/vpp/+/32083>`_ [veC 540]: interface: error checking and returning for set interface rx-mode
  | `31452 <https:////gerrit.fd.io/r/c/vpp/+/31452>`_ [veC 628]: nat: remove ASSERT in nat_6t_flow_ip4_translate
  | `29396 <https:////gerrit.fd.io/r/c/vpp/+/29396>`_ [VeC 764]: bonding: automatically set interface to promiscuos for LACP bonding
  | `28105 <https:////gerrit.fd.io/r/c/vpp/+/28105>`_ [VeC 839]: dpdk: allocate rx_queues and tx_queues early
  | `20189 <https:////gerrit.fd.io/r/c/vpp/+/20189>`_ [VeC 1245]: acl interface vlib: memory leaks
  | `17947 <https:////gerrit.fd.io/r/c/vpp/+/17947>`_ [VeC 1350]: c11 safeC replacement for strncpy and strcpy

**sunitha naram reddy** <snaramre@cisco.com>:

  | `23417 <https:////gerrit.fd.io/r/c/vpp/+/23417>`_ [Vec 710]: tests: scapy 2.4.3 changes
  | `23131 <https:////gerrit.fd.io/r/c/vpp/+/23131>`_ [vec 1111]: tests: make test changes for scapy 2.4.3
  | `21621 <https:////gerrit.fd.io/r/c/vpp/+/21621>`_ [veC 1174]: python3 string to byte conversions for udp tests

**vijayakumar rajamanickam** <vijayakumar.rajamanickam@nokia.com>:

  | `19829 <https:////gerrit.fd.io/r/c/vpp/+/19829>`_ [vec 939]: reassembly: Ipv4 reassembly timeout  error counter

**wanghanlin wanghanlin** <wanghanlin@corp.netease.com>:

  | `34318 <https:////gerrit.fd.io/r/c/vpp/+/34318>`_ [Vec 376]: vcl: fix inaccuracy wait rpc response timeout
  | `33012 <https:////gerrit.fd.io/r/c/vpp/+/33012>`_ [VeC 497]: dpdk: add DEV_TX_OFFLOAD_IPV4_CKSUM support
  | `32963 <https:////gerrit.fd.io/r/c/vpp/+/32963>`_ [VeC 497]: dpdk: support TX CKSUM offload for mlx5
  | `32962 <https:////gerrit.fd.io/r/c/vpp/+/32962>`_ [veC 497]: vppinfra: add timestamp for positioning problem
  | `28703 <https:////gerrit.fd.io/r/c/vpp/+/28703>`_ [Vec 650]: vcl: support kernel stack based on localhost IPV4 address

**xujunjie-cover** <xujunjielxx@163.com>:

  | `36494 <https:////gerrit.fd.io/r/c/vpp/+/36494>`_ [VeC 141]: lb: fix make l4 lb function work
  | `34703 <https:////gerrit.fd.io/r/c/vpp/+/34703>`_ [VeC 341]: dns: cache: fix show dns cache Unlock missing after show dns cache with name.

**yacan liu** <liuyacan@corp.netease.com>:

  | `32949 <https:////gerrit.fd.io/r/c/vpp/+/32949>`_ [vec 501]: vcl: support packetdrill test framework

**yang mo** <srsdellsound@yahoo.com>:

  | `32754 <https:////gerrit.fd.io/r/c/vpp/+/32754>`_ [VeC 472]: sr: make srv6 ad flow support multi thread

**ye donggang** <yedg@wangsu.com>:

  | `29814 <https:////gerrit.fd.io/r/c/vpp/+/29814>`_ [VeC 707]: acl:  fix acl endless loop without session
  | `28603 <https:////gerrit.fd.io/r/c/vpp/+/28603>`_ [veC 716]: ipsec: sort polices when del
  | `30082 <https:////gerrit.fd.io/r/c/vpp/+/30082>`_ [veC 724]: interface:  fix show interface addr error
  | `28606 <https:////gerrit.fd.io/r/c/vpp/+/28606>`_ [veC 808]: ipsec: use icv size to hmac in aead algo

**力茂 张** <zhanglimao0017@gmail.com>:

  | `18455 <https:////gerrit.fd.io/r/c/vpp/+/18455>`_ [veC 1334]: configure classify table occur Segmentation fault

**郑 德伦** <xszhengdelun@gmail.com>:

  | `27193 <https:////gerrit.fd.io/r/c/vpp/+/27193>`_ [VeC 902]: interface: fix pcap trace filter error

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
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
authors          502
maintainers      38
committers       0
================ ===

