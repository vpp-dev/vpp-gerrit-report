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
generated on Tuesday 2026-04-21, 04:19:46
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

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45379 <https:////gerrit.fd.io/r/c/vpp/+/45379>`_ [VECr 9]: af_xdp: add mac-reuse option
  | `45501 <https:////gerrit.fd.io/r/c/vpp/+/45501>`_ [VECr 10]: af_xdp: cleanup fds and netns on error
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer

bpf_trace_filter: **Mohammed Hawari** <mohammed@hawari.fr>
  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VECr 24]: bpf_trace_filter: fix bpf_expr memory leak on error path

build: **Damjan Marion** <damarion@cisco.com>
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer

cdp: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 20]: l2: fix missing CDP hello packets on BVI interface

classify: **Dave Barach** <vpp@barachs.net>
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 10]: tm: add 'mark_flow' action for traffic management

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 7]: crypto: add op tracing capability

ct6: **Dave Barach** <vpp@barachs.net>
  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VECr 17]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VECr 17]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

dev: **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45358 <https:////gerrit.fd.io/r/c/vpp/+/45358>`_ [VECr 0]: dhcp: export DHCPv6 runtime state for PPPoE observability
  | `45569 <https:////gerrit.fd.io/r/c/vpp/+/45569>`_ [VECr 1]: dhcp: export DHCPv6 runtime state for PPPoE observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 24]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core
  | `45562 <https:////gerrit.fd.io/r/c/vpp/+/45562>`_ [VECr 3]: dpdk: add trace-bufsz startup.conf option
  | `45561 <https:////gerrit.fd.io/r/c/vpp/+/45561>`_ [VECr 3]: dpdk: add 'dpdk trace save' CLI command
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 20]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 28]: ethernet: implement outer_vlan_id_any sub-interface matching

fib: **Neale Ranns** <neale@graphiant.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core

flow: **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45556 <https:////gerrit.fd.io/r/c/vpp/+/45556>`_ [VECr 0]: quic: handle half-open cleanup
  | `45576 <https:////gerrit.fd.io/r/c/vpp/+/45576>`_ [VECr 0]: hs-test: Http2TcpClientCloseDuringHandshake fix

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45452 <https:////gerrit.fd.io/r/c/vpp/+/45452>`_ [VECr 12]: iavf: fix 16 queue pair startup
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 12]: iavf: fix native TSO datapath for 1500-byte frames

interface: **Dave Barach** <vpp@barachs.net>
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 0]: interface: add global default rx-mode setting
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 3]: interface: enable IPv6 link state on unnumbered interfaces
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 28]: ethernet: implement outer_vlan_id_any sub-interface matching

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 25]: tests: reduce sleep interval in ip-neighbor age test

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 8]: ip6-nd: support RDNSS option in IPv6 RA
  | `42958 <https:////gerrit.fd.io/r/c/vpp/+/42958>`_ [VECr 10]: tm: add 'mark_flow' action for traffic management
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 10]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 10]: ip: fix reassembly bugs and add tests
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 12]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45472 <https:////gerrit.fd.io/r/c/vpp/+/45472>`_ [VECr 12]: ip: add multicast SVR
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VECr 20]: ip6: fix show ip6-ll cli if selector
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 3]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VECr 7]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 8]: ip6-nd: support RDNSS option in IPv6 RA
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 12]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 12]: ip6-nd: add nd-proxy all dst

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 7]: crypto: add op tracing capability

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VECr 20]: l2: fix missing CDP hello packets on BVI interface
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 28]: ethernet: implement outer_vlan_id_any sub-interface matching

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 5]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 6]: lb: API bugfix
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 12]: lb: Add punt feature to per-port VIPs

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 0]: interface: add global default rx-mode setting
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VECr 7]: crypto: add op tracing capability
  | `45490 <https:////gerrit.fd.io/r/c/vpp/+/45490>`_ [VECr 10]: gre: fix tunnel dump issues
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 12]: ip: svr add bit indicating fragmentation to vnet_buffer
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VECr 21]: build rpm-packaging: make vpp rpm package for kylinV11

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

pg: **Dave Barach** <vpp@barachs.net>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45502 <https:////gerrit.fd.io/r/c/vpp/+/45502>`_ [VECr 9]: ping: set LOCALLY_ORIGINATED flag on cli-initiated ping packets.

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45556 <https:////gerrit.fd.io/r/c/vpp/+/45556>`_ [VECr 0]: quic: handle half-open cleanup

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [VECr 0]: sfdp: add api enum for timeouts
  | `45101 <https:////gerrit.fd.io/r/c/vpp/+/45101>`_ [VECr 20]: sfdp: guard packet bit shifts in lookup

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 24]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VECr 13]: snort: copy metadata from original to generated packets

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 0]: interface: add global default rx-mode setting
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `45414 <https:////gerrit.fd.io/r/c/vpp/+/45414>`_ [VECr 0]: tests: avoid spurious read timeouts
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core
  | `45454 <https:////gerrit.fd.io/r/c/vpp/+/45454>`_ [VECr 0]: tests: eliminate capture file busy-wait
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [VECr 0]: sfdp: add api enum for timeouts
  | `44966 <https:////gerrit.fd.io/r/c/vpp/+/44966>`_ [VECr 3]: ip-neighbor: fix missing solicited-node multicast MAC
  | `45487 <https:////gerrit.fd.io/r/c/vpp/+/45487>`_ [VECr 5]: lb: Allow setting weight on AS
  | `45428 <https:////gerrit.fd.io/r/c/vpp/+/45428>`_ [VECr 6]: lb: API bugfix
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VECr 8]: ip6-nd: support RDNSS option in IPv6 RA
  | `45490 <https:////gerrit.fd.io/r/c/vpp/+/45490>`_ [VECr 10]: gre: fix tunnel dump issues
  | `45495 <https:////gerrit.fd.io/r/c/vpp/+/45495>`_ [VECr 10]: ip: fix reassembly bugs, add extended SV reass CLI and tests
  | `45494 <https:////gerrit.fd.io/r/c/vpp/+/45494>`_ [VECr 10]: ip: fix reassembly bugs and add tests
  | `45467 <https:////gerrit.fd.io/r/c/vpp/+/45467>`_ [VECr 12]: tests: proper return value checking for 'modern' 'service' APIs
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 12]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 12]: ip6-nd: add nd-proxy all dst
  | `45473 <https:////gerrit.fd.io/r/c/vpp/+/45473>`_ [VECr 12]: tests: add type annotations
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VECr 12]: lb: Add punt feature to per-port VIPs
  | `45475 <https:////gerrit.fd.io/r/c/vpp/+/45475>`_ [VECr 12]: tests: write failed_tests file to test tmp directory
  | `45477 <https:////gerrit.fd.io/r/c/vpp/+/45477>`_ [VECr 12]: tests: add default values for filter/skip-filter
  | `45476 <https:////gerrit.fd.io/r/c/vpp/+/45476>`_ [VECr 12]: tests: add register_exclusive() function
  | `45474 <https:////gerrit.fd.io/r/c/vpp/+/45474>`_ [VECr 12]: tests: add assert_counter_in_range()
  | `45468 <https:////gerrit.fd.io/r/c/vpp/+/45468>`_ [VECr 12]: tests: customizable IP schemes for remote hosts
  | `45466 <https:////gerrit.fd.io/r/c/vpp/+/45466>`_ [VECr 12]: tests: support renaming interfaces
  | `45455 <https:////gerrit.fd.io/r/c/vpp/+/45455>`_ [VECr 12]: tests: move debug ppp() packet formatting outside of test framework
  | `45420 <https:////gerrit.fd.io/r/c/vpp/+/45420>`_ [VECr 13]: tests: replace set_errors_str with "show error" CLI
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VECr 20]: af_xdp: add support for multi-buffer
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 24]: sfdp: add sfdp-session-stats service
  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VECr 25]: tests: reduce sleep interval in ip-neighbor age test
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VECr 28]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

vcl: **Florin Coras** <fcoras@cisco.com>
  | `44450 <https:////gerrit.fd.io/r/c/vpp/+/44450>`_ [VECr 0]: misc: patch to test CI infra

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45262 <https:////gerrit.fd.io/r/c/vpp/+/45262>`_ [VECr 0]: interface: add global default rx-mode setting
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VECr 28]: gso: implement IPv6 extension header traversal

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `45469 <https:////gerrit.fd.io/r/c/vpp/+/45469>`_ [VECr 12]: vlib: avoid warning by using correct node fn declaration
  | `43538 <https:////gerrit.fd.io/r/c/vpp/+/43538>`_ [VECr 20]: stats: show raw value in show stat segment

vpp: **Dave Barach** <vpp@barachs.net>
  | `45289 <https:////gerrit.fd.io/r/c/vpp/+/45289>`_ [VECr 0]: pppoeclient: add PPPoE client plugin with PPPoX core
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 24]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44546 <https:////gerrit.fd.io/r/c/vpp/+/44546>`_ [VECr 14]: vppapigen: error on use of array with unspecified length

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45471 <https:////gerrit.fd.io/r/c/vpp/+/45471>`_ [VECr 12]: vppinfra: add const-qualifier to avoid warning(s)
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 12]: vppinfra: add cast to prevent warning

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45246 <https:////gerrit.fd.io/r/c/vpp/+/45246>`_ [VECr 3]: flow: single-interface-per-flow model

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 55]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 55]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 20]: vhost: fix rxvq interrupts triggered because of race

**Alok Mishra** <almishra@marvell.com>:

  | `42257 <https:////gerrit.fd.io/r/c/vpp/+/42257>`_ [VeC 42]: octeon: implement hardware traffic management

**Andrew Mason** <mason12@gmail.com>:

  | `44082 <https:////gerrit.fd.io/r/c/vpp/+/44082>`_ [vec 165]: linux-cp: Punt for ISIS traffic over linux-cp plugin
  | `44085 <https:////gerrit.fd.io/r/c/vpp/+/44085>`_ [veC 165]: linux-cp: Punt for ISIS traffic over linux-cp plugin

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 89]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 117]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features
  | `43916 <https:////gerrit.fd.io/r/c/vpp/+/43916>`_ [Vec 178]: vlib: print non-parked threads on vlib_worker_thread_barrier_sync_int

**Aritra Basu** <aritrbas@cisco.com>:

  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 31]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 33]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 33]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 33]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 33]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 39]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 117]: pnat: do not disable pnat on rule deletion

**Benoît Ganne** <bganne@cisco.com>:

  | `45573 <https:////gerrit.fd.io/r/c/vpp/+/45573>`_ [VEc 0]: docs: clarify security scope and add SECURITY.md
  | `45203 <https:////gerrit.fd.io/r/c/vpp/+/45203>`_ [VeC 39]: policer: avoid redundant l2_overhead array access on TX path
  | `39443 <https:////gerrit.fd.io/r/c/vpp/+/39443>`_ [veC 52]: vnet: reorder vnet_buffer2 metadata
  | `44962 <https:////gerrit.fd.io/r/c/vpp/+/44962>`_ [VeC 61]: pppoe: initialize sw_if_index before early goto

**C.J. Collier**:

  | `1948 <https:////gerrit.fd.io/r/c/vpp/+/1948>`_ [veC 179]: DO NOT MERGE - testing new build image

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 17]: ikev2: add Curve25519 and Curve448 DH groups
  | `44092 <https:////gerrit.fd.io/r/c/vpp/+/44092>`_ [veC 159]: ipsec: precompute payload and payload length adjustments
  | `44081 <https:////gerrit.fd.io/r/c/vpp/+/44081>`_ [veC 164]: ipsec: fill op templates with lengths and tag sizes

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `45042 <https:////gerrit.fd.io/r/c/vpp/+/45042>`_ [VeC 33]: stats: stat_segment_ls_r() only return NULL on error
  | `45043 <https:////gerrit.fd.io/r/c/vpp/+/45043>`_ [VeC 33]: stats: don't leak regcomp() allocated memory

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 35]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 35]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `44519 <https:////gerrit.fd.io/r/c/vpp/+/44519>`_ [VEc 0]: vppinfra: format_hexdump_trunc, unformat_base10, format_backtrace

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45566 <https:////gerrit.fd.io/r/c/vpp/+/45566>`_ [vEC 0]: sfdp: fix inconsistent session timer updates
  | `44754 <https:////gerrit.fd.io/r/c/vpp/+/44754>`_ [VEc 17]: tracepath: introduce tracepath plugin
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 56]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 103]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `43369 <https:////gerrit.fd.io/r/c/vpp/+/43369>`_ [VEc 0]: cnat: support encapsulation and session cleanup on backend deletion
  | `45110 <https:////gerrit.fd.io/r/c/vpp/+/45110>`_ [vEC 3]: bufmon: unregister old callbacks before re-registering on enable

**Ivan Ivanets** <iivanets@cisco.com>:

  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 54]: crypto: unify per-thread key_data allocation

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `45381 <https:////gerrit.fd.io/r/c/vpp/+/45381>`_ [VEc 4]: linux-cp: add more namespace-based tests

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 73]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 73]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 73]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 73]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [vEC 3]: rdma: add mlx5 TSO support for raw packet tx
  | `44559 <https:////gerrit.fd.io/r/c/vpp/+/44559>`_ [Vec 48]: af_xdp: ensure null termination in format() string outputs
  | `44584 <https:////gerrit.fd.io/r/c/vpp/+/44584>`_ [veC 88]: tests: fix tag_fixme_debian12 to tag_fixme_debian11
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 100]: virtio: add native plugin L2 xconnect test with QEMU

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 75]: vppapigen: fix json build error

**Klement Sekera** <ksekera@netgate.com>:

  | `42486 <https:////gerrit.fd.io/r/c/vpp/+/42486>`_ [VEc 0]: tests: add send_and_expect_multi

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 34]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 34]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 34]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 34]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 9]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 131]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 33]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 39]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 62]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 66]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 101]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 79]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 56]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 61]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 0]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [VEc 5]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 80]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 82]: fix: correct fixstyle in session_sdl command function

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 32]: vppapigen: fix inconsistency in paths JSON

**Ryosuke Nakayama** <ryosuke_666@icloud.com>:

  | `45117 <https:////gerrit.fd.io/r/c/vpp/+/45117>`_ [veC 45]: atlantic: remove unused pkt_n_desc variable
  | `45116 <https:////gerrit.fd.io/r/c/vpp/+/45116>`_ [VeC 45]: snort: fix maybe-uninitialized warning with GCC 15
  | `45119 <https:////gerrit.fd.io/r/c/vpp/+/45119>`_ [VeC 45]: build: add Fedora 43 build compatibility
  | `45113 <https:////gerrit.fd.io/r/c/vpp/+/45113>`_ [VeC 45]: ipsec: fix implicit enum cast warnings with GCC 15
  | `45115 <https:////gerrit.fd.io/r/c/vpp/+/45115>`_ [VeC 45]: sasc: fix maybe-uninitialized warning with GCC 15
  | `45114 <https:////gerrit.fd.io/r/c/vpp/+/45114>`_ [VeC 45]: dpdk: fix maybe-uninitialized warning with GCC 15
  | `45112 <https:////gerrit.fd.io/r/c/vpp/+/45112>`_ [VeC 45]: build: add AlmaLinux support to install-dep target

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [vEC 20]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 115]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 123]: linux-cp: on remove do cleanup for all fibs
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 138]: fib: dump by src not only contributing routes

**Venkata Ravichandra Mynidi** <vmynidi@marvell.com>:

  | `40775 <https:////gerrit.fd.io/r/c/vpp/+/40775>`_ [VEc 26]: tm: add tm framework for hw traffic management

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45058 <https:////gerrit.fd.io/r/c/vpp/+/45058>`_ [VeC 40]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [vEC 20]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 101]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 101]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 101]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 101]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 101]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 102]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 102]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 102]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 102]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 102]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 102]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 102]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [vEC 5]: empty change for GHA(CSIT) testing

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 117]: ip-neighbor: ARP/NA per-interface counter improvements

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 69]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [VEc 20]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [VEc 20]: dns: support ipv6 server to resolve name
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 74]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 126]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VEc 13]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 32]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [vEC 20]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 114]: lb: fix incorrect byte order conversion for vip port display

**ruici wang** <964491902@qq.com>:

  | `44100 <https:////gerrit.fd.io/r/c/vpp/+/44100>`_ [veC 159]: ipsec: prevent use of deleted keys in async mode

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [veC 47]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 102]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 84]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 84]: l2: fix null pointer access in l2-efp-filter

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
authors          108
maintainers      62
committers       0
abandoned        0
================ ===

