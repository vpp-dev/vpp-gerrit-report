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
generated on Saturday 2026-10-10, 07:01:16
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

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 17]: vlib: ASAN-poison unallocated buffers
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 21]: buffers: make natural layout always default

build: **Damjan Marion** <damarion@cisco.com>
  | `46291 <https:////gerrit.fd.io/r/c/vpp/+/46291>`_ [VECr 5]: build: add SPDK as an external dependency
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 11]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 21]: buffers: make natural layout always default
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 24]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 16]: cnat: prevent SNAT policy aliasing across FIBs
  | `46809 <https:////gerrit.fd.io/r/c/vpp/+/46809>`_ [VECr 22]: cnat: skip output SNAT for unsupported protocols
  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VECr 30]: cnat: do not count unsupported IP protocols as session alloc failure

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 21]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 0]: misc: surs patch to test CI infra
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra
  | `46808 <https:////gerrit.fd.io/r/c/vpp/+/46808>`_ [VECr 4]: docs: announce libvnet visibility change
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 4]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 4]: iavf: add setup documentation
  | `46292 <https:////gerrit.fd.io/r/c/vpp/+/46292>`_ [VECr 5]: spdk: add in-process NVMe/TCP target plugin
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 9]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 11]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 21]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 21]: buffers: make natural layout always default
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46953 <https:////gerrit.fd.io/r/c/vpp/+/46953>`_ [VECr 0]: dpdk: recognise the the MANA VF as a bifurcated device
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 4]: dpdk: fix QAT cryptodev AEAD sessions
  | `46939 <https:////gerrit.fd.io/r/c/vpp/+/46939>`_ [VECr 9]: dpdk: don't leak chained mbufs when multi-seg is disabled
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 21]: dpdk: log MFIB MAC replay tolerance at debug level

dpdk-cryptodev: **Kai Ji** <kai.ji@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 4]: dpdk: fix QAT cryptodev AEAD sessions

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 4]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)

fib: **Neale Ranns** <neale@graphiant.com>
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 3]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `46486 <https:////gerrit.fd.io/r/c/vpp/+/46486>`_ [VECr 15]: fib ethernet: honour ethernet-output features on L2 adjacencies
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 15]: fib: honor unnumbered RX interface in MFIB RPF check

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 17]: hsi: wake drains when ownership changes

hsi: **Florin Coras** <fcoras@cisco.com>
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 17]: hsi: wake drains when ownership changes

iavf: **Damjan Marion** <damarion@cisco.com>
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 4]: iavf: add setup documentation
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 13]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 21]: pppoeclient: fix orphan TX nodes and shared rename

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VECr 10]: ip: stop forwarding the Ethernet trailer
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 17]: ip: fix punt socket rx when multiple FDs are ready
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 17]: ip: fix adjacent packet overwrite with ip6 frags
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 17]: ip: fix adjacent packet overwrite with ip frags
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 17]: ip: fix ip mroute bulk insertion CLI for certain inputs

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 10]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 28]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 28]: ip6-nd: add nd-proxy all dst
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 28]: ip6-nd: fix unicast NA handling in ND proxy

ipip: **Ole Troan** <otroan@employees.org>
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 4]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 4]: lb: fix NAT66 UDP/IPv6 checksum zero-fold
  | `46901 <https:////gerrit.fd.io/r/c/vpp/+/46901>`_ [VECr 10]: lb: prefetch sticky buckets four packets ahead

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 3]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `46937 <https:////gerrit.fd.io/r/c/vpp/+/46937>`_ [VECr 9]: linux-cp: only drop a table reference for routes lcp installed

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46993 <https:////gerrit.fd.io/r/c/vpp/+/46993>`_ [VECr 2]: pppoeclient: bind the learned VLAN on the main thread
  | `46992 <https:////gerrit.fd.io/r/c/vpp/+/46992>`_ [VECr 2]: pppoeclient: keep control-plane work off workers and pin session VLAN
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 2]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 4]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)
  | `46292 <https:////gerrit.fd.io/r/c/vpp/+/46292>`_ [VECr 5]: spdk: add in-process NVMe/TCP target plugin
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VECr 9]: crypto: fix fixed-tag AEAD validation
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 11]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VECr 14]: vnet: install missing vnet headers
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 21]: pppoeclient: fix orphan TX nodes and shared rename
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 21]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 24]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `46487 <https:////gerrit.fd.io/r/c/vpp/+/46487>`_ [VECr 8]: nat: look up address-only static mappings with protocol 0

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 5]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 9]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [VECr 9]: rdma: add mlx5 enhanced MPW with optional inline
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 21]: rdma: steer PPPoE discovery and session flows

session: **Florin Coras** <fcoras@cisco.com>
  | `47025 <https:////gerrit.fd.io/r/c/vpp/+/47025>`_ [VECr 0]: vnet: export more symbols
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 5]: udp: add segmentation offload support
  | `46797 <https:////gerrit.fd.io/r/c/vpp/+/46797>`_ [VECr 23]: session: report refused for local connect miss
  | `46473 <https:////gerrit.fd.io/r/c/vpp/+/46473>`_ [VECr 29]: session: revalidate ct listener during accept

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 1]: sfdp: add api sfdp_kill_session_batch
  | `46952 <https:////gerrit.fd.io/r/c/vpp/+/46952>`_ [VECr 8]: sfdp: add/del tenant notification callbacks

svm: **Dave Barach** <vpp@barachs.net>
  | `46280 <https:////gerrit.fd.io/r/c/vpp/+/46280>`_ [VECr 5]: svm: allow fifo chunk provisioning at offset

teib: **Neale Ranns** <neale@graphiant.com>
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `47020 <https:////gerrit.fd.io/r/c/vpp/+/47020>`_ [VECr 0]: tests: skip parameterized_class base classes in discovery
  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [VECr 0]: misc: patch to test maketest action timeout
  | `46995 <https:////gerrit.fd.io/r/c/vpp/+/46995>`_ [VECr 0]: tests: improve return type consistency
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 1]: sfdp: add api sfdp_kill_session_batch
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 3]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 4]: ipsec: IPTFS (RFC 9347) unit tests
  | `46966 <https:////gerrit.fd.io/r/c/vpp/+/46966>`_ [VECr 4]: ikev2: guard unassigned profiles in SA status
  | `46963 <https:////gerrit.fd.io/r/c/vpp/+/46963>`_ [VECr 6]: tests: fix fragment_rfc791/fragment_rfc8200 bugs
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VECr 10]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VECr 10]: ip: stop forwarding the Ethernet trailer
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 11]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VECr 15]: fib: honor unnumbered RX interface in MFIB RPF check
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 16]: cnat: prevent SNAT policy aliasing across FIBs
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 17]: vlib: ASAN-poison unallocated buffers
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 17]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 21]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46809 <https:////gerrit.fd.io/r/c/vpp/+/46809>`_ [VECr 22]: cnat: skip output SNAT for unsupported protocols
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 28]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 28]: ip6-nd: add nd-proxy all dst
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 28]: ip6-nd: fix unicast NA handling in ND proxy
  | `46541 <https:////gerrit.fd.io/r/c/vpp/+/46541>`_ [VECr 30]: tests: preserve LD_PRELOAD across stdbuf on uutils (Rust)
  | `46554 <https:////gerrit.fd.io/r/c/vpp/+/46554>`_ [VECr 30]: tests: fix multiprocessing Python 3.14 failures on Ubuntu 26.04
  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VECr 30]: cnat: do not count unsupported IP protocols as session alloc failure
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

udp: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 5]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46280 <https:////gerrit.fd.io/r/c/vpp/+/46280>`_ [VECr 5]: svm: allow fifo chunk provisioning at offset
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 7]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VECr 9]: crypto: fix fixed-tag AEAD validation
  | `46797 <https:////gerrit.fd.io/r/c/vpp/+/46797>`_ [VECr 23]: session: report refused for local connect miss
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 30]: teib: move the TEIB implementation to a plugin

vapi: **Ole Troan** <otroan@employees.org>
  | `46905 <https:////gerrit.fd.io/r/c/vpp/+/46905>`_ [VECr 11]: vapi: mark unregistered vl_msg_ids invalid in the lookup table

vcl: **Florin Coras** <fcoras@cisco.com>
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 0]: misc: surs patch to test CI infra
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 0]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46857 <https:////gerrit.fd.io/r/c/vpp/+/46857>`_ [VECr 1]: vlib: initialize process sleep timer handle to ~0
  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [VECr 1]: vlib: resume a process once per suspension
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 21]: buffers: make natural layout always default
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VECr 25]: vlib: add show handoff pending CLI

vpp: **Dave Barach** <vpp@barachs.net>
  | `46900 <https:////gerrit.fd.io/r/c/vpp/+/46900>`_ [VECr 8]: vpp: vpp/vnet/main.c fix parsing vpp option and improve description of usage
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 21]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 21]: buffers: make natural layout always default

vpp-swan: **Fan Zhang** <fanzhang.oss@gmail.com>, **Gabriel Oginski** <gabrielx.oginski@intel.com>
  | `46958 <https:////gerrit.fd.io/r/c/vpp/+/46958>`_ [VECr 8]: vpp-swan: Replace call to clib_mem_init_thread_safe with clib_mem_init

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 116]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 123]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 123]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VeC 31]: acl: add callback hooks for list add/del
  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 39]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 140]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 85]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 163]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VEc 2]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `47003 <https:////gerrit.fd.io/r/c/vpp/+/47003>`_ [vEC 0]: vppinfra: fix race draining deleted files
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [vEC 15]: ip6-nd: enforce on-link source validation for ND learning
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VeC 38]: tests: bypass http/https proxy in test curl invocations
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 50]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 94]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 101]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 105]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 119]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 119]: vlib: fix trace flag loss when multiple pending frames share next frame

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 73]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 109]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 109]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 126]: ikev2: add Curve25519 and Curve448 DH groups

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 86]: acl: correct interface command help

**Florin Coras** <florin.coras@gmail.com>:

  | `46826 <https:////gerrit.fd.io/r/c/vpp/+/46826>`_ [vEC 0]: tcp: add cubic hystart++ support RFC 9406
  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [veC 38]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VEc 4]: ipsec: IPTFS (RFC 9347) foundation
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [veC 34]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 63]: dpdk: buffer bug fixes
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 156]: dpdk: tracing improvements

**Gopalakrishnan Subramani** <gsubramani@idirect.net>:

  | `47021 <https:////gerrit.fd.io/r/c/vpp/+/47021>`_ [vEC 0]: igmp: set proxy mfib Accept on host and Forward on router
  | `47023 <https:////gerrit.fd.io/r/c/vpp/+/47023>`_ [vEC 0]: igmp: set proxy mfib Accept on host and Forward on router

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 108]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 108]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VEc 3]: sfdp: add sfdp-session-stats service
  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [veC 39]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 100]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 107]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 107]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 107]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 107]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 108]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 108]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 108]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 120]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 120]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 123]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 144]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 109]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 105]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 109]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 80]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 109]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 109]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 109]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46636 <https:////gerrit.fd.io/r/c/vpp/+/46636>`_ [VeC 35]: tests: avoid repeated pg barriers awaiting capture
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VeC 36]: vnet: keep deleted interface node names unique
  | `46719 <https:////gerrit.fd.io/r/c/vpp/+/46719>`_ [VeC 36]: tests: avoid iperf preexec deadlocks
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VeC 36]: tests: make qemu network lock recoverable

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 121]: ip bonding hash: inner-aware flow hash (opt-in)

**Kai Ji** <kai.ji@intel.com>:

  | `46925 <https:////gerrit.fd.io/r/c/vpp/+/46925>`_ [VEc 0]: crypto: fix engine registration and async dispatch

**Keith Spinney** <kspinney@cisco.com>:

  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [vEC 4]: lb: add NAT6_NOPORT encap type
  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [VEc 4]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [vEC 0]: test: wait for handoff queues to drain before reading a capture
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 88]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 88]: api: add build-time python stub generation via vppapigen
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 170]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 120]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 121]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [VEc 2]: flow: add per-thread flow pool cache for multi-worker safety
  | `46800 <https:////gerrit.fd.io/r/c/vpp/+/46800>`_ [VEc 2]: vlib: pool-cache prefill and foreach macro
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VEc 25]: policer: reject deletion of policer used by punt policing
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vec 98]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 121]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 127]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 127]: dpdk: multi-thread async flow offload with per-worker caches

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 49]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 53]: ipip: fix support for ipip6o6 from linux tunnel

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [VEc 30]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [VEc 30]: teib: add tests for the TEIB API

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 127]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [vEC 4]: papi: read stats scalars and gauges when they are accessed
  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [veC 36]: stats: add directory command to vpp_get_stats
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 63]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 70]: vppapigen: fix unaligned access to packed messages
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 177]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [VEc 16]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [VEc 24]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [VEc 28]: cnat: improve flow statistics and error coverage

**Peter Morrow** <pdmorrow@gmail.com>:

  | `46954 <https:////gerrit.fd.io/r/c/vpp/+/46954>`_ [VEc 0]: vlib: leave a MANA VF down when taking its netvsc device

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 9]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [veC 40]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [veC 40]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 135]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 147]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [vEC 17]: vppapigen: fix inconsistency in paths JSON
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 75]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `47017 <https:////gerrit.fd.io/r/c/vpp/+/47017>`_ [vEC 0]: http: fix h2 hang on continuation already in fifo
  | `47019 <https:////gerrit.fd.io/r/c/vpp/+/47019>`_ [vEC 0]: http: fix h2 crash on unexpected DATA frame
  | `47002 <https:////gerrit.fd.io/r/c/vpp/+/47002>`_ [vEC 0]: quic: fix connection leak on app reset
  | `47009 <https:////gerrit.fd.io/r/c/vpp/+/47009>`_ [VEc 0]: tls: fix openssl rx spin when app fifo can't grow
  | `47000 <https:////gerrit.fd.io/r/c/vpp/+/47000>`_ [VEc 0]: tls http: fix accept after listener stops
  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 107]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 93]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 66]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 73]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 73]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 75]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 77]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 79]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VEc 23]: fib: dump by src not only contributing routes

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 50]: docs: Get the VPP Source

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 86]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 87]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 85]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 144]: flowprobe: count based sampling support

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 133]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 177]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `47026 <https:////gerrit.fd.io/r/c/vpp/+/47026>`_ [vEc 0]: hsi-plugin: expose hsi API functions for re-use
  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 106]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 135]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 135]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 136]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 137]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 142]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 98]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VEc 10]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VEc 10]: ip6-nd: support RDNSS option in IPv6 RA

**jiang li** <1394788707@qq.com>:

  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VEc 9]: dispatch-trace: fix SIGSEGV/SIGABRT on multi-worker handoff

**juhua yin** <ameliayin1990@gmail.com>:

  | `46828 <https:////gerrit.fd.io/r/c/vpp/+/46828>`_ [VEc 16]: dpdk: fix change mac address of the member failed

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 151]: vlib: fix '\' command input will causes memory out of bounds

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 166]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 4]: cnat: add scope_id to session key
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 47]: vlib: re-base the timing wheel when arming an empty wheel

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 161]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 148]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 150]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 151]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 157]: session: make transport to use application's segment manager

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
authors          138
maintainers      70
committers       0
abandoned        0
================ ===

