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
generated on Tuesday 2024-07-09, 02:10:18
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

  | `41237 <https:////gerrit.fd.io/r/c/vpp/+/41237>`_ [VECR 0]: prom: concurrent connections fix
  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECR 26]: ipsec: add SA validity check fetching IPsec SA

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

build: **Damjan Marion** <damarion@cisco.com>
  | `41166 <https:////gerrit.fd.io/r/c/vpp/+/41166>`_ [VECr 5]: build: Fix crossbuilding definitions
  | `40971 <https:////gerrit.fd.io/r/c/vpp/+/40971>`_ [VECr 20]: build: add SHA256 checksums for external downloaded dependencies

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 13]: vlib: fix seed parse error

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `41168 <https:////gerrit.fd.io/r/c/vpp/+/41168>`_ [VECr 13]: dpdk: xstats as symlinks

fib: **Neale Ranns** <neale@graphiant.com>
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 4]: fib: improve ipv6 fib scaling
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 5]: fib: log an error when destroying non-empty tables
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 5]: fib: fix covered_inherit_add
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VECr 16]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 16]: fib: fix udp encap mp-safe ops and id validation

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app
  | `41176 <https:////gerrit.fd.io/r/c/vpp/+/41176>`_ [VECr 7]: hs-test: Add CPU pinning test suite

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app

http: **Florin Coras** <fcoras@cisco.com>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 5]: fib: make mfib optional

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 17]: vxlan: move vxlan-gpe to a plugin

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 0]: ip: added CLI command to set ip6 reassembly params
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 4]: fib: improve ipv6 fib scaling
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 5]: ip6: fix icmp error on check fail
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 5]: fib: make mfib optional
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 14]: ip: fix ip4 shallow reassembly output feature handoff
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 14]: ip: add ip6 shallow reassembly output feature

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `41138 <https:////gerrit.fd.io/r/c/vpp/+/41138>`_ [VECr 19]: ipsec: add binapi to set/get the SA's seq/replay_window
  | `41103 <https:////gerrit.fd.io/r/c/vpp/+/41103>`_ [VECr 26]: ipsec: Add api to show the number of SAs distributed over the workers

mactime: **Dave Barach** <vpp@barachs.net>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 14]: ip: fix ip4 shallow reassembly output feature handoff
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 17]: vxlan: move vxlan-gpe to a plugin

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `40898 <https:////gerrit.fd.io/r/c/vpp/+/40898>`_ [VECr 17]: vxlan: move vxlan-gpe to a plugin

pg: **Dave Barach** <vpp@barachs.net>
  | `41246 <https:////gerrit.fd.io/r/c/vpp/+/41246>`_ [VECr 3]: pg: fix offload offsets for ip4/6-input

prom: **Florin Coras** <fcoras@cisco.com>
  | `41165 <https:////gerrit.fd.io/r/c/vpp/+/41165>`_ [VECr 0]: http: return more than data from server app

session: **Florin Coras** <fcoras@cisco.com>
  | `41249 <https:////gerrit.fd.io/r/c/vpp/+/41249>`_ [VECr 0]: session: add api to program rx io evts
  | `41239 <https:////gerrit.fd.io/r/c/vpp/+/41239>`_ [VECr 9]: session: crash in session_rule_add_del if session is not enable

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 5]: fib: make mfib optional
  | `41174 <https:////gerrit.fd.io/r/c/vpp/+/41174>`_ [VECr 16]: fib: fix fib entry tracking crash on table remove
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 16]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 17]: fib: fix invalid udp encap id cases

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 16]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 5]: fib: make mfib optional
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 5]: fib: fix covered_inherit_add
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 17]: fib: fix invalid udp encap id cases

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40890 <https:////gerrit.fd.io/r/c/vpp/+/40890>`_ [VECr 13]: vlib: fix seed parse error
  | `41099 <https:////gerrit.fd.io/r/c/vpp/+/41099>`_ [VECr 28]: vlib: require main core with 'skip-cores' attribute

vppapigen: **Ole Troan** <otroan@employees.org>
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VECr 25]: vppapigen: fix enum format function

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40994 <https:////gerrit.fd.io/r/c/vpp/+/40994>`_ [VECr 11]: vppinfra: fix huge page alloc error on 5.19+ kernel
  | `41160 <https:////gerrit.fd.io/r/c/vpp/+/41160>`_ [VECr 19]: vppinfra: cleaner way of getting libdl in CMake

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Chernavin** <achernavin@netgate.com>:

  | `41161 <https:////gerrit.fd.io/r/c/vpp/+/41161>`_ [VEc 12]: bonding: make link state depend on active members

**Alok Mishra** <almishra@marvell.com>:

  | `41192 <https:////gerrit.fd.io/r/c/vpp/+/41192>`_ [vEC 9]: octeon: fix link down issue
  | `40823 <https:////gerrit.fd.io/r/c/vpp/+/40823>`_ [VEc 26]: octeon: add support for max_rx_frame_size update

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 137]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 0]: pvti: Packet Vector Tunnel Interface

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 69]: docs: Restore and update nat section of progressive tutorial

**Dau Do** <daudo@yahoo.com>:

  | `41107 <https:////gerrit.fd.io/r/c/vpp/+/41107>`_ [VEc 23]: hash: Add cli to enable soft interface hashing based on esp
  | `41104 <https:////gerrit.fd.io/r/c/vpp/+/41104>`_ [vEC 27]: ipsec: Add option to configure the handoff worker queue size
  | `41100 <https:////gerrit.fd.io/r/c/vpp/+/41100>`_ [vEC 28]: ipsec: Add option to configure the handoff worker queue size
  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [veC 72]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [vEC 10]: misc: patch to test CI infra changes

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VeC 56]: ikev2: multiple ts per profile

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VeC 58]: tests: skip more excluded plugin tests
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 77]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VeC 88]: fib: fix mpls tunnel restacking
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 105]: vlib: add config for elog tracing

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 152]: tcp: Start persist timer if snd_wnd is zero and no probing

**Fan Zhang** <fanzhang.oss@gmail.com>:

  | `40854 <https:////gerrit.fd.io/r/c/vpp/+/40854>`_ [VeC 53]: wireguard: fix dereference null return value
  | `40841 <https:////gerrit.fd.io/r/c/vpp/+/40841>`_ [VeC 55]: wireguard: fix uninitialized pointer read

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 134]: session: make local port allocator fib aware

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 117]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VeC 55]: vlib: fix automatic core pinning
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VeC 67]: docs: update core-pinning configuration
  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [Vec 84]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 109]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [vEC 14]: ip: add extended shallow reassembly
  | `40836 <https:////gerrit.fd.io/r/c/vpp/+/40836>`_ [VeC 42]: vnet: print Success for API errno 0 instead of UNKNOWN
  | `40920 <https:////gerrit.fd.io/r/c/vpp/+/40920>`_ [VeC 46]: tests: more options for decoding pcaps
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 111]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 75]: linux-cp: Add VRF synchronization

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 18]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 18]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [veC 67]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [Vec 77]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Matthew Smith** <mgsmith@netgate.com>:

  | `40983 <https:////gerrit.fd.io/r/c/vpp/+/40983>`_ [VEc 18]: vapi: only wait if queue is empty

**Matus Fabian** <matfabia@cisco.com>:

  | `41193 <https:////gerrit.fd.io/r/c/vpp/+/41193>`_ [VEc 0]: http: state machine fix

**Maxime Peim** <mpeim@cisco.com>:

  | `40918 <https:////gerrit.fd.io/r/c/vpp/+/40918>`_ [veC 47]: classify: add name to classify heap
  | `40888 <https:////gerrit.fd.io/r/c/vpp/+/40888>`_ [VeC 55]: pg: allow node unformat after hex data

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `41093 <https:////gerrit.fd.io/r/c/vpp/+/41093>`_ [VEc 28]: octeon: fix oct_free() and free allocated memory

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 112]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 97]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 138]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 141]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 109]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 117]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 98]: octeon: add crypto framework

**Niyaz Murshed** <niyaz.murshed@arm.com>:

  | `41182 <https:////gerrit.fd.io/r/c/vpp/+/41182>`_ [VEc 5]: vppinfra: Add macro for targeted prefetching

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 97]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VeC 55]: vppinfra: fix dpdk compilation
  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vec 62]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 39]: ikev2: handoff packets
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VeC 58]: vapi: remove plugin dependency from tests
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 154]: tap: add virtio polling option

**Todd Hsiao** <thsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 39]: ip: Full reassembly and fragmentation enhancement
  | `40992 <https:////gerrit.fd.io/r/c/vpp/+/40992>`_ [veC 39]: ip: add IPV6_FRAGMENTATION to extension_hdr_type

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 13]: ip6-nd: simplify API to directly set options

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VeC 80]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 46]: vlib: mark cli quit command as mp_safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 90]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 95]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 95]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 99]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 99]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 99]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 99]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 99]: mpls: fix crashes on mpls tunnel create/delete
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 128]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 128]: nat: stick nat44-ed to use configured outside-fib

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VEc 17]: vppinfra: fix cpu freq init error if cpu support aperfmperf
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 90]: ipsec: cli: 'set interface ipsec spd' support delete

**Zephyr Pellerin** <zpelleri@cisco.com>:

  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VeC 55]: build: don't embed directives within macro arguments

**jinhui li** <lijh_7@chinatelecom.cn>:

  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VeC 84]: ip: discard old trace flag after copy

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 108]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 117]: vppinfra: fix memory overrun in mhash_set_mem

**steven luong** <sluong@cisco.com>:

  | `41248 <https:////gerrit.fd.io/r/c/vpp/+/41248>`_ [vEC 0]: session: application namespace may reference a deleted vrf table
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 151]: virtio: RSS support

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
authors          76
maintainers      27
committers       2
abandoned        0
================ ===

