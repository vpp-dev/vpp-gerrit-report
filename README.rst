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
generated on Wednesday 2024-11-13, 02:28:47
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
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 13]: build: add SHA256 checksums for external downloaded dependencies

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 18]: sflow: initial checkin

http: **Florin Coras** <fcoras@cisco.com>
  | `41823 <https:////gerrit.fd.io/r/c/vpp/+/41823>`_ [VECr 0]: http: HTTP Datagrams and the Capsule Protocol

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `41824 <https:////gerrit.fd.io/r/c/vpp/+/41824>`_ [VECr 0]: http_static: api add keepalive-timeout

interface: **Dave Barach** <vpp@barachs.net>
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 4]: session: add ip4-fib-id and ip6-fib-id to app ns CLI

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VECr 29]: linux-cp: do ip6-ll cleanup on interface removal

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `41721 <https:////gerrit.fd.io/r/c/vpp/+/41721>`_ [VECr 21]: ipsec: fix spd fast path single match compare for ipv6

libmemif: **Mohsin Kazmi** <sykazmi@cisco.com>
  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VECr 0]: libmemif: Fixed strlcpy symbol detection.

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 6]: linux-cp: Add VRF synchronization
  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VECr 29]: linux-cp: do ip6-ll cleanup on interface removal

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VECr 16]: nat: refactor argument order for nat44-ed static mapping
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 18]: sflow: initial checkin
  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VECr 29]: linux-cp: do ip6-ll cleanup on interface removal

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `41717 <https:////gerrit.fd.io/r/c/vpp/+/41717>`_ [VECr 14]: nat: add clear session for nat44-ed
  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VECr 16]: nat: refactor argument order for nat44-ed static mapping
  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VECr 29]: linux-cp: do ip6-ll cleanup on interface removal

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `41822 <https:////gerrit.fd.io/r/c/vpp/+/41822>`_ [VECr 1]: octeon: set rss flowkey after mac update
  | `41821 <https:////gerrit.fd.io/r/c/vpp/+/41821>`_ [VECr 1]: octeon: fix compilation for octeon

session: **Florin Coras** <fcoras@cisco.com>
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 4]: session: add ip4-fib-id and ip6-fib-id to app ns CLI
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 13]: session: make local port allocator fib aware

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 13]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41824 <https:////gerrit.fd.io/r/c/vpp/+/41824>`_ [VECr 0]: http_static: api add keepalive-timeout
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 4]: session: add ip4-fib-id and ip6-fib-id to app ns CLI
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 18]: sflow: initial checkin
  | `41457 <https:////gerrit.fd.io/r/c/vpp/+/41457>`_ [VECr 21]: tests: remove use of python 2.7 compatibility module 'six'

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 13]: session: make local port allocator fib aware

vcl: **Florin Coras** <fcoras@cisco.com>
  | `41801 <https:////gerrit.fd.io/r/c/vpp/+/41801>`_ [VECr 4]: vcl: support pre/post cb before mq wait
  | `41798 <https:////gerrit.fd.io/r/c/vpp/+/41798>`_ [VECr 10]: vcl: make ldp workers thread local
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 21]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `41762 <https:////gerrit.fd.io/r/c/vpp/+/41762>`_ [VECr 13]: vlib: add CLI command to show nodes supporting packet tracing
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 15]: vlib: improve core pinning
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VECr 20]: vlib: require main core with 'skip-cores' attribute

vpp: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 15]: vlib: improve core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 15]: vlib: improve core pinning

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 99]: ip: added CLI command to set ip6 reassembly params

**Alexander Chernavin** <chernavin@mts.ru>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 139]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 33]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 50]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 102]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Artem Glazychev** <glazychev@mts.ru>:

  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VeC 68]: sr: fix sr_policy fib table

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41378 <https:////gerrit.fd.io/r/c/vpp/+/41378>`_ [VeC 68]: vat2: docs
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 76]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 78]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 92]: docs: vpp_papi example script

**Benoît Ganne** <bganne@cisco.com>:

  | `41691 <https:////gerrit.fd.io/r/c/vpp/+/41691>`_ [VeC 35]: vlib: add clib_stack_frame_get_raw()
  | `41544 <https:////gerrit.fd.io/r/c/vpp/+/41544>`_ [VeC 64]: tracenode: fix pcap capture if packet is also traced
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 118]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 36]: memif: add support for per queue counters
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 146]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 150]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 153]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 155]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 155]: ipsec: Add option to configure the handoff worker queue size

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40891 <https:////gerrit.fd.io/r/c/vpp/+/40891>`_ [VEc 3]: build: add vpp-opt-deps package

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 32]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 32]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 69]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 82]: qos: fix qos record cli

**Florin Coras** <florin.coras@gmail.com>:

  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VeC 123]: api: support api clients with real-time scheduling

**Ivan Ivanets** <iivanets@cisco.com>:

  | `41799 <https:////gerrit.fd.io/r/c/vpp/+/41799>`_ [VEc 3]: tests: vpp_qemu_utils with concurrency handling
  | `41497 <https:////gerrit.fd.io/r/c/vpp/+/41497>`_ [veC 75]: misc: patch to check behavior of test for BFD API when bfd_udp_mod_session function doesn't work correctly

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 43]: vppinfra: add ARM neoverse-v2 support
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 48]: vlib: fix seed parse error

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [vEC 30]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 27]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 28]: docs: Add doc for API Trace Tools
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [Vec 32]: vxlan: move vxlan-gpe to a plugin
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 62]: api-trace: enable both rx and tx direction

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 145]: vapi: only wait if queue is empty

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 174]: classify: add name to classify heap

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41648 <https:////gerrit.fd.io/r/c/vpp/+/41648>`_ [VEc 12]: pg: fix the buffer deletion
  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 46]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 34]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 48]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 50]: vlib: add vfio-token parsing support
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 155]: octeon: fix oct_free() and free allocated memory

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [VEc 26]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 153]: ipsec: add SA validity check fetching IPsec SA

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 71]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 71]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 71]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 71]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 71]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 71]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 71]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 71]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 71]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 71]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 71]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 71]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 71]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 92]: vapi: remove plugin dependency from tests

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 166]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 166]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Tom Jones** <thj@freebsd.org>:

  | `41355 <https:////gerrit.fd.io/r/c/vpp/+/41355>`_ [VeC 103]: build: Add FreeBSD install-dep support

**Varun Rapelly** <vrapelly@marvell.com>:

  | `41591 <https:////gerrit.fd.io/r/c/vpp/+/41591>`_ [VEc 0]: tls: add async processing support

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 78]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 32]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 36]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 43]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 43]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 43]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 43]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 43]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 43]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 43]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 43]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 43]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 43]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 43]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 43]: stats: add sw interface tags to statseg
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 143]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 143]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 144]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 173]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 43]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 49]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 63]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 47]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**ohnatiuk** <ohnatiuk@cisco.com>:

  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VeC 75]: build: use VPP_BUILD_TOPDIR from environment if set
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VeC 75]: vapi: remove directory name from include guards

**sonsumin** <itoodo12@gmail.com>:

  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 41]: refactor(nat44): change argument order and parsing format for static mapping

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
authors          88
maintainers      21
committers       0
abandoned        0
================ ===

