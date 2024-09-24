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
generated on Tuesday 2024-09-24, 02:30:12
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

  | `41587 <https:////gerrit.fd.io/r/c/vpp/+/41587>`_ [VECR 0]: octeon: enable ethernet pause frame support
  | `41532 <https:////gerrit.fd.io/r/c/vpp/+/41532>`_ [VECR 18]: octeon: enable h/w vlan tagging support

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

api: **Dave Barach** <vpp@barachs.net>
  | `41524 <https:////gerrit.fd.io/r/c/vpp/+/41524>`_ [VECr 14]: bfd: add support for multihop

avf: **Damjan Marion** <damarion@cisco.com>
  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VECr 13]: avf: mark api as deprecated
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VECr 13]: avf: interprocess reply via pointer

bfd: **Klement Sekera** <klement.sekera@gmail.com>
  | `41524 <https:////gerrit.fd.io/r/c/vpp/+/41524>`_ [VECr 14]: bfd: add support for multihop

build: **Damjan Marion** <damarion@cisco.com>
  | `41354 <https:////gerrit.fd.io/r/c/vpp/+/41354>`_ [VECr 14]: dpdk: Enable dpdk build on FreeBSD

dev: **Damjan Marion** <damarion@cisco.com>
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VECr 13]: dev: declare api as production
  | `41556 <https:////gerrit.fd.io/r/c/vpp/+/41556>`_ [VECr 13]: dev: interprocess reply via pointer

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 16]: dhcp: fix buffer length after adding new option

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41378 <https:////gerrit.fd.io/r/c/vpp/+/41378>`_ [VECr 18]: vat2: docs
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 28]: docs: Restore and update nat section of progressive tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `41547 <https:////gerrit.fd.io/r/c/vpp/+/41547>`_ [VECr 7]: dpdk: add new device ID for Cisco VIC VF

memif: **Damjan Marion** <damarion@cisco.com>
  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [VECr 17]: memif: add cli to display "no tx slot" stats

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41504 <https:////gerrit.fd.io/r/c/vpp/+/41504>`_ [VECr 0]: build: add missing fib_walk.h to VNET_HEADERS
  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VECr 25]: build: use VPP_BUILD_TOPDIR from environment if set

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `41595 <https:////gerrit.fd.io/r/c/vpp/+/41595>`_ [VECr 0]: octeon: fix SDP device link information
  | `41589 <https:////gerrit.fd.io/r/c/vpp/+/41589>`_ [VECr 3]: octeon: fix error handling for packet with error

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 30]: session: make local port allocator fib aware

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VECr 18]: sr: fix sr_policy fib table

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 30]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41563 <https:////gerrit.fd.io/r/c/vpp/+/41563>`_ [VECr 6]: misc: Test code to debug the CI. DO NOT MERGE!
  | `41524 <https:////gerrit.fd.io/r/c/vpp/+/41524>`_ [VECr 14]: bfd: add support for multihop
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 16]: dhcp: fix buffer length after adding new option
  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VECr 21]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41457 <https:////gerrit.fd.io/r/c/vpp/+/41457>`_ [VECr 25]: tests: remove use of python 2.7 compatibility module 'six'

tracenode: **Maxime Peim** <mpeim@cisco.com>
  | `41544 <https:////gerrit.fd.io/r/c/vpp/+/41544>`_ [VECr 14]: tracenode: fix pcap capture if packet is also traced

udp: **Florin Coras** <fcoras@cisco.com>
  | `41524 <https:////gerrit.fd.io/r/c/vpp/+/41524>`_ [VECr 14]: bfd: add support for multihop
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 30]: session: make local port allocator fib aware

vapi: **Ole Troan** <ot@cisco.com>
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VECr 7]: vapi: don't store dict in length field
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VECr 25]: vapi: remove directory name from include guards

vat2: **Ole Troan** <ot@cisco.com>
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VECr 26]: vat2: fix -p in vat2 help text

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 4]: misc: patch to test CI infra changes

vppapigen: **Ole Troan** <otroan@employees.org>
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VECr 19]: vppapigen: fix enum format function

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41564 <https:////gerrit.fd.io/r/c/vpp/+/41564>`_ [VECr 12]: vppinfra: exclude clib_dt_node_add_child on FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `41431 <https:////gerrit.fd.io/r/c/vpp/+/41431>`_ [VEc 3]: hs-test: added nginx multi-thread tests
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 49]: ip: added CLI command to set ip6 reassembly params

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 89]: bonding: make link state depend on active members

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `41567 <https:////gerrit.fd.io/r/c/vpp/+/41567>`_ [vEC 0]: snort: API functions for plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [vEC 0]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 52]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VeC 55]: build: add SHA256 checksums for external downloaded dependencies
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [veC 60]: acl: use ip4_preflen_to_mask instead of artisanal function

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 42]: docs: vpp_papi example script

**Benoît Ganne** <bganne@cisco.com>:

  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 68]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 96]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 100]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 103]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 105]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 105]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 149]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `41481 <https:////gerrit.fd.io/r/c/vpp/+/41481>`_ [VEc 21]: build: fix gcov failure on ubuntu 24.04

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 133]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 154]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 165]: fib: fix mpls tunnel restacking

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 32]: qos: fix qos record cli

**Florin Coras** <florin.coras@gmail.com>:

  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VeC 73]: api: support api clients with real-time scheduling

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VeC 32]: vlib: improve core pinning
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 105]: vlib: require main core with 'skip-cores' attribute
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 144]: docs: update core-pinning configuration

**Ivan Ivanets** <iivanets@cisco.com>:

  | `41497 <https:////gerrit.fd.io/r/c/vpp/+/41497>`_ [vEC 25]: misc: patch to check behavior of test for BFD API when bfd_udp_mod_session function doesn't work correctly

**Jay Wang** <jay.wang2@arm.com>:

  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 61]: vlib: fix seed parse error
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 73]: vppinfra: add ARM neoverse-v2 support

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [veC 91]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VeC 91]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VeC 91]: ip: add ip6 shallow reassembly output feature

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 152]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vEc 12]: api-trace: enable both rx and tx direction
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 19]: api: Refresh VPP API language with path background
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VEc 28]: vxlan: move vxlan-gpe to a plugin
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 28]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 144]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 154]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 95]: vapi: only wait if queue is empty

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 124]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 132]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [VEc 0]: vlib: add vfio-token parsing support
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [VEc 4]: dev: add support for vf device with vf_token
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 105]: octeon: fix oct_free() and free allocated memory

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 174]: fib: Fix the make-before break load-balance construction

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [vEC 0]: octeon: add crypto framework

**Ole Troan** <otroan@employees.org>:

  | `41542 <https:////gerrit.fd.io/r/c/vpp/+/41542>`_ [VEc 7]: vppapigen: fix f-string in crcchecker
  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 40]: ip6: don't forward packets with invalid source address
  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VeC 54]: dpdk: xstats as symlinks

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 174]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 103]: ipsec: add SA validity check fetching IPsec SA
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 132]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 139]: build: add config option for LD_PRELOAD

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [vEC 21]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [vEC 21]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [vEC 21]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [vEC 21]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [vEC 21]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [vEC 21]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [vEC 21]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [vEC 21]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [vEC 21]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [vEC 21]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [vEC 21]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [vEC 21]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41546 <https:////gerrit.fd.io/r/c/vpp/+/41546>`_ [vEc 12]: ipsec: cleanup tun protect on interface removal
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 42]: vapi: remove plugin dependency from tests

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 116]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 116]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Tom Jones** <thj@freebsd.org>:

  | `41355 <https:////gerrit.fd.io/r/c/vpp/+/41355>`_ [VeC 53]: build: Add FreeBSD install-dep support

**Varun Rapelly** <vrapelly@marvell.com>:

  | `41591 <https:////gerrit.fd.io/r/c/vpp/+/41591>`_ [VEc 0]: tls: add async processing support

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 28]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 157]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 93]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 93]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 94]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 123]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 167]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 172]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 172]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 176]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 176]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 176]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 176]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 176]: mpls: fix crashes on mpls tunnel create/delete

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [VEc 0]: http: fix timer pool assert crash due to timer freed when timeout in main thread
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 167]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 132]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 161]: ip: discard old trace flag after copy

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
authors          89
maintainers      27
committers       2
abandoned        0
================ ===

