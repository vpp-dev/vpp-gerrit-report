
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2025-01-11, 02:28:50
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

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `42083 <https:////gerrit.fd.io/r/c/vpp/+/42083>`_ [VECr 4]: af_packet: worker thread call vlib_log coredump
  | `41994 <https:////gerrit.fd.io/r/c/vpp/+/41994>`_ [VECr 24]: af_packet: fix crash on af_packet_fd_error

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `42082 <https:////gerrit.fd.io/r/c/vpp/+/42082>`_ [VECr 10]: arp: fix command resolve and config filed exist differ

build: **Damjan Marion** <damarion@cisco.com>
  | `42121 <https:////gerrit.fd.io/r/c/vpp/+/42121>`_ [VECr 1]: dpdk: bump to DPDK 24.11.1
  | `42113 <https:////gerrit.fd.io/r/c/vpp/+/42113>`_ [VECr 1]: build: support anolis8 operation for vpp
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 4]: vppinfra: add ARM neoverse-v2 support
  | `42086 <https:////gerrit.fd.io/r/c/vpp/+/42086>`_ [VECr 7]: build: add support for debian trixie

classify: **Dave Barach** <vpp@barachs.net>
  | `41966 <https:////gerrit.fd.io/r/c/vpp/+/41966>`_ [VECr 0]: classify: add options to filter out the geneve packets
  | `42034 <https:////gerrit.fd.io/r/c/vpp/+/42034>`_ [VECr 24]: classify: cli filter support for dynamic delete

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `42066 <https:////gerrit.fd.io/r/c/vpp/+/42066>`_ [VECr 18]: cnat: fix udp checksum calculation

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `42134 <https:////gerrit.fd.io/r/c/vpp/+/42134>`_ [VECr 0]: crypto: remove AEAD opt types
  | `42116 <https:////gerrit.fd.io/r/c/vpp/+/42116>`_ [VECr 0]: vnet: add async algo support for ctr sha2

dev: **Damjan Marion** <damarion@cisco.com>
  | `42110 <https:////gerrit.fd.io/r/c/vpp/+/42110>`_ [VECr 1]: dev: add cli show dev class

dns: **Dave Barach** <vpp@barachs.net>
  | `42080 <https:////gerrit.fd.io/r/c/vpp/+/42080>`_ [VECr 1]: dns: fix server no reply but still retry problem
  | `42072 <https:////gerrit.fd.io/r/c/vpp/+/42072>`_ [VECr 4]: dns: dns resolution optimisation and bug fixes
  | `42074 <https:////gerrit.fd.io/r/c/vpp/+/42074>`_ [VECr 14]: dns: dns api, cli and vat resolve interface implements
  | `42041 <https:////gerrit.fd.io/r/c/vpp/+/42041>`_ [VECr 23]: dns: did't shall resolve before enable

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 3]: vlib: fix seed parse error
  | `42059 <https:////gerrit.fd.io/r/c/vpp/+/42059>`_ [VECr 20]: tests: fix docs compile syntax warning
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `42121 <https:////gerrit.fd.io/r/c/vpp/+/42121>`_ [VECr 1]: dpdk: bump to DPDK 24.11.1

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `42108 <https:////gerrit.fd.io/r/c/vpp/+/42108>`_ [VECr 1]: ip: fix local csum check
  | `42123 <https:////gerrit.fd.io/r/c/vpp/+/42123>`_ [VECr 1]: ip: skip options handling for locally originated packets

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `42112 <https:////gerrit.fd.io/r/c/vpp/+/42112>`_ [VECr 1]: l2: fix segment fault

lacp: **Steven Luong** <sluong@cisco.com>
  | `42124 <https:////gerrit.fd.io/r/c/vpp/+/42124>`_ [VECr 0]: linux-cp: Add support for LACP packets

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `42124 <https:////gerrit.fd.io/r/c/vpp/+/42124>`_ [VECr 0]: linux-cp: Add support for LACP packets
  | `42123 <https:////gerrit.fd.io/r/c/vpp/+/42123>`_ [VECr 1]: ip: skip options handling for locally originated packets
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 1]: linux-cp: Add VRF synchronization
  | `42065 <https:////gerrit.fd.io/r/c/vpp/+/42065>`_ [VECr 1]: linux-cp: fix segfault while receiving nl messages

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `42104 <https:////gerrit.fd.io/r/c/vpp/+/42104>`_ [VECr 3]: pg: fix tr to trace
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `42098 <https:////gerrit.fd.io/r/c/vpp/+/42098>`_ [VECr 3]: octeon: rework octeon crypto framework

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 20]: session: make local port allocator fib aware

snort: **Damjan Marion** <damarion@cisco.com>
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 4]: snort: support multiple instances per interface

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `41533 <https:////gerrit.fd.io/r/c/vpp/+/41533>`_ [VECr 1]: sr: fix sr_policy fib table

svm: **Dave Barach** <vpp@barachs.net>
  | `42050 <https:////gerrit.fd.io/r/c/vpp/+/42050>`_ [VECr 1]: svm: improve ooo try collect

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 20]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `42124 <https:////gerrit.fd.io/r/c/vpp/+/42124>`_ [VECr 0]: linux-cp: Add support for LACP packets
  | `42094 <https:////gerrit.fd.io/r/c/vpp/+/42094>`_ [VECr 1]: ipsec: add test for tun sa ip6 fast-path spd policy matching
  | `41970 <https:////gerrit.fd.io/r/c/vpp/+/41970>`_ [VECr 4]: snort: support multiple instances per interface
  | `42044 <https:////gerrit.fd.io/r/c/vpp/+/42044>`_ [VECr 23]: build: fix coverage for various lcov versions
  | `41680 <https:////gerrit.fd.io/r/c/vpp/+/41680>`_ [VECr 30]: sflow: initial checkin

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 20]: session: make local port allocator fib aware

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `42134 <https:////gerrit.fd.io/r/c/vpp/+/42134>`_ [VECr 0]: crypto: remove AEAD opt types

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 3]: vlib: fix seed parse error
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VECr 28]: vlib: require main core with 'skip-cores' attribute

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 4]: vppinfra: add ARM neoverse-v2 support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Slesarev** <aslesare@cisco.com>:

  | `41722 <https:////gerrit.fd.io/r/c/vpp/+/41722>`_ [VeC 32]: libmemif: Fixed strlcpy symbol detection.

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41914 <https:////gerrit.fd.io/r/c/vpp/+/41914>`_ [vEc 0]: pvti: add a doc with write-up, and fix CLI help
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [VeC 92]: acl: use ip4_preflen_to_mask instead of artisanal function
  | `41427 <https:////gerrit.fd.io/r/c/vpp/+/41427>`_ [veC 109]: TEST: remove a DVR test on 22.04
  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 161]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Bence Romsics** <bence.romsics@gmail.com>:

  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VeC 135]: vat2: fix -p in vat2 help text
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 137]: docs: Restore and update nat section of progressive tutorial
  | `41399 <https:////gerrit.fd.io/r/c/vpp/+/41399>`_ [VeC 151]: docs: vpp_papi example script

**Dau Do** <daudo@yahoo.com>:

  | `41538 <https:////gerrit.fd.io/r/c/vpp/+/41538>`_ [veC 95]: memif: add support for per queue counters

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [vEC 1]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 91]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 91]: vlib: add config for elog tracing
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 128]: vppapigen: fix enum format function

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `41467 <https:////gerrit.fd.io/r/c/vpp/+/41467>`_ [VeC 141]: qos: fix qos record cli

**Florian Larysch** <fl@n621.de>:

  | `41961 <https:////gerrit.fd.io/r/c/vpp/+/41961>`_ [VeC 35]: build: fix PATH with multiple /usr/lib* matches

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41985 <https:////gerrit.fd.io/r/c/vpp/+/41985>`_ [VeC 31]: api: fix crash in pcap capture api

**Kai Ji** <kai.ji@intel.com>:

  | `42042 <https:////gerrit.fd.io/r/c/vpp/+/42042>`_ [VEc 22]: dpdk: add in the VLAN offload flag for the iavf PMD driver

**Klement Sekera** <klement.sekera@gmail.com>:

  | `41935 <https:////gerrit.fd.io/r/c/vpp/+/41935>`_ [VeC 45]: ip: fix ICMP inner payload parsing

**Kyle McClammy** <kylem@serverforge.org>:

  | `41705 <https:////gerrit.fd.io/r/c/vpp/+/41705>`_ [veC 89]: Enabled building net_sfc driver in dpdk.mk Added SFN7042Q adapter and virtual functions to init.c and driver.c

**Lajos Katona** <katonalala@gmail.com>:

  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [Vec 44]: vxlan: move vxlan-gpe to a plugin
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 44]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 44]: docs: Add doc for API Trace Tools
  | `41545 <https:////gerrit.fd.io/r/c/vpp/+/41545>`_ [vec 121]: api-trace: enable both rx and tx direction

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `41435 <https:////gerrit.fd.io/r/c/vpp/+/41435>`_ [VeC 105]: vppinfra: add ARM Neoverse-V1 support

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41698 <https:////gerrit.fd.io/r/c/vpp/+/41698>`_ [VeC 93]: octeon: register callback to set max npa pools
  | `41459 <https:////gerrit.fd.io/r/c/vpp/+/41459>`_ [Vec 107]: dev: add support for vf device with vf_token
  | `41458 <https:////gerrit.fd.io/r/c/vpp/+/41458>`_ [Vec 109]: vlib: add vfio-token parsing support

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VEc 17]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events
  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [VEc 17]: ping: Allow to specify a source interface in ping binary API

**Ole Troan** <otroan@employees.org>:

  | `41342 <https:////gerrit.fd.io/r/c/vpp/+/41342>`_ [Vec 85]: ip6: don't forward packets with invalid source address

**Pierre Pfister** <ppfister@cisco.com>:

  | `42032 <https:////gerrit.fd.io/r/c/vpp/+/42032>`_ [vEC 24]: clib: add full simulated time support

**Rabei Becheikh** <rabei.becheikh@enigmedia.es>:

  | `41519 <https:////gerrit.fd.io/r/c/vpp/+/41519>`_ [VeC 130]: flowprobe: Fix the problem of Network Byte Order for Ethernet type
  | `41518 <https:////gerrit.fd.io/r/c/vpp/+/41518>`_ [veC 130]: flowprobe:   Fix the problem of Network Byte Order for Ethernet type Type: fix
  | `41517 <https:////gerrit.fd.io/r/c/vpp/+/41517>`_ [veC 130]: flowprobe: Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41516 <https:////gerrit.fd.io/r/c/vpp/+/41516>`_ [veC 130]: flowprobe:Fix the problem of  Network Byte Order for Ethernet type Type:fix
  | `41515 <https:////gerrit.fd.io/r/c/vpp/+/41515>`_ [veC 130]: flowprobe:   Fix the problem of  Network Byte Order for Ethernet type Type: fix
  | `41514 <https:////gerrit.fd.io/r/c/vpp/+/41514>`_ [veC 130]: fowprobe:   Fix the problem with Network Byte Order for Ethernet type Type: fix
  | `41513 <https:////gerrit.fd.io/r/c/vpp/+/41513>`_ [veC 130]: Flowprobe: Fix etherType value for IPFIX (Network Byte Order) Type: Fix
  | `41512 <https:////gerrit.fd.io/r/c/vpp/+/41512>`_ [veC 130]: Flowprobe: Fix etherType Type:Fix
  | `41509 <https:////gerrit.fd.io/r/c/vpp/+/41509>`_ [veC 130]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field and modify test
  | `41510 <https:////gerrit.fd.io/r/c/vpp/+/41510>`_ [veC 130]: flowprobe:   Fix the problem with Network Byte Order for Ethernet type and modify the test Type: fix
  | `41507 <https:////gerrit.fd.io/r/c/vpp/+/41507>`_ [veC 130]: flowprobe: Fix the problem with Network Byte Order for Ethernet type field
  | `41506 <https:////gerrit.fd.io/r/c/vpp/+/41506>`_ [veC 130]: docs: Fix the problem with Network Byte Order for Ethernet type field Type:fix
  | `41505 <https:////gerrit.fd.io/r/c/vpp/+/41505>`_ [veC 130]: docs: Fix the problem with Network Byte Order for Ethernet type field Type: fix

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `41678 <https:////gerrit.fd.io/r/c/vpp/+/41678>`_ [VeC 88]: linux-cp: do ip6-ll cleanup on interface removal

**Varun Rapelly** <vrapelly@marvell.com>:

  | `42070 <https:////gerrit.fd.io/r/c/vpp/+/42070>`_ [VEc 0]: tls:async event handling enhancement
  | `42119 <https:////gerrit.fd.io/r/c/vpp/+/42119>`_ [VEc 0]: tls: added dpdk engine support

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `41979 <https:////gerrit.fd.io/r/c/vpp/+/41979>`_ [vEC 3]: build: support 128B/64B cache-line size in Arm image

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 137]: ip6-nd: simplify API to directly set options

**Vladimir Smirnov** <civil.over@gmail.com>:

  | `42126 <https:////gerrit.fd.io/r/c/vpp/+/42126>`_ [vEC 1]: dpdk: update rdma-core to 55.0
  | `42090 <https:////gerrit.fd.io/r/c/vpp/+/42090>`_ [VEc 2]: build: Add VLIB_MAX_NELTS configure option
  | `42089 <https:////gerrit.fd.io/r/c/vpp/+/42089>`_ [vEc 2]: fix: fail in runtime if workers > nelts

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 36]: stats: add sw interface tags to statseg
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 44]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 44]: fib: fix udp encap mp-safe ops and id validation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 47]: vlib: mark cli quit command as mp_safe
  | `41657 <https:////gerrit.fd.io/r/c/vpp/+/41657>`_ [VeC 91]: nat: make nat44-ed cli summary less verbose
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 95]: nat: add nat44-ed session filtering by fib table
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 102]: nat: add nat44-ed ipfix dst address and port logging
  | `41659 <https:////gerrit.fd.io/r/c/vpp/+/41659>`_ [VeC 102]: nat: make nat44-ed api dumps & cli show mp-safe
  | `41658 <https:////gerrit.fd.io/r/c/vpp/+/41658>`_ [VeC 102]: nat: fix nat44-ed per-vrf session limit and tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 102]: mpls: fix crashes on mpls tunnel create/delete
  | `41656 <https:////gerrit.fd.io/r/c/vpp/+/41656>`_ [VeC 102]: nat: pass nat44-ed packets with ttl=1 on outside interfaces
  | `41615 <https:////gerrit.fd.io/r/c/vpp/+/41615>`_ [VeC 102]: mpls: clang-format mpls-tunnel for upcoming changes
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 102]: nat: stick nat44-ed to use configured outside-fib
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 102]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 102]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 102]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 102]: stats: add interface link speed to statseg

**Vratko Polak** <vrpolak@cisco.com>:

  | `41558 <https:////gerrit.fd.io/r/c/vpp/+/41558>`_ [VeC 102]: avf: mark api as deprecated
  | `41557 <https:////gerrit.fd.io/r/c/vpp/+/41557>`_ [VeC 108]: dev: declare api as production
  | `41552 <https:////gerrit.fd.io/r/c/vpp/+/41552>`_ [VeC 122]: avf: interprocess reply via pointer

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `41594 <https:////gerrit.fd.io/r/c/vpp/+/41594>`_ [Vec 106]: http: fix timer pool assert crash due to timer freed when timeout in main thread

**lei feng** <1579628578@qq.com>:

  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [vEC 0]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [VEc 1]: docs: Python apis examples
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [VEc 1]: dns: dns request ip6 fix
  | `42058 <https:////gerrit.fd.io/r/c/vpp/+/42058>`_ [vEC 1]: docs: Python apis examples
  | `42057 <https:////gerrit.fd.io/r/c/vpp/+/42057>`_ [vEC 20]: docs: Python apis examples
  | `42056 <https:////gerrit.fd.io/r/c/vpp/+/42056>`_ [vEC 20]: docs: Python apis examples
  | `42055 <https:////gerrit.fd.io/r/c/vpp/+/42055>`_ [vEC 20]: docs: Python apis examples
  | `41866 <https:////gerrit.fd.io/r/c/vpp/+/41866>`_ [VEc 23]: dns: did't shall resolve before enable
  | `42040 <https:////gerrit.fd.io/r/c/vpp/+/42040>`_ [vEC 23]: docs: add examples for VXLAN tunnel
  | `42039 <https:////gerrit.fd.io/r/c/vpp/+/42039>`_ [vEC 23]: docs: add examples for GRE teb tunnel
  | `41863 <https:////gerrit.fd.io/r/c/vpp/+/41863>`_ [VeC 50]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41860 <https:////gerrit.fd.io/r/c/vpp/+/41860>`_ [veC 50]: build: ubuntu24.04 llvm[18] lack of the header and library of asan
  | `41855 <https:////gerrit.fd.io/r/c/vpp/+/41855>`_ [VeC 51]: svm: fix check bitmap logic error
  | `41854 <https:////gerrit.fd.io/r/c/vpp/+/41854>`_ [veC 51]: svm: fix check bitmap logic error
  | `41852 <https:////gerrit.fd.io/r/c/vpp/+/41852>`_ [veC 51]: svm: fix check bitmap logic error
  | `41851 <https:////gerrit.fd.io/r/c/vpp/+/41851>`_ [veC 51]: svm: fix check bitmap logic error
  | `41850 <https:////gerrit.fd.io/r/c/vpp/+/41850>`_ [veC 51]: Makefile: support anolis8 operation for vpp
  | `41848 <https:////gerrit.fd.io/r/c/vpp/+/41848>`_ [veC 51]: Makefile: support anolis8 operation for vpp Type: improvement

**shaohui jin** <jinshaohui789@163.com>:

  | `41652 <https:////gerrit.fd.io/r/c/vpp/+/41652>`_ [veC 50]: dhcp:fix dhcp server no support Option 82,unable to assign an IP address.
  | `41653 <https:////gerrit.fd.io/r/c/vpp/+/41653>`_ [veC 50]: dhcp:dhcp request packets always use the first server address.

**sonsumin** <itoodo12@gmail.com>:

  | `41681 <https:////gerrit.fd.io/r/c/vpp/+/41681>`_ [VeC 75]: nat: refactor argument order for nat44-ed static mapping
  | `41667 <https:////gerrit.fd.io/r/c/vpp/+/41667>`_ [veC 100]: refactor(nat44): change argument order and parsing format for static mapping

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
authors          95
maintainers      35
committers       0
abandoned        0
================ ===

