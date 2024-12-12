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
generated on Thursday 2024-12-12, 02:41:16
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

  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VECR 2]: libmemif: Fixed strlcpy symbol detection.

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `41992 <https:////gerrit.fd.io/r/c/vpp/+/41992>`_ [VECr 0]: docs: add examples for BPF trace filtering

build: **Damjan Marion** <damarion@cisco.com>
  | `41993 <https:////gerrit.fd.io/r/c/vpp/+/41993>`_ [VECr 0]: build: archive install-*-deps logs when run in ci
  | `41868 <https:////gerrit.fd.io/r/c/vpp/+/41868>`_ [VECr 19]: build: support anolis8 operation for vpp
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [VECr 20]: build: ubuntu24.04 llvm[18] lack of the header and library of asan

classify: **Dave Barach** <vpp@barachs.net>
  | `41966 <https:////gerrit.fd.io/r/c/vpp/+/41966>`_ [VECr 1]: classify: add options to filter out the geneve packets

dev: **Damjan Marion** <damarion@cisco.com>
  | `41946 <https:////gerrit.fd.io/r/c/vpp/+/41946>`_ [VECr 0]: dev: assign tx queue to all threads

dns: **Dave Barach** <vpp@barachs.net>
  | `41922 <https:////gerrit.fd.io/r/c/vpp/+/41922>`_ [VECr 18]: dns: fix checksum and support upstreaming ip6
  | `41921 <https:////gerrit.fd.io/r/c/vpp/+/41921>`_ [VECr 18]: dns: fix dns both send A and AAAA will fetch error response
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [VECr 20]: dns: did't shall resolve before enable
  | `41864 <https:////gerrit.fd.io/r/c/vpp/+/41864>`_ [VECr 20]: dns: cli support enable dns and config server addr

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 0]: sflow: initial checkin
  | `41992 <https:////gerrit.fd.io/r/c/vpp/+/41992>`_ [VECr 0]: docs: add examples for BPF trace filtering

ebuild: **Dave Barach** <vpp@barachs.net>
  | `41961 <https:////gerrit.fd.io/r/c/vpp/+/41961>`_ [VECr 5]: build: fix PATH with multiple /usr/lib* matches

fib: **Neale Ranns** <neale@graphiant.com>
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 14]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 14]: fib: fix udp encap mp-safe ops and id validation

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41906 <https:////gerrit.fd.io/r/c/vpp/+/41906>`_ [VECr 0]: hs-test: added a test counter and time elapsed

interface: **Dave Barach** <vpp@barachs.net>
  | `41985 <https:////gerrit.fd.io/r/c/vpp/+/41985>`_ [VECr 1]: api: fix crash in pcap capture api
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 6]: stats: add sw interface tags to statseg

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VECr 15]: ip: fix ICMP inner payload parsing

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `41721 <https:////gerrit.fd.io/r/c/vpp/+/41721>`_ [VECr 6]: ipsec: fix spd fast path single match compare for ipv6

map: **Ole Troan** <ot@cisco.com>, **Jon Loeliger** <jdl@netgate.com>
  | `41971 <https:////gerrit.fd.io/r/c/vpp/+/41971>`_ [VECr 5]: map: map_domain_dump fails for empty tag

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 0]: sflow: initial checkin
  | `41955 <https:////gerrit.fd.io/r/c/vpp/+/41955>`_ [VECr 9]: crypto: add config option to adjust crypto sw scheduler queue size

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VECr 15]: ip: fix ICMP inner payload parsing

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41972 <https:////gerrit.fd.io/r/c/vpp/+/41972>`_ [VECr 5]: papi: vpp_papi asyncio support
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 6]: stats: add sw interface tags to statseg

pg: **Dave Barach** <vpp@barachs.net>
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VECr 0]: pg: misc improvements and fixes

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 8]: session: make local port allocator fib aware

snort: **Damjan Marion** <damarion@cisco.com>
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 1]: snort: support multiple instances per interface

svm: **Dave Barach** <vpp@barachs.net>
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [VECr 21]: svm: fix check bitmap logic error

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 8]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 0]: sflow: initial checkin
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VECr 0]: pg: misc improvements and fixes
  | `41985 <https:////gerrit.fd.io/r/c/vpp/+/41985>`_ [VECr 1]: api: fix crash in pcap capture api
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 1]: snort: support multiple instances per interface
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 6]: stats: add sw interface tags to statseg
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 14]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 14]: fib: fix udp encap mp-safe ops and id validation

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 8]: session: make local port allocator fib aware
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 14]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 14]: fib: fix invalid udp encap id cases

vcl: **Florin Coras** <fcoras@cisco.com>
  | `41801 <https:////gerrit.fd.io/r/c/vpp/+/41801>`_ [VECr 2]: vcl: support pre/post cb before mq wait

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VECr 17]: vlib: mark cli quit command as mp_safe

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <chernavin@mts.ru>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 168]: bonding: make link state depend on active members

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 62]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 79]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 131]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Artem Glazychev** <glazychev@mts.ru>:

  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VeC 97]: sr: fix sr_policy fib table

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 105]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 107]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 121]: docs: vpp_papi example script

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 65]: memif: add support for per queue counters
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 175]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 179]: hash: Add cli to enable soft interface hashing based on esp

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VeC 50]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 61]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 61]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 98]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 111]: qos: fix qos record cli

**Guillaume Solignac** <gsoligna@cisco.com>:

  | `41839 <https:////gerrit.fd.io/r/c/vpp/+/41839>`_ [VEc 26]: armada: fix feature arc for secondary interfaces

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 49]: vlib: require main core with 'skip-cores' attribute

**Jay Wang** <jay.wang2@arm.com>:

  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VeC 72]: vppinfra: add ARM neoverse-v2 support
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VeC 77]: vlib: fix seed parse error

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 35]: linux-cp: Add VRF synchronization

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [veC 59]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VEc 14]: vxlan: move vxlan-gpe to a plugin
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 14]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 14]: docs: Add doc for API Trace Tools
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 91]: api-trace: enable both rx and tx direction

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 75]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 63]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 77]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 79]: vlib: add vfio-token parsing support

**Ole Troan** <otroan@employees.org>:

  | `41717 <https:////gerrit.fd.io/r/c/vpp/+/41717>`_ [VeC 43]: nat: add clear session for nat44-ed
  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 55]: ip6: don't forward packets with invalid source address

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 100]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 100]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 100]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 100]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 100]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 100]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 100]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 100]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 100]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 100]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 100]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 100]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 100]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VeC 58]: linux-cp: do ip6-ll cleanup on interface removal

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [vEC 0]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 107]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 61]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 65]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 72]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 72]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 72]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 72]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 72]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 72]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 72]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 72]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 72]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 72]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 72]: stats: add interface link speed to statseg
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 172]: fib: fix fib entry tracking crash on table remove

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 72]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 78]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 92]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 76]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `41860 <https:////gerrit.fd.io/r/c/vpp/+/41860>`_ [vEC 20]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41854 <https:////gerrit.fd.io/r/c/vpp/+/41854>`_ [vEC 21]: svm: fix check bitmap logic error
  | `41852 <https:////gerrit.fd.io/r/c/vpp/+/41852>`_ [vEC 21]: svm: fix check bitmap logic error
  | `41851 <https:////gerrit.fd.io/r/c/vpp/+/41851>`_ [vEC 21]: svm: fix check bitmap logic error
  | `41850 <https:////gerrit.fd.io/r/c/vpp/+/41850>`_ [vEC 21]: Makefile: support anolis8 operation for vpp
  | `41848 <https:////gerrit.fd.io/r/c/vpp/+/41848>`_ [vEC 21]: Makefile: support anolis8 operation for vpp Type: improvement

**ohnatiuk** <ohnatiuk@cisco.com>:

  | `41501 <https:////gerrit.fd.io/r/c/vpp/+/41501>`_ [VeC 104]: build: use VPP_BUILD_TOPDIR from environment if set
  | `41499 <https:////gerrit.fd.io/r/c/vpp/+/41499>`_ [VeC 104]: vapi: remove directory name from include guards

**shaohui jin** <jinshaohui789@163.com>:

  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [vEC 20]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.
  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [vEC 20]: dhcp:dhcp request packets always use the first server address.

**sonsumin** <itoodo12@gmail.com>:

  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VeC 45]: nat: refactor argument order for nat44-ed static mapping
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 70]: refactor(nat44): change argument order and parsing format for static mapping

**steven luong** <sluong@cisco.com>:

  | `41846 <https:////gerrit.fd.io/r/c/vpp/+/41846>`_ [VEc 2]: session: add auto sdl

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
authors          79
maintainers      28
committers       1
abandoned        0
================ ===

