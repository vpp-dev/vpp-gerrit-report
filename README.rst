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
generated on Tuesday 2026-04-14, 04:17:18
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

  | `45516 <https:////gerrit.fd.io/r/c/vpp/+/45516>`_ [VECR 0]: quic: skip quic_update_fifo_size if not attached

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45379 <https:////gerrit.fd.io/r/c/vpp/+/45379>`_ [VECr 2]: af_xdp: add mac-reuse option
  | `45501 <https:////gerrit.fd.io/r/c/vpp/+/45501>`_ [VECr 3]: af_xdp: cleanup fds and netns on error
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 13]: af_xdp: add support for multi-buffer

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VECr 17]: bpf_trace_filter: fix bpf_expr memory leak on error path

bufmon: **Benoît Ganne** <bganne@cisco.com>
  | `45110 <https:////gerrit.fd.io/r/c/vpp/+/45110>`_ [VECr 6]: bufmon: unregister old callbacks before re-registering on enable

build: **Damjan Marion** <damarion@cisco.com>
  | `45513 <https:////gerrit.fd.io/r/c/vpp/+/45513>`_ [VECr 0]: dpdk: bump to DPDK 26.03 and rdma-core 62.0
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 13]: af_xdp: add support for multi-buffer

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 13]: l2: fix missing CDP hello packets on BVI interface

classify: **Dave Barach** <vpp@barachs.net>
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 3]: tm: add 'mark_flow' action for traffic management

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 0]: crypto: add op tracing capability

ct6: **Dave Barach** <vpp@barachs.net>
  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VECr 10]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VECr 10]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

dev: **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45358 <https:////gerrit.fd.io/r/c/vpp/+/45358>`_ [VECr 9]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 10]: misc: patch to test CI infra
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45497 <https:////gerrit.fd.io/r/c/vpp/+/45497>`_ [VECr 3]: dpdk: fix async flow offload counters
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 13]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 21]: ethernet: implement outer_vlan_id_any sub-interface matching

fib: **Neale Ranns** <neale@graphiant.com>
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 26]: fib: honor unnumbered RX interface in MFIB RPF check

flow: **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Adrian Villin** <avillin@cisco.com>
  | `45499 <https:////gerrit.fd.io/r/c/vpp/+/45499>`_ [VECr 0]: http: draft-ietf-masque-connect-udp-03 support
  | `45419 <https:////gerrit.fd.io/r/c/vpp/+/45419>`_ [VECr 6]: hs-test: Add EchoBuiltinHttp2ConnectUdpBackpressureTest and EchoBuiltinHttp2ConnectUdpBackpressureMWTest

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `45499 <https:////gerrit.fd.io/r/c/vpp/+/45499>`_ [VECr 0]: http: draft-ietf-masque-connect-udp-03 support

http: **Florin Coras** <fcoras@cisco.com>
  | `45499 <https:////gerrit.fd.io/r/c/vpp/+/45499>`_ [VECr 0]: http: draft-ietf-masque-connect-udp-03 support

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45452 <https:////gerrit.fd.io/r/c/vpp/+/45452>`_ [VECr 5]: iavf: fix 16 queue pair startup
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 5]: iavf: fix native TSO datapath for 1500-byte frames

interface: **Dave Barach** <vpp@barachs.net>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 3]: interface: add global default rx-mode setting
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 21]: ethernet: implement outer_vlan_id_any sub-interface matching

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 18]: tests: reduce sleep interval in ip-neighbor age test
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 24]: ip-neighbor: suppress off-link adj-fib on addressed interfaces

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 1]: ip6-nd: support RDNSS option in IPv6 RA
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 3]: tm: add 'mark_flow' action for traffic management
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 3]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 3]: ip: fix reassembly bugs and add tests
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 5]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45472 <https:////gerrit.fd.io/r/c/vpp/+/45472>`_ [VECr 5]: ip: add multicast SVR
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VECr 13]: ip6: fix show ip6-ll cli if selector
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 26]: ip6-nd: add per-interface control for inbound RA acceptance

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VECr 0]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 1]: ip6-nd: support RDNSS option in IPv6 RA
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 5]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 5]: ip6-nd: add nd-proxy all dst
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 5]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 26]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 26]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 26]: ip6-nd: add per-interface control for inbound RA acceptance

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 0]: crypto: add op tracing capability

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 13]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 21]: ethernet: implement outer_vlan_id_any sub-interface matching

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 3]: lb: API bugfix
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 5]: lb: Add punt feature to per-port VIPs

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VECr 25]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 0]: crypto: add op tracing capability
  | `45490 <https:////gerrit.fd.io/r/c/vpp/+/45490>`_ [VECr 3]: gre: fix tunnel dump issues
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 5]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 13]: af_xdp: add support for multi-buffer
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VECr 14]: build rpm-packaging: make vpp rpm package for kylinV11
  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VECr 26]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VECr 26]: stats: don't leak regcomp() allocated memory

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [VECr 3]: papi: improve performance on set_errors

pg: **Dave Barach** <vpp@barachs.net>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45502 <https:////gerrit.fd.io/r/c/vpp/+/45502>`_ [VECr 2]: ping: set LOCALLY_ORIGINATED flag on cli-initiated ping packets.

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 27]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 27]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 27]: policer: reject deletion of policer used by punt policing

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 13]: sfdp: guard packet bit shifts in lookup

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45517 <https:////gerrit.fd.io/r/c/vpp/+/45517>`_ [VECr 0]: snort: remove remaining snort_get_main() refs
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VECr 6]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VECr 26]: snort: fix inject/finalize ordering race in deq node

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 3]: interface: add global default rx-mode setting
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45414 <https:////gerrit.fd.io/r/c/vpp/+/45414>`_ [VECr 0]: tests: avoid spurious read timeouts
  | `45454 <https:////gerrit.fd.io/r/c/vpp/+/45454>`_ [VECr 0]: tests: eliminate capture file busy-wait
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 1]: ip6-nd: support RDNSS option in IPv6 RA
  | `45490 <https:////gerrit.fd.io/r/c/vpp/+/45490>`_ [VECr 3]: gre: fix tunnel dump issues
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 3]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 3]: ip: fix reassembly bugs and add tests
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 3]: lb: API bugfix
  | `45467 <https:////gerrit.fd.io/r/c/vpp/+/45467>`_ [VECr 5]: tests: proper return value checking for 'modern' 'service' APIs
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 5]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 5]: ip6-nd: add nd-proxy all dst
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 5]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45473 <https:////gerrit.fd.io/r/c/vpp/+/45473>`_ [VECr 5]: tests: add type annotations
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 5]: lb: Add punt feature to per-port VIPs
  | `45475 <https:////gerrit.fd.io/r/c/vpp/+/45475>`_ [VECr 5]: tests: write failed_tests file to test tmp directory
  | `45477 <https:////gerrit.fd.io/r/c/vpp/+/45477>`_ [VECr 5]: tests: add default values for filter/skip-filter
  | `45476 <https:////gerrit.fd.io/r/c/vpp/+/45476>`_ [VECr 5]: tests: add register_exclusive() function
  | `45474 <https:////gerrit.fd.io/r/c/vpp/+/45474>`_ [VECr 5]: tests: add assert_counter_in_range()
  | `45468 <https:////gerrit.fd.io/r/c/vpp/+/45468>`_ [VECr 5]: tests: customizable IP schemes for remote hosts
  | `45466 <https:////gerrit.fd.io/r/c/vpp/+/45466>`_ [VECr 5]: tests: support renaming interfaces
  | `45455 <https:////gerrit.fd.io/r/c/vpp/+/45455>`_ [VECr 5]: tests: move debug ppp() packet formatting outside of test framework
  | `45420 <https:////gerrit.fd.io/r/c/vpp/+/45420>`_ [VECr 6]: tests: replace set_errors_str with "show error" CLI
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 13]: af_xdp: add support for multi-buffer
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 18]: tests: reduce sleep interval in ip-neighbor age test
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 21]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VECr 24]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 26]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 26]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VECr 26]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VECr 26]: ip6-nd: add per-interface control for inbound RA acceptance
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VECr 27]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VECr 27]: policer: fix unchecked policer removal
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 27]: policer: reject deletion of policer used by punt policing

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal

vapi: **Ole Troan** <ot@cisco.com>
  | `45393 <https:////gerrit.fd.io/r/c/vpp/+/45393>`_ [VECr 10]: vapi: fix union generation for C++

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 10]: misc: patch to test CI infra

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 3]: interface: add global default rx-mode setting
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 21]: gso: implement IPv6 extension header traversal

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45469 <https:////gerrit.fd.io/r/c/vpp/+/45469>`_ [VECr 5]: vlib: avoid warning by using correct node fn declaration
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VECr 13]: stats: show raw value in show stat segment

vpp: **Dave Barach** <vpp@barachs.net>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44546 <https:////gerrit.fd.io/r/c/vpp/+/44546>`_ [VECr 7]: vppapigen: error on use of array with unspecified length
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 25]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `44519 <https:////gerrit.fd.io/r/c/vpp/+/44519>`_ [VECr 0]: vppinfra: format_hexdump_trunc, unformat_bitrate, format_backtrace
  | `45471 <https:////gerrit.fd.io/r/c/vpp/+/45471>`_ [VECr 5]: vppinfra: add const-qualifier to avoid warning(s)
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 5]: vppinfra: add cast to prevent warning

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 48]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 48]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 13]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VeC 35]: octeon: implement hardware traffic management

**Andrew Mason** <mason12@gmail.com>:

  | `44082 <https:////gerrit.fd.io/r/c/vpp/+/44082>`_ [vec 158]: linux-cp: Punt for ISIS traffic over linux-cp plugin
  | `44085 <https:////gerrit.fd.io/r/c/vpp/+/44085>`_ [veC 158]: linux-cp: Punt for ISIS traffic over linux-cp plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 82]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 110]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features
  | `43916 <https:////gerrit.fd.io/r/c/vpp/+/43916>`_ [Vec 171]: vlib: print non-parked threads on vlib_worker_thread_barrier_sync_int
  | `43915 <https:////gerrit.fd.io/r/c/vpp/+/43915>`_ [Vec 174]: vnet: Initialize the classify arrays to ~0

**Aritra Basu** <aritrbas@cisco.com>:

  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 31]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 110]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `45203 <https:////gerrit.fd.io/r/c/vpp/+/45203>`_ [VeC 32]: policer: avoid redundant l2_overhead array access on TX path
  | `39443 <https:////gerrit.fd.io/r/c/vpp/+/39443>`_ [veC 45]: vnet: reorder vnet_buffer2 metadata
  | `44962 <https:////gerrit.fd.io/r/c/vpp/+/44962>`_ [VeC 54]: pppoe: initialize sw_if_index before early goto

**C.J. Collier**:

  | `1948 <https:////gerrit.fd.io/r/c/vpp/+/1948>`_ [veC 172]: DO NOT MERGE - testing new build image

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 10]: ikev2: add Curve25519 and Curve448 DH groups
  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [veC 152]: ipsec: precompute payload and payload length adjustments
  | `44081 <https:////gerrit.fd.io/r/c/vpp/+/44081>`_ [veC 157]: ipsec: fill op templates with lengths and tag sizes

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [vEC 28]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [vEC 28]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44754 <https:////gerrit.fd.io/r/c/vpp/+/44754>`_ [VEc 10]: tracepath: introduce tracepath plugin
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 49]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 96]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VEc 6]: cnat: support encapsulation and session cleanup on backend deletion

**Ivan Ivanets** <iivanets@cisco.com>:

  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 47]: crypto: unify per-thread key_data allocation

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `45381 <https:////gerrit.fd.io/r/c/vpp/+/45381>`_ [vEc 3]: linux-cp: add more namespace-based tests

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 66]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 66]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 66]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 66]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `44559 <https:////gerrit.fd.io/r/c/vpp/+/44559>`_ [Vec 41]: af_xdp: ensure null termination in format() string outputs
  | `44584 <https:////gerrit.fd.io/r/c/vpp/+/44584>`_ [veC 81]: tests: fix tag_fixme_debian12 to tag_fixme_debian11
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 93]: virtio: add native plugin L2 xconnect test with QEMU

**Jiajun Liang** <3138947285@qq.com>:

  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VEc 0]: pppoe: add PPPoE client and pppox

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 68]: vppapigen: fix json build error

**Klement Sekera** <ksekera@netgate.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [vEc 0]: tests: add send_and_expect_multi

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45312 <https:////gerrit.fd.io/r/c/vpp/+/45312>`_ [vEc 12]: sfdp: fix timer macro usage
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [vEC 27]: policer: reject delete of policer still applied to interface

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 2]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 124]: vcl: LDP default to regular option
  | `43874 <https:////gerrit.fd.io/r/c/vpp/+/43874>`_ [Vec 178]: unittest: add sfdp testing and unity framework

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 32]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 55]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 59]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 94]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 72]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 49]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 54]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 4]: sfdp: offload lookup via vnet flow mark

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 73]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 75]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [vEC 1]: lb: Allow setting weight on AS

**Ryosuke Nakayama** <ryosuke_666@icloud.com>:

  | `45117 <https:////gerrit.fd.io/r/c/vpp/+/45117>`_ [veC 38]: atlantic: remove unused pkt_n_desc variable
  | `45116 <https:////gerrit.fd.io/r/c/vpp/+/45116>`_ [VeC 38]: snort: fix maybe-uninitialized warning with GCC 15
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VeC 38]: build: add Fedora 43 build compatibility
  | `45113 <https:////gerrit.fd.io/r/c/vpp/+/45113>`_ [VeC 38]: ipsec: fix implicit enum cast warnings with GCC 15
  | `45115 <https:////gerrit.fd.io/r/c/vpp/+/45115>`_ [VeC 38]: sasc: fix maybe-uninitialized warning with GCC 15
  | `45114 <https:////gerrit.fd.io/r/c/vpp/+/45114>`_ [VeC 38]: dpdk: fix maybe-uninitialized warning with GCC 15
  | `45112 <https:////gerrit.fd.io/r/c/vpp/+/45112>`_ [VeC 38]: build: add AlmaLinux support to install-dep target

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 13]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 108]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 116]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 131]: fib: dump by src not only contributing routes

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VEc 19]: tm: add tm framework for hw traffic management

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VeC 33]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [vEC 13]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 94]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 94]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 94]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 94]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 94]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 95]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 95]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 95]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 95]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 95]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 95]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 95]: vlib: mark cli quit command as mp_safe

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 110]: ip-neighbor: ARP/NA per-interface counter improvements

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 62]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [VEc 13]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [VEc 13]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 67]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 119]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 6]: cnat: add scope_id to session key

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [vEC 13]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 107]: lb: fix incorrect byte order conversion for vip port display

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [veC 152]: ipsec: prevent use of deleted keys in async mode

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [veC 40]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 95]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 77]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 77]: l2: fix null pointer access in l2-efp-filter

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Maxime Peim** <maxime.peim@gmail.com>:

  | `43515 <https:////gerrit.fd.io/r/c/vpp/+/43515>`_ [A 180]: ping: introduce traceroute tool

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
authors          93
maintainers      75
committers       1
abandoned        1
================ ===

