
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2024-07-30, 02:10:48
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

api: **Dave Barach** <vpp@barachs.net>
  | `41257 <https:////gerrit.fd.io/r/c/vpp/+/41257>`_ [VECr 17]: api: support api clients with real-time scheduling

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `41252 <https:////gerrit.fd.io/r/c/vpp/+/41252>`_ [VECr 11]: buffers: support disabling allocation per numa domain

build: **Damjan Marion** <damarion@cisco.com>
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 6]: build: add SHA256 checksums for external downloaded dependencies
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 17]: vppinfra: add ARM neoverse-v2 support

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 5]: dhcp: fix buffer length after adding new option

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 5]: vlib: fix seed parse error
  | `41252 <https:////gerrit.fd.io/r/c/vpp/+/41252>`_ [VECr 11]: buffers: support disabling allocation per numa domain

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 11]: vxlan: move vxlan-gpe to a plugin

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 21]: ip: added CLI command to set ip6 reassembly params

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 11]: vxlan: move vxlan-gpe to a plugin

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 11]: vxlan: move vxlan-gpe to a plugin

pg: **Dave Barach** <vpp@barachs.net>
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VECr 11]: pg: fix offload offsets for ip4/6-input

tcp: **Florin Coras** <fcoras@cisco.com>
  | `41310 <https:////gerrit.fd.io/r/c/vpp/+/41310>`_ [VECr 0]: tcp: fix typo in show tcp config CLI command

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `41272 <https:////gerrit.fd.io/r/c/vpp/+/41272>`_ [VECr 5]: dhcp: fix buffer length after adding new option

vapi: **Ole Troan** <ot@cisco.com>
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VECr 5]: vapi: remove plugin dependency from tests

vat2: **Ole Troan** <ot@cisco.com>
  | `41277 <https:////gerrit.fd.io/r/c/vpp/+/41277>`_ [VECr 11]: vat2: fix -p in vat2 help text

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 5]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 5]: vlib: fix seed parse error
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 17]: vlib: improve core pinning

vpp: **Dave Barach** <vpp@barachs.net>
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 17]: vlib: improve core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `41259 <https:////gerrit.fd.io/r/c/vpp/+/41259>`_ [VECr 17]: vppinfra: add ARM neoverse-v2 support
  | `41094 <https:////gerrit.fd.io/r/c/vpp/+/41094>`_ [VECr 17]: vlib: improve core pinning

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [Vec 33]: bonding: make link state depend on active members

**Alok Mishra** <almishra@marvell.com>:

  | `40823 <https:////gerrit.fd.io/r/c/vpp/+/40823>`_ [VEc 13]: octeon: add support for max_rx_frame_size update

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 158]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 4]: pvti: Packet Vector Tunnel Interface
  | `41203 <https:////gerrit.fd.io/r/c/vpp/+/41203>`_ [vEC 4]: acl: use ip4_preflen_to_mask instead of artisanal function

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 90]: docs: Restore and update nat section of progressive tutorial

**Benoît Ganne** <bganne@cisco.com>:

  | `41307 <https:////gerrit.fd.io/r/c/vpp/+/41307>`_ [vEC 0]: tests: fix scapy 2.4.5 ipsec patch for ESN

**Dau Do** <daudo@yahoo.com>:

  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VeC 40]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [Vec 44]: hash: Add cli to enable soft interface hashing based on esp
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VeC 47]: ipsec: Add api to show the number of SAs distributed over the workers
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [veC 48]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [veC 49]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 93]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `41288 <https:////gerrit.fd.io/r/c/vpp/+/41288>`_ [vEC 0]: tests: update scapy to version 2.4.5

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 77]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 46]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 98]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 109]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 126]: vlib: add config for elog tracing

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 173]: tcp: Start persist timer if snd_wnd is zero and no probing

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 155]: session: make local port allocator fib aware

**Guillaume Solignac** <gsoligna@cisco.com>:

  | `41160 <https:////gerrit.fd.io/r/c/vpp/+/41160>`_ [VeC 40]: vppinfra: cleaner way of getting libdl in CMake

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 138]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VeC 49]: vlib: require main core with 'skip-cores' attribute
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VeC 76]: vlib: fix automatic core pinning
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 88]: docs: update core-pinning configuration
  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [Vec 105]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 130]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [veC 35]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VeC 35]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VeC 35]: ip: add ip6 shallow reassembly output feature
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 132]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 96]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 20]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 20]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 88]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 98]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [Vec 39]: vapi: only wait if queue is empty

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 68]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 76]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [Vec 49]: octeon: fix oct_free() and free allocated memory

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 133]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 118]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 159]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 162]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 130]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 138]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 119]: octeon: add crypto framework

**Ole Troan** <otroan@employees.org>:

  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VeC 34]: dpdk: xstats as symlinks

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 118]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VeC 47]: ipsec: add SA validity check fetching IPsec SA
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 76]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 83]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 60]: ikev2: handoff packets
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 175]: tap: add virtio polling option

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 60]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 60]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [Vec 34]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 101]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VeC 37]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 37]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 38]: fib: fix invalid udp encap id cases
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 67]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 111]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 116]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 116]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 120]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 120]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 120]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 120]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 120]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 149]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 149]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 111]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 76]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 105]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 129]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 138]: vppinfra: fix memory overrun in mhash_set_mem

**steven luong** <sluong@cisco.com>:

  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 172]: virtio: RSS support

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
maintainers      14
committers       0
abandoned        0
================ ===

