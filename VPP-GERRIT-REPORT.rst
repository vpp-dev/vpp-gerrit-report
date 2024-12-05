
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2024-12-05, 02:42:15
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
  | `41868 <https:////gerrit.fd.io/r/c/vpp/+/41868>`_ [VECr 12]: build: support anolis8 operation for vpp
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [VECr 13]: build: ubuntu24.04 llvm[18] lack of the header and library of asan

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41956 <https:////gerrit.fd.io/r/c/vpp/+/41956>`_ [VECr 0]: misc: move to a plugin

classify: **Dave Barach** <vpp@barachs.net>
  | `41933 <https:////gerrit.fd.io/r/c/vpp/+/41933>`_ [VECr 8]: bpf_trace_filter: allow pcap filtering without classifier

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `41654 <https:////gerrit.fd.io/r/c/vpp/+/41654>`_ [VECr 0]: cnat: add support for icmp traceroute

dev: **Damjan Marion** <damarion@cisco.com>
  | `41946 <https:////gerrit.fd.io/r/c/vpp/+/41946>`_ [VECr 5]: dev: assign tx queue to all threads

dns: **Dave Barach** <vpp@barachs.net>
  | `41922 <https:////gerrit.fd.io/r/c/vpp/+/41922>`_ [VECr 11]: dns: fix checksum and support upstreaming ip6
  | `41921 <https:////gerrit.fd.io/r/c/vpp/+/41921>`_ [VECr 11]: dns: fix dns both send A and AAAA will fetch error response
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [VECr 13]: dns: did't shall resolve before enable
  | `41864 <https:////gerrit.fd.io/r/c/vpp/+/41864>`_ [VECr 13]: dns: cli support enable dns and config server addr

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41956 <https:////gerrit.fd.io/r/c/vpp/+/41956>`_ [VECr 0]: misc: move to a plugin

ebuild: **Dave Barach** <vpp@barachs.net>
  | `41961 <https:////gerrit.fd.io/r/c/vpp/+/41961>`_ [VECr 0]: build: fix PATH with multiple /usr/lib* matches

fib: **Neale Ranns** <neale@graphiant.com>
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 7]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 7]: fib: fix udp encap mp-safe ops and id validation

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41899 <https:////gerrit.fd.io/r/c/vpp/+/41899>`_ [VECr 1]: hs-test: added multi-threaded proxy test (iperf)
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 7]: http: connection upgrade mechanism

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 7]: http: connection upgrade mechanism

http: **Florin Coras** <fcoras@cisco.com>
  | `41918 <https:////gerrit.fd.io/r/c/vpp/+/41918>`_ [VECr 7]: http: connection upgrade mechanism

interface: **Dave Barach** <vpp@barachs.net>
  | `41933 <https:////gerrit.fd.io/r/c/vpp/+/41933>`_ [VECr 8]: bpf_trace_filter: allow pcap filtering without classifier
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 26]: session: add ip4-fib-id and ip6-fib-id to app ns CLI

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `41956 <https:////gerrit.fd.io/r/c/vpp/+/41956>`_ [VECr 0]: misc: move to a plugin
  | `41869 <https:////gerrit.fd.io/r/c/vpp/+/41869>`_ [VECr 5]: ip: add enable ip4 api
  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VECr 8]: ip: fix ICMP inner payload parsing

libmemif: **Mohsin Kazmi** <sykazmi@cisco.com>
  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VECr 22]: libmemif: Fixed strlcpy symbol detection.

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 28]: linux-cp: Add VRF synchronization

memif: **Damjan Marion** <damarion@cisco.com>
  | `41947 <https:////gerrit.fd.io/r/c/vpp/+/41947>`_ [VECr 0]: memif: add num pkts received/sent per queue

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41956 <https:////gerrit.fd.io/r/c/vpp/+/41956>`_ [VECr 0]: misc: move to a plugin
  | `41948 <https:////gerrit.fd.io/r/c/vpp/+/41948>`_ [VECr 0]: crypto: add config option to adjust crypto sw scheduler queue size
  | `41955 <https:////gerrit.fd.io/r/c/vpp/+/41955>`_ [VECr 2]: crypto: add config option to adjust crypto sw scheduler queue size
  | `41933 <https:////gerrit.fd.io/r/c/vpp/+/41933>`_ [VECr 8]: bpf_trace_filter: allow pcap filtering without classifier

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VECr 8]: ip: fix ICMP inner payload parsing

pppoe: **Hongjun Ni** <hongjun.ni@intel.com>
  | `41956 <https:////gerrit.fd.io/r/c/vpp/+/41956>`_ [VECr 0]: misc: move to a plugin

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 1]: session: make local port allocator fib aware
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 14]: session: add auto sdl
  | `41837 <https:////gerrit.fd.io/r/c/vpp/+/41837>`_ [VECr 20]: session: clean up session table when re-adding an existing application namespace
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 26]: session: add ip4-fib-id and ip6-fib-id to app ns CLI

svm: **Dave Barach** <vpp@barachs.net>
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [VECr 14]: svm: fix check bitmap logic error

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `41900 <https:////gerrit.fd.io/r/c/vpp/+/41900>`_ [VECr 1]: tap: update tap_flags

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 1]: session: make local port allocator fib aware
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 14]: session: add auto sdl

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41654 <https:////gerrit.fd.io/r/c/vpp/+/41654>`_ [VECr 0]: cnat: add support for icmp traceroute
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 7]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 7]: fib: fix udp encap mp-safe ops and id validation
  | `41933 <https:////gerrit.fd.io/r/c/vpp/+/41933>`_ [VECr 8]: bpf_trace_filter: allow pcap filtering without classifier
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 14]: session: add auto sdl
  | `41815 <https:////gerrit.fd.io/r/c/vpp/+/41815>`_ [VECr 26]: session: add ip4-fib-id and ip6-fib-id to app ns CLI

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 1]: session: make local port allocator fib aware
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 7]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 7]: fib: fix invalid udp encap id cases
  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VECr 14]: session: add auto sdl

vcl: **Florin Coras** <fcoras@cisco.com>
  | `41801 <https:////gerrit.fd.io/r/c/vpp/+/41801>`_ [VECr 2]: vcl: support pre/post cb before mq wait

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VECr 10]: vlib: mark cli quit command as mp_safe

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VeC 121]: ip: added CLI command to set ip6 reassembly params

**Alexander Chernavin** <chernavin@mts.ru>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 161]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 55]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 72]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 124]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Artem Glazychev** <glazychev@mts.ru>:

  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VeC 90]: sr: fix sr_policy fib table

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 98]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 100]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 114]: docs: vpp_papi example script

**Benoît Ganne** <bganne@cisco.com>:

  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VeC 140]: pg: fix offload offsets for ip4/6-input

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 58]: memif: add support for per queue counters
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 168]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 172]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 175]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 177]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 177]: ipsec: Add option to configure the handoff worker queue size

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VeC 43]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 54]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 54]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 91]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 104]: qos: fix qos record cli

**Guillaume Solignac** <gsoligna@cisco.com>:

  | `41950 <https:////gerrit.fd.io/r/c/vpp/+/41950>`_ [vEC 2]: Update the link_state based on hw interface link is up
  | `41839 <https:////gerrit.fd.io/r/c/vpp/+/41839>`_ [VEc 19]: armada: fix feature arc for secondary interfaces

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 42]: vlib: require main core with 'skip-cores' attribute

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 65]: vppinfra: add ARM neoverse-v2 support
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 70]: vlib: fix seed parse error

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [veC 52]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VEc 7]: vxlan: move vxlan-gpe to a plugin
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 7]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 7]: docs: Add doc for API Trace Tools
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 84]: api-trace: enable both rx and tx direction

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 68]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 56]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 70]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 72]: vlib: add vfio-token parsing support
  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 177]: octeon: fix oct_free() and free allocated memory

**Ole Troan** <otroan@employees.org>:

  | `41717 <https:////gerrit.fd.io/r/c/vpp/+/41717>`_ [VeC 36]: nat: add clear session for nat44-ed
  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 48]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 175]: ipsec: add SA validity check fetching IPsec SA

**Pim van Pelt** <pim@ipng.nl>:

  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VeC 40]: sflow: initial checkin

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `41721 <https:////gerrit.fd.io/r/c/vpp/+/41721>`_ [VeC 43]: ipsec: fix spd fast path single match compare for ipv6

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 93]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 93]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 93]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 93]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 93]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 93]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 93]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 93]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 93]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 93]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 93]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 93]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 93]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VeC 51]: linux-cp: do ip6-ll cleanup on interface removal

**Varun Rapelly** <vrapelly@marvell.com>:

  | `41591 <https:////gerrit.fd.io/r/c/vpp/+/41591>`_ [VEc 5]: tls: add async processing support

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 100]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 54]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 58]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 65]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 65]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 65]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 65]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 65]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 65]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 65]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 65]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 65]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 65]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 65]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 65]: stats: add sw interface tags to statseg
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 165]: fib: fix fib entry tracking crash on table remove

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 65]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 71]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 85]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 69]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `41860 <https:////gerrit.fd.io/r/c/vpp/+/41860>`_ [vEC 13]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41854 <https:////gerrit.fd.io/r/c/vpp/+/41854>`_ [vEC 14]: svm: fix check bitmap logic error
  | `41852 <https:////gerrit.fd.io/r/c/vpp/+/41852>`_ [vEC 14]: svm: fix check bitmap logic error
  | `41851 <https:////gerrit.fd.io/r/c/vpp/+/41851>`_ [vEC 14]: svm: fix check bitmap logic error
  | `41850 <https:////gerrit.fd.io/r/c/vpp/+/41850>`_ [vEC 14]: Makefile: support anolis8 operation for vpp
  | `41848 <https:////gerrit.fd.io/r/c/vpp/+/41848>`_ [vEC 14]: Makefile: support anolis8 operation for vpp Type: improvement

**ohnatiuk** <ohnatiuk@cisco.com>:

  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VeC 97]: build: use VPP_BUILD_TOPDIR from environment if set
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VeC 97]: vapi: remove directory name from include guards

**shaohui jin** <jinshaohui789@163.com>:

  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [vEC 13]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.
  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [vEC 13]: dhcp:dhcp request packets always use the first server address.

**sonsumin** <itoodo12@gmail.com>:

  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VeC 38]: nat: refactor argument order for nat44-ed static mapping
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 63]: refactor(nat44): change argument order and parsing format for static mapping

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
maintainers      30
committers       0
abandoned        0
================ ===

