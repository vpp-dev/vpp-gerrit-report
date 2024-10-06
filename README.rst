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
generated on Sunday 2024-10-06, 02:35:04
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

avf: **Damjan Marion** <damarion@cisco.com>
  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VECr 5]: avf: mark api as deprecated
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VECr 25]: avf: interprocess reply via pointer

build: **Damjan Marion** <damarion@cisco.com>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 5]: vppinfra: add ARM neoverse-v2 support
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 8]: vppinfra: add ARM Neoverse-V1 support

dev: **Damjan Marion** <damarion@cisco.com>
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VECr 11]: dev: declare api as production

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 28]: dhcp: fix buffer length after adding new option

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41665 <https:////gerrit.fd.io/r/c/vpp/+/41665>`_ [VECr 4]: docs: fix statseg title in config reference
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 10]: vlib: fix seed parse error
  | `41378 <https:////gerrit.fd.io/r/c/vpp/+/41378>`_ [VECr 30]: vat2: docs

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VECr 1]: dpdk: xstats as symlinks
  | `41607 <https:////gerrit.fd.io/r/c/vpp/+/41607>`_ [VECr 8]: dpdk: validate number of tx descriptors

fib: **Neale Ranns** <neale@graphiant.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 5]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 5]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 5]: fib: ensure mpls dpo index is valid for its next node

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41434 <https:////gerrit.fd.io/r/c/vpp/+/41434>`_ [VECr 1]: hs-test: added dry run mode

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41679 <https:////gerrit.fd.io/r/c/vpp/+/41679>`_ [VECr 1]: hsa: add appns support to http cli server

http: **Florin Coras** <fcoras@cisco.com>
  | `41677 <https:////gerrit.fd.io/r/c/vpp/+/41677>`_ [VECr 1]: http: timer pool assert crash fix

interface: **Dave Barach** <vpp@barachs.net>
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 5]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 5]: stats: add sw interface tags to statseg

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 4]: nat: add nat44-ed session filtering by fib table

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VECr 1]: linux-cp: do ip6-ll cleanup on interface removal

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 5]: mpls: fix crashes on mpls tunnel create/delete
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VECr 5]: mpls: clang-format mpls-tunnel for upcoming changes

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 4]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VECr 5]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VECr 5]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VECr 5]: nat: fix nat44-ed per-vrf session limit and tests
  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VECr 5]: nat: make nat44-ed cli summary less verbose
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VECr 5]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VECr 5]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 5]: nat: fix nat44-ed address removal from fib

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 5]: stats: add sw interface tags to statseg

pg: **Dave Barach** <vpp@barachs.net>
  | `41638 <https:////gerrit.fd.io/r/c/vpp/+/41638>`_ [VECr 1]: pg: add support to delete pg interface
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 5]: stats: add interface link speed to statseg

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VECr 30]: sr: fix sr_policy fib table

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41638 <https:////gerrit.fd.io/r/c/vpp/+/41638>`_ [VECr 1]: pg: add support to delete pg interface
  | `41563 <https:////gerrit.fd.io/r/c/vpp/+/41563>`_ [VECr 3]: misc: Test code to debug the CI. DO NOT MERGE!
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VECr 4]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VECr 5]: nat: add nat44-ed ipfix dst address and port logging
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VECr 5]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 5]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 5]: nat: fix nat44-ed address removal from fib
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 5]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 5]: stats: add sw interface tags to statseg
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 28]: dhcp: fix buffer length after adding new option

tracenode: **Maxime Peim** <mpeim@cisco.com>
  | `41544 <https:////gerrit.fd.io/r/c/vpp/+/41544>`_ [VECr 26]: tracenode: fix pcap capture if packet is also traced

vapi: **Ole Troan** <ot@cisco.com>
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VECr 19]: vapi: don't store dict in length field

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 4]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 5]: stats: add interface link speed to statseg
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 10]: vlib: fix seed parse error

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 5]: vppinfra: add ARM neoverse-v2 support
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VECr 8]: vppinfra: add ARM Neoverse-V1 support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Abdel** <abdbaig@cisco.com>:

  | `41524 <https:////gerrit.fd.io/r/c/vpp/+/41524>`_ [VEc 1]: bfd: add support for multihop

**Adrian Villin** <avillin@cisco.com>:

  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 61]: ip: added CLI command to set ip6 reassembly params

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 101]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [vEC 12]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 64]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VeC 67]: build: add SHA256 checksums for external downloaded dependencies
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [veC 72]: acl: use ip4_preflen_to_mask instead of artisanal function

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 38]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 40]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 54]: docs: vpp_papi example script

**Benoît Ganne** <bganne@cisco.com>:

  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 80]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [vEC 5]: memif: add support for per queue counters
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 108]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 112]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 115]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 117]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 117]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 161]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `41481 <https:////gerrit.fd.io/r/c/vpp/+/41481>`_ [Vec 33]: build: fix gcov failure on ubuntu 24.04
  | `41457 <https:////gerrit.fd.io/r/c/vpp/+/41457>`_ [VeC 37]: tests: remove use of python 2.7 compatibility module 'six'

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 145]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 31]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 166]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 177]: fib: fix mpls tunnel restacking

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 44]: qos: fix qos record cli

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 42]: session: make local port allocator fib aware
  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VeC 85]: api: support api clients with real-time scheduling

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VeC 44]: vlib: improve core pinning
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 117]: vlib: require main core with 'skip-cores' attribute
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 156]: docs: update core-pinning configuration

**Ivan Ivanets** <iivanets@cisco.com>:

  | `41497 <https:////gerrit.fd.io/r/c/vpp/+/41497>`_ [veC 37]: misc: patch to check behavior of test for BFD API when bfd_udp_mod_session function doesn't work correctly

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [veC 103]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VeC 103]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VeC 103]: ip: add ip6 shallow reassembly output feature

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 164]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vEc 24]: api-trace: enable both rx and tx direction
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 31]: api: Refresh VPP API language with path background
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [Vec 40]: vxlan: move vxlan-gpe to a plugin
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 40]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 156]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 166]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 107]: vapi: only wait if queue is empty

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 136]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 144]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [VEc 10]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [VEc 12]: vlib: add vfio-token parsing support
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 117]: octeon: fix oct_free() and free allocated memory

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VEc 1]: octeon: add crypto framework

**Ole Troan** <otroan@employees.org>:

  | `41542 <https:////gerrit.fd.io/r/c/vpp/+/41542>`_ [VEc 19]: vppapigen: fix f-string in crcchecker
  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 52]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 115]: ipsec: add SA validity check fetching IPsec SA
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 144]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 151]: build: add config option for LD_PRELOAD

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 33]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 33]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 33]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 33]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 33]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 33]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 33]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 33]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 33]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 33]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 33]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 33]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 33]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 54]: vapi: remove plugin dependency from tests

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 128]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 128]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Tom Jones** <thj@freebsd.org>:

  | `41355 <https:////gerrit.fd.io/r/c/vpp/+/41355>`_ [VeC 65]: build: Add FreeBSD install-dep support

**Varun Rapelly** <vrapelly@marvell.com>:

  | `41591 <https:////gerrit.fd.io/r/c/vpp/+/41591>`_ [vEc 1]: tls: add async processing support

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 40]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 169]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 105]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 105]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 106]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 135]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 179]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [VEc 9]: http: fix timer pool assert crash due to timer freed when timeout in main thread
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 179]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 144]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 173]: ip: discard old trace flag after copy

**ohnatiuk** <ohnatiuk@cisco.com>:

  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VeC 37]: build: use VPP_BUILD_TOPDIR from environment if set
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VeC 37]: vapi: remove directory name from include guards

**sonsumin** <itoodo12@gmail.com>:

  | `41670 <https:////gerrit.fd.io/r/c/vpp/+/41670>`_ [vEC 3]: refactor: remove unnecessary comments from code
  | `41669 <https:////gerrit.fd.io/r/c/vpp/+/41669>`_ [vEC 3]: fix: resolve Checkstyle errors
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [vEC 3]: refactor(nat44): change argument order and parsing format for static mapping

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
authors          87
maintainers      35
committers       0
abandoned        0
================ ===

