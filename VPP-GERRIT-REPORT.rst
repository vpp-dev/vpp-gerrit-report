
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2024-11-25, 02:39:05
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
  | `41868 <https:////gerrit.fd.io/r/c/vpp/+/41868>`_ [VECr 2]: build: support anolis8 operation for vpp
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [VECr 3]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 25]: build: add SHA256 checksums for external downloaded dependencies

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `41654 <https:////gerrit.fd.io/r/c/vpp/+/41654>`_ [VECr 3]: cnat: add support for icmp traceroute

dns: **Dave Barach** <vpp@barachs.net>
  | `41922 <https:////gerrit.fd.io/r/c/vpp/+/41922>`_ [VECr 1]: dns: fix checksum and support upstreaming ip6
  | `41921 <https:////gerrit.fd.io/r/c/vpp/+/41921>`_ [VECr 1]: dns: fix dns both send A and AAAA will fetch error response
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [VECr 3]: dns: did't shall resolve before enable
  | `41864 <https:////gerrit.fd.io/r/c/vpp/+/41864>`_ [VECr 3]: dns: cli support enable dns and config server addr

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 0]: http: connection upgrade mechanism

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 0]: http: connection upgrade mechanism

http: **Florin Coras** <fcoras@cisco.com>
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 0]: http: connection upgrade mechanism

interface: **Dave Barach** <vpp@barachs.net>
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 16]: session: add ip4-fib-id and ip6-fib-id to app ns CLI

libmemif: **Mohsin Kazmi** <sykazmi@cisco.com>
  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VECr 12]: libmemif: Fixed strlcpy symbol detection.

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 18]: linux-cp: Add VRF synchronization

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VECr 28]: nat: refactor argument order for nat44-ed static mapping
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `41717 <https:////gerrit.fd.io/r/c/vpp/+/41717>`_ [VECr 26]: nat: add clear session for nat44-ed
  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VECr 28]: nat: refactor argument order for nat44-ed static mapping

session: **Florin Coras** <fcoras@cisco.com>
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 4]: session: add auto sdl
  | `41837 <https:////gerrit.fd.io/r/c/vpp/+/41837>`_ [VECr 10]: session: clean up session table when re-adding an existing application namespace
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 16]: session: add ip4-fib-id and ip6-fib-id to app ns CLI
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

svm: **Dave Barach** <vpp@barachs.net>
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [VECr 4]: svm: fix check bitmap logic error

tcp: **Florin Coras** <fcoras@cisco.com>
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 4]: session: add auto sdl
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41849 <https:////gerrit.fd.io/r/c/vpp/+/41849>`_ [VECr 2]: tests: use v3 version of session sdl dump api in ip6 test
  | `41654 <https:////gerrit.fd.io/r/c/vpp/+/41654>`_ [VECr 3]: cnat: add support for icmp traceroute
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 4]: session: add auto sdl
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 16]: session: add ip4-fib-id and ip6-fib-id to app ns CLI
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 25]: session: make local port allocator fib aware

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 4]: session: add auto sdl

vcl: **Florin Coras** <fcoras@cisco.com>
  | `41801 <https:////gerrit.fd.io/r/c/vpp/+/41801>`_ [VECr 6]: vcl: support pre/post cb before mq wait

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VECr 0]: vlib: mark cli quit command as mp_safe
  | `41762 <https:////gerrit.fd.io/r/c/vpp/+/41762>`_ [VECr 25]: vlib: add CLI command to show nodes supporting packet tracing
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 27]: vlib: improve core pinning

vpp: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 27]: vlib: improve core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 27]: vlib: improve core pinning

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 111]: ip: added CLI command to set ip6 reassembly params

**Alexander Chernavin** <chernavin@mts.ru>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 151]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 45]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 62]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 114]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Artem Glazychev** <glazychev@mts.ru>:

  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VeC 80]: sr: fix sr_policy fib table

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41378 <https:////gerrit.fd.io/r/c/vpp/+/41378>`_ [VeC 80]: vat2: docs
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 88]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 90]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 104]: docs: vpp_papi example script

**Benoît Ganne** <bganne@cisco.com>:

  | `41857 <https:////gerrit.fd.io/r/c/vpp/+/41857>`_ [vEC 4]: svm: fix overflow when no region is big enough
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 130]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 48]: memif: add support for per queue counters
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 158]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 162]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 165]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 167]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 167]: ipsec: Add option to configure the handoff worker queue size

**Dave Wallace** <dwallacelf@gmail.com>:

  | `41457 <https:////gerrit.fd.io/r/c/vpp/+/41457>`_ [VeC 33]: tests: remove use of python 2.7 compatibility module 'six'
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VeC 33]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 44]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 44]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 81]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 94]: qos: fix qos record cli

**Guillaume Solignac** <gsoligna@cisco.com>:

  | `41839 <https:////gerrit.fd.io/r/c/vpp/+/41839>`_ [VEc 9]: armada: fix feature arc for secondary interfaces

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 32]: vlib: require main core with 'skip-cores' attribute

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 55]: vppinfra: add ARM neoverse-v2 support
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 60]: vlib: fix seed parse error

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [veC 42]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 39]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 40]: docs: Add doc for API Trace Tools
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [Vec 44]: vxlan: move vxlan-gpe to a plugin
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 74]: api-trace: enable both rx and tx direction

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 157]: vapi: only wait if queue is empty

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 58]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 46]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 60]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 62]: vlib: add vfio-token parsing support
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 167]: octeon: fix oct_free() and free allocated memory

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 38]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 165]: ipsec: add SA validity check fetching IPsec SA

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `41721 <https:////gerrit.fd.io/r/c/vpp/+/41721>`_ [VeC 33]: ipsec: fix spd fast path single match compare for ipv6

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 83]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 83]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 83]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 83]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 83]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 83]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 83]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 83]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 83]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 83]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 83]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 83]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 83]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VeC 41]: linux-cp: do ip6-ll cleanup on interface removal
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 104]: vapi: remove plugin dependency from tests

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 178]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 178]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Tom Jones** <thj@freebsd.org>:

  | `41355 <https:////gerrit.fd.io/r/c/vpp/+/41355>`_ [VeC 115]: build: Add FreeBSD install-dep support

**Varun Rapelly** <vrapelly@marvell.com>:

  | `41591 <https:////gerrit.fd.io/r/c/vpp/+/41591>`_ [VEc 2]: tls: add async processing support

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 90]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 44]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 48]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 55]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 55]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 55]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 55]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 55]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 55]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 55]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 55]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 55]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 55]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 55]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 55]: stats: add sw interface tags to statseg
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 155]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 155]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 156]: fib: fix invalid udp encap id cases

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 55]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 61]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 75]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 59]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `41860 <https:////gerrit.fd.io/r/c/vpp/+/41860>`_ [vEC 3]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41854 <https:////gerrit.fd.io/r/c/vpp/+/41854>`_ [vEC 4]: svm: fix check bitmap logic error
  | `41852 <https:////gerrit.fd.io/r/c/vpp/+/41852>`_ [vEC 4]: svm: fix check bitmap logic error
  | `41851 <https:////gerrit.fd.io/r/c/vpp/+/41851>`_ [vEC 4]: svm: fix check bitmap logic error
  | `41850 <https:////gerrit.fd.io/r/c/vpp/+/41850>`_ [vEC 4]: Makefile: support anolis8 operation for vpp
  | `41848 <https:////gerrit.fd.io/r/c/vpp/+/41848>`_ [vEC 4]: Makefile: support anolis8 operation for vpp Type: improvement

**ohnatiuk** <ohnatiuk@cisco.com>:

  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VeC 87]: build: use VPP_BUILD_TOPDIR from environment if set
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VeC 87]: vapi: remove directory name from include guards

**shaohui jin** <jinshaohui789@163.com>:

  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [vEC 3]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.
  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [vEC 3]: dhcp:dhcp request packets always use the first server address.

**sonsumin** <itoodo12@gmail.com>:

  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 53]: refactor(nat44): change argument order and parsing format for static mapping

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
authors          94
maintainers      24
committers       0
abandoned        0
================ ===

