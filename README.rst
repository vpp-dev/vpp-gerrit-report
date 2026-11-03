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
generated on Tuesday 2026-11-03, 07:52:46
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

  | `47407 <https:////gerrit.fd.io/r/c/vpp/+/47407>`_ [VECR 0]: http: use per-thread clock for date header

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `47058 <https:////gerrit.fd.io/r/c/vpp/+/47058>`_ [VECr 17]: acl: stop counting hash hits in a shared per-entry field

api: **Dave Barach** <vpp@barachs.net>
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 7]: api: align shared-memory API handler calls
  | `47210 <https:////gerrit.fd.io/r/c/vpp/+/47210>`_ [VECr 7]: api: use unsigned socket handle bit

arp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47276 <https:////gerrit.fd.io/r/c/vpp/+/47276>`_ [VECr 7]: arp: fix reply for local address with adj-fib
  | `46494 <https:////gerrit.fd.io/r/c/vpp/+/46494>`_ [VECr 7]: arp: reset proxy-arp state on interface deletion

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `47321 <https:////gerrit.fd.io/r/c/vpp/+/47321>`_ [VECr 4]: vlib: add helper to check available headroom in vlib_buffer_t

build: **Damjan Marion** <damarion@cisco.com>
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 4]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47270 <https:////gerrit.fd.io/r/c/vpp/+/47270>`_ [VECr 8]: build: refresh optional SPDK upstream snapshot
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VECr 0]: cnat: fix show cnat client showing invalid for client id

dev: **Damjan Marion** <damarion@cisco.com>
  | `47406 <https:////gerrit.fd.io/r/c/vpp/+/47406>`_ [VECr 0]: dev: validate primary Ethernet MAC addresses

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47281 <https:////gerrit.fd.io/r/c/vpp/+/47281>`_ [VECr 7]: dhcp: fix PD client crash without link-local
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 7]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VECr 12]: dispatch-trace: fix SIGSEGV on multi-worker handoff

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 0]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 4]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `47298 <https:////gerrit.fd.io/r/c/vpp/+/47298>`_ [VECr 5]: misc: VPP 26.10 Release Notes
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 7]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 9]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46808 <https:////gerrit.fd.io/r/c/vpp/+/46808>`_ [VECr 28]: docs: announce libvnet visibility change
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 28]: iavf: add setup documentation

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `46939 <https:////gerrit.fd.io/r/c/vpp/+/46939>`_ [VECr 3]: dpdk: don't leak chained mbufs when multi-seg is disabled
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 7]: dpdk: log MFIB MAC replay tolerance at debug level
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 7]: dpdk: read transceiver EEPROM asynchronously, never under the barrier
  | `47200 <https:////gerrit.fd.io/r/c/vpp/+/47200>`_ [VECr 11]: dpdk: fix clib file descriptor leak on admin down
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD
  | `46953 <https:////gerrit.fd.io/r/c/vpp/+/46953>`_ [VECr 24]: dpdk: recognise the the MANA VF as a bifurcated device
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 28]: dpdk: fix QAT cryptodev AEAD sessions

dpdk-cryptodev: **Kai Ji** <kai.ji@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46926 <https:////gerrit.fd.io/r/c/vpp/+/46926>`_ [VECr 28]: dpdk: fix QAT cryptodev AEAD sessions

drivers: **Damjan Marion** <damarion@cisco.com>
  | `47416 <https:////gerrit.fd.io/r/c/vpp/+/47416>`_ [VECr 0]: ice: guard cleanup before port registration

ebuild: **Dave Barach** <vpp@barachs.net>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47211 <https:////gerrit.fd.io/r/c/vpp/+/47211>`_ [VECr 7]: ethernet: compare unaligned MAC addresses

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)

fib: **Neale Ranns** <neale@graphiant.com>
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 0]: fib: fix stale importer pointer in attached-export walk
  | `47292 <https:////gerrit.fd.io/r/c/vpp/+/47292>`_ [VECr 4]: fib: introduce per-source entry count in mfib
  | `47293 <https:////gerrit.fd.io/r/c/vpp/+/47293>`_ [VECr 4]: fib: add mfib_entry_get_n_paths helper
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 5]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 17]: fib: decide the glean source by the address it holds
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 19]: fib: swap in the paths of a source new to the entry

flow: **Damjan Marion** <damarion@cisco.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

gha: **Dave Wallace** <dwallacelf@gmail.com>
  | `47401 <https:////gerrit.fd.io/r/c/vpp/+/47401>`_ [VECr 0]: gha: remove stale LOG_DIR from worflows

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `47405 <https:////gerrit.fd.io/r/c/vpp/+/47405>`_ [VECr 0]: http: support receiving chunked transfer coding
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 4]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `47405 <https:////gerrit.fd.io/r/c/vpp/+/47405>`_ [VECr 0]: http: support receiving chunked transfer coding
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

http: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `47405 <https:////gerrit.fd.io/r/c/vpp/+/47405>`_ [VECr 0]: http: support receiving chunked transfer coding

http_static: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `47405 <https:////gerrit.fd.io/r/c/vpp/+/47405>`_ [VECr 0]: http: support receiving chunked transfer coding

iavf: **Damjan Marion** <damarion@cisco.com>
  | `47413 <https:////gerrit.fd.io/r/c/vpp/+/47413>`_ [VECr 0]: iavf: validate gso headers and tso limits
  | `47411 <https:////gerrit.fd.io/r/c/vpp/+/47411>`_ [VECr 0]: iavf: account for tx drops without descriptors
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 0]: iavf: remove empty gso fragments before tx
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 28]: iavf: add setup documentation

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `47349 <https:////gerrit.fd.io/r/c/vpp/+/47349>`_ [VECr 3]: ikev2: free buffer and still tear down local IKE SA when Delete send fails
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 7]: ikev2: keep GRE protection on Child Delete
  | `47242 <https:////gerrit.fd.io/r/c/vpp/+/47242>`_ [VECr 9]: ikev2: accept responder-initiated Child SA rekey
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 9]: ikev2: allocate Child SA IDs without collision
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 9]: ikev2: accept additional Child SA from responder
  | `47241 <https:////gerrit.fd.io/r/c/vpp/+/47241>`_ [VECr 9]: ikev2: preserve responses across local requests
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 13]: ikev2: configure inbound ESP replay window

interface: **Dave Barach** <vpp@barachs.net>
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VECr 0]: interface: initialize IPv6 link state for unnumbered interfaces
  | `47237 <https:////gerrit.fd.io/r/c/vpp/+/47237>`_ [VECr 6]: interface: make show hardware-interfaces mp-safe
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 7]: pppoeclient: fix orphan TX nodes and shared rename
  | `47213 <https:////gerrit.fd.io/r/c/vpp/+/47213>`_ [VECr 7]: dpdk: read transceiver EEPROM asynchronously, never under the barrier

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 4]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 6]: ip-neighbor: add neighbour table event counters
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 7]: api: align shared-memory API handler calls

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `47383 <https:////gerrit.fd.io/r/c/vpp/+/47383>`_ [VECr 2]: ip: fix IPv6 SVR total payload length
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 4]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 7]: api: align shared-memory API handler calls
  | `47206 <https:////gerrit.fd.io/r/c/vpp/+/47206>`_ [VECr 7]: ip6: use unsigned solicited-node mask
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 9]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 9]: ip: fix adjacent packet overwrite with ip6 frags
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 9]: ip: fix punt socket rx when multiple FDs are ready
  | `47177 <https:////gerrit.fd.io/r/c/vpp/+/47177>`_ [VECr 14]: ip: parse the output-arc IPv6 header in sv-reass update
  | `47172 <https:////gerrit.fd.io/r/c/vpp/+/47172>`_ [VECr 16]: ip: clear l4_hdr_truncated bit in ip4 sv-reass
  | `47173 <https:////gerrit.fd.io/r/c/vpp/+/47173>`_ [VECr 16]: ip: tolerate a NULL total_ip_payload_length in sv-reass lock

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `47208 <https:////gerrit.fd.io/r/c/vpp/+/47208>`_ [VECr 7]: ip6: parse DAD transmit count as u32
  | `47207 <https:////gerrit.fd.io/r/c/vpp/+/47207>`_ [VECr 7]: ip6: wait for event without a DAD timer
  | `47206 <https:////gerrit.fd.io/r/c/vpp/+/47206>`_ [VECr 7]: ip6: use unsigned solicited-node mask

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 7]: ikev2: keep GRE protection on Child Delete
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 9]: ikev2: accept additional Child SA from responder

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47264 <https:////gerrit.fd.io/r/c/vpp/+/47264>`_ [VECr 9]: l2: refuse L3-only bridge and xconnect members

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46901 <https:////gerrit.fd.io/r/c/vpp/+/46901>`_ [VECr 0]: lb: prefetch sticky buckets four packets ahead
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 28]: lb: fix NAT66 UDP/IPv6 checksum zero-fold

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `47295 <https:////gerrit.fd.io/r/c/vpp/+/47295>`_ [VECr 4]: linux-cp: delete multicast routes from the MFIB
  | `47294 <https:////gerrit.fd.io/r/c/vpp/+/47294>`_ [VECr 4]: linux-cp: use special fib/mfib source for special routes
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 5]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47279 <https:////gerrit.fd.io/r/c/vpp/+/47279>`_ [VECr 7]: linux-cp: flush IPv4 routes whenever the host link goes down
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 7]: linux-cp: do not unlock an mfib for MPLS tables
  | `46937 <https:////gerrit.fd.io/r/c/vpp/+/46937>`_ [VECr 7]: linux-cp: only drop a table reference for routes lcp installed
  | `47222 <https:////gerrit.fd.io/r/c/vpp/+/47222>`_ [VECr 9]: linux-cp: avoid a drop path on first route source
  | `46492 <https:////gerrit.fd.io/r/c/vpp/+/46492>`_ [VECr 14]: linux-cp: don't copy an unknown link speed to the host tap
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 18]: linux-cp: add qinq linux to vpp support

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `47274 <https:////gerrit.fd.io/r/c/vpp/+/47274>`_ [VECr 0]: freebsd-cp: FreeBSD Control Plane plugin similar to Linux CP plugin but siginificantly simplified
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 4]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 7]: pppoeclient: fix orphan TX nodes and shared rename
  | `46992 <https:////gerrit.fd.io/r/c/vpp/+/46992>`_ [VECr 7]: pppoeclient: keep control-plane work off workers and pin session VLAN
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 7]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46993 <https:////gerrit.fd.io/r/c/vpp/+/46993>`_ [VECr 7]: pppoeclient: bind the learned VLAN on the main thread
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 7]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 9]: span gre: refuse destinations with no output node
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

nat: **Ole Troan** <otroan@employees.org>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 10]: nat: select dynamic translation by source prefix

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 4]: ip6: fix Pad1 off-by-one in hop-by-hop option pars

papi: **Ole Troan** <otroan@employees.org>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

policer: **Neale Ranns** <neale@graphiant.com>, **Maxime Peim** <maxime.peim@gmail.com>
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 0]: policer: prevent deletion of referenced policers
  | `47209 <https:////gerrit.fd.io/r/c/vpp/+/47209>`_ [VECr 7]: api: align shared-memory API handler calls

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 10]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [VECr 0]: rdma: add mlx5 enhanced MPW with optional inline
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 9]: rdma: add mlx5 DV TSO support for raw packet tx

session: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 10]: udp: add segmentation offload support
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

snort: **Damjan Marion** <damarion@cisco.com>
  | `47231 <https:////gerrit.fd.io/r/c/vpp/+/47231>`_ [VECr 11]: snort: consume the enqueue event before clearing interrupt_pending

span: **N/A
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 9]: span gre: refuse destinations with no output node

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46901 <https:////gerrit.fd.io/r/c/vpp/+/46901>`_ [VECr 0]: lb: prefetch sticky buckets four packets ahead
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VECr 0]: policer: prevent deletion of referenced policers
  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [VECr 0]: misc: patch to test maketest action timeout
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 4]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `47335 <https:////gerrit.fd.io/r/c/vpp/+/47335>`_ [VECr 4]: tests: centralize UDP packet info decoding
  | `46907 <https:////gerrit.fd.io/r/c/vpp/+/46907>`_ [VECr 4]: fastacl: RFC 8955 FlowSpec filter for volumetric DDoS mitigation
  | `46959 <https:////gerrit.fd.io/r/c/vpp/+/46959>`_ [VECr 5]: linux-cp: free lcp_router_table if 0 routes and no lcp pairs only
  | `47291 <https:////gerrit.fd.io/r/c/vpp/+/47291>`_ [VECr 5]: tests: set core_pattern in CI
  | `47239 <https:////gerrit.fd.io/r/c/vpp/+/47239>`_ [VECr 5]: tests: fix core lookup with absolute core_pattern
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 5]: ipsec: IPTFS (RFC 9347) unit tests
  | `47273 <https:////gerrit.fd.io/r/c/vpp/+/47273>`_ [VECr 6]: ip-neighbor: add neighbour table event counters
  | `47217 <https:////gerrit.fd.io/r/c/vpp/+/47217>`_ [VECr 6]: mss_clamp: fix IPv4 vector MSS interface
  | `47279 <https:////gerrit.fd.io/r/c/vpp/+/47279>`_ [VECr 7]: linux-cp: flush IPv4 routes whenever the host link goes down
  | `47120 <https:////gerrit.fd.io/r/c/vpp/+/47120>`_ [VECr 7]: linux-cp: do not unlock an mfib for MPLS tables
  | `47192 <https:////gerrit.fd.io/r/c/vpp/+/47192>`_ [VECr 7]: ikev2: keep GRE protection on Child Delete
  | `47276 <https:////gerrit.fd.io/r/c/vpp/+/47276>`_ [VECr 7]: arp: fix reply for local address with adj-fib
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 7]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46991 <https:////gerrit.fd.io/r/c/vpp/+/46991>`_ [VECr 7]: pppoeclient: echo relay tag and accept PADS without AC-Cookie
  | `46494 <https:////gerrit.fd.io/r/c/vpp/+/46494>`_ [VECr 7]: arp: reset proxy-arp state on interface deletion
  | `47264 <https:////gerrit.fd.io/r/c/vpp/+/47264>`_ [VECr 9]: l2: refuse L3-only bridge and xconnect members
  | `47263 <https:////gerrit.fd.io/r/c/vpp/+/47263>`_ [VECr 9]: span gre: refuse destinations with no output node
  | `47242 <https:////gerrit.fd.io/r/c/vpp/+/47242>`_ [VECr 9]: ikev2: accept responder-initiated Child SA rekey
  | `47194 <https:////gerrit.fd.io/r/c/vpp/+/47194>`_ [VECr 9]: ikev2: allocate Child SA IDs without collision
  | `47247 <https:////gerrit.fd.io/r/c/vpp/+/47247>`_ [VECr 9]: ikev2: accept additional Child SA from responder
  | `47222 <https:////gerrit.fd.io/r/c/vpp/+/47222>`_ [VECr 9]: linux-cp: avoid a drop path on first route source
  | `47241 <https:////gerrit.fd.io/r/c/vpp/+/47241>`_ [VECr 9]: ikev2: preserve responses across local requests
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VECr 9]: tests: make qemu network lock recoverable
  | `47252 <https:////gerrit.fd.io/r/c/vpp/+/47252>`_ [VECr 10]: nat: select dynamic translation by source prefix
  | `46963 <https:////gerrit.fd.io/r/c/vpp/+/46963>`_ [VECr 12]: tests: fix fragment_rfc791/fragment_rfc8200 bugs
  | `47214 <https:////gerrit.fd.io/r/c/vpp/+/47214>`_ [VECr 13]: ikev2: configure inbound ESP replay window
  | `47076 <https:////gerrit.fd.io/r/c/vpp/+/47076>`_ [VECr 17]: fib: decide the glean source by the address it holds
  | `47001 <https:////gerrit.fd.io/r/c/vpp/+/47001>`_ [VECr 18]: linux-cp: add qinq linux to vpp support
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 19]: fib: swap in the paths of a source new to the entry
  | `47020 <https:////gerrit.fd.io/r/c/vpp/+/47020>`_ [VECr 24]: tests: skip parameterized_class base classes in discovery
  | `46995 <https:////gerrit.fd.io/r/c/vpp/+/46995>`_ [VECr 25]: tests: improve return type consistency

udp: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 10]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `47402 <https:////gerrit.fd.io/r/c/vpp/+/47402>`_ [VECr 0]: fib: fix stale importer pointer in attached-export walk
  | `46955 <https:////gerrit.fd.io/r/c/vpp/+/46955>`_ [VECr 4]: ip6: fix Pad1 off-by-one in hop-by-hop option pars
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 6]: ipsec: IPTFS (RFC 9347)
  | `47078 <https:////gerrit.fd.io/r/c/vpp/+/47078>`_ [VECr 19]: fib: swap in the paths of a source new to the entry

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `47205 <https:////gerrit.fd.io/r/c/vpp/+/47205>`_ [VECr 7]: vlib: avoid null pointer arithmetic in main walk
  | `47255 <https:////gerrit.fd.io/r/c/vpp/+/47255>`_ [VECr 9]: vlib: preserve const in plugin suffix lookup
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 7]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

vppapigen: **Ole Troan** <otroan@employees.org>
  | `47253 <https:////gerrit.fd.io/r/c/vpp/+/47253>`_ [VECr 10]: vppapigen: support output plugins on Python 3.15
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 19]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VECr 5]: vppinfra: add cast to prevent warning
  | `47204 <https:////gerrit.fd.io/r/c/vpp/+/47204>`_ [VECr 7]: vppinfra: avoid null member access on hash miss
  | `47188 <https:////gerrit.fd.io/r/c/vpp/+/47188>`_ [VECr 7]: vppinfra: use unsigned CPU feature masks
  | `47056 <https:////gerrit.fd.io/r/c/vpp/+/47056>`_ [VECr 11]: build: Changes in makefiles to enabe build on FreeBSD

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `47322 <https:////gerrit.fd.io/r/c/vpp/+/47322>`_ [VECr 4]: vxlan: check available headroom

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 140]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [vEC 0]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VeC 55]: acl: add callback hooks for list add/del
  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 63]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 164]: snort: don't store snort metadata in buffer

**Andrey Vasilevsky** <anvanster@gmail.com>:

  | `46487 <https:////gerrit.fd.io/r/c/vpp/+/46487>`_ [VeC 32]: nat: look up address-only static mappings with protocol 0

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 109]: crypto: openssl - check ctx alloc/init in key-add

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [VEc 26]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VEc 4]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [veC 39]: ip6-nd: enforce on-link source validation for ND learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 39]: fib: honor unnumbered RX interface in MFIB RPF check
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 52]: ip6-nd: fix unicast NA handling in ND proxy
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VeC 62]: tests: bypass http/https proxy in test curl invocations
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 75]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 118]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 125]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 129]: kube-test: retry Job finalizer cleanup conflicts
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 143]: vlib: fix trace flag loss when multiple pending frames share next frame

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 97]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 133]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 133]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `47240 <https:////gerrit.fd.io/r/c/vpp/+/47240>`_ [vEC 4]: build: default to 64-byte cache lines on aarch64
  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 150]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [vEC 0]: misc: patch to test CI infra

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 110]: acl: correct interface command help

**Florin Coras** <florin.coras@gmail.com>:

  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [veC 62]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [veC 58]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 87]: dpdk: buffer bug fixes

**Gopalakrishnan Subramani** <gsubramani@idirect.net>:

  | `47023 <https:////gerrit.fd.io/r/c/vpp/+/47023>`_ [vEC 24]: igmp: set proxy mfib Accept on host and Forward on router

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 132]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 132]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VEc 27]: sfdp: add sfdp-session-stats service
  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [veC 63]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 124]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 131]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 131]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 131]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 131]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 132]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 132]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 132]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 144]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 144]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 147]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 168]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VEc 3]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 129]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 133]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `47116 <https:////gerrit.fd.io/r/c/vpp/+/47116>`_ [vEC 17]: fib: populate the glean on source reactivation
  | `46905 <https:////gerrit.fd.io/r/c/vpp/+/46905>`_ [VeC 35]: vapi: mark unregistered vl_msg_ids invalid in the lookup table

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 104]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 133]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 133]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 133]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `47415 <https:////gerrit.fd.io/r/c/vpp/+/47415>`_ [vEC 0]: iavf: simplify tx descriptor chain handling
  | `47414 <https:////gerrit.fd.io/r/c/vpp/+/47414>`_ [vEC 0]: iavf: split oversized tso data descriptors
  | `47412 <https:////gerrit.fd.io/r/c/vpp/+/47412>`_ [vEC 0]: iavf: track context descriptor buffer references
  | `47410 <https:////gerrit.fd.io/r/c/vpp/+/47410>`_ [vEC 0]: iavf: wrap outstanding tx index at queue stop

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 145]: ip bonding hash: inner-aware flow hash (opt-in)

**Kai Ji** <kai.ji@intel.com>:

  | `46925 <https:////gerrit.fd.io/r/c/vpp/+/46925>`_ [VEc 5]: crypto: fix engine registration and async dispatch
  | `46927 <https:////gerrit.fd.io/r/c/vpp/+/46927>`_ [VeC 33]: crypto: fix fixed-tag AEAD validation

**Keith Spinney** <kspinney@cisco.com>:

  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [vEC 28]: lb: add NAT6_NOPORT encap type
  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [VEc 28]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [vEC 24]: test: wait for handoff queues to drain before reading a capture
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VeC 49]: vlib: add show handoff pending CLI
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 112]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 112]: api: add build-time python stub generation via vppapigen

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 144]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 145]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <mfabianlf@pm.me>:

  | `47343 <https:////gerrit.fd.io/r/c/vpp/+/47343>`_ [vEc 4]: session: fix certificate registration race

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [VEc 11]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 145]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 151]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 151]: dpdk: multi-thread async flow offload with per-worker caches

**Micha? Czerwonka** <mczka.mczka@gmail.com>:

  | `46900 <https:////gerrit.fd.io/r/c/vpp/+/46900>`_ [VeC 32]: vpp: vpp/vnet/main.c fix parsing vpp option and improve description of usage

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VeC 48]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 73]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 77]: ipip: fix support for ipip6o6 from linux tunnel

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VeC 54]: teib: move the TEIB implementation to a plugin
  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [Vec 54]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [Vec 54]: teib: add tests for the TEIB API

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 52]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 52]: ip6-nd: add nd-proxy all dst

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 151]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46920 <https:////gerrit.fd.io/r/c/vpp/+/46920>`_ [VEc 5]: ip: stop forwarding the Ethernet trailer
  | `46982 <https:////gerrit.fd.io/r/c/vpp/+/46982>`_ [vEC 28]: papi: read stats scalars and gauges when they are accessed
  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [veC 60]: stats: add directory command to vpp_get_stats
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 87]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 94]: vppapigen: fix unaligned access to packed messages

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VeC 40]: cnat: prevent SNAT policy aliasing across FIBs
  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [Vec 40]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [Vec 48]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [Vec 52]: cnat: improve flow statistics and error coverage

**Paul Vinciguerra** <pvinci@vinciconsulting.com>:

  | `47190 <https:////gerrit.fd.io/r/c/vpp/+/47190>`_ [VEc 10]: af_packet: preserve VLAN TPID when restoring stripped tags

**Pavel Lavrukhin** <danttevip@gmail.com>:

  | `47112 <https:////gerrit.fd.io/r/c/vpp/+/47112>`_ [VEc 0]: ikev2 ipip: negotiate USE_TRANSPORT_MODE
  | `47318 <https:////gerrit.fd.io/r/c/vpp/+/47318>`_ [VEc 3]: ikev2: fail the exchange when DH_compute_key returns invalid length
  | `47348 <https:////gerrit.fd.io/r/c/vpp/+/47348>`_ [VEc 3]: ikev2: always clean up local Child SA when sending Delete fails
  | `47320 <https:////gerrit.fd.io/r/c/vpp/+/47320>`_ [VEc 3]: ikev2: validate peer KE payload length
  | `47337 <https:////gerrit.fd.io/r/c/vpp/+/47337>`_ [VEc 3]: linux-cp: reject route with oversized netlink address attribute
  | `47339 <https:////gerrit.fd.io/r/c/vpp/+/47339>`_ [VEc 3]: ikev2: fetch cipher/MD once in crypto_init
  | `47193 <https:////gerrit.fd.io/r/c/vpp/+/47193>`_ [VEc 3]: ikev2: preserve SA IDs after vector shift

**Pavlo Piatakov** <ppiatako@cisco.com>:

  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VeC 54]: cnat: do not count unsupported IP protocols as session alloc failure

**Peter Morrow** <pdmorrow@gmail.com>:

  | `46954 <https:////gerrit.fd.io/r/c/vpp/+/46954>`_ [VEc 21]: vlib: leave a MANA VF down when taking its netvsc device

**Pierre Pfister** <pierre@meter.com>:

  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [VEc 21]: vlib: resume a process once per suspension

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 13]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [veC 64]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [veC 65]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 159]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 171]: octeon: add PFC support

**Ram Subramanian** <ram@meter.com>:

  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VeC 38]: vnet: install missing vnet headers

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VEc 9]: vlib: ASAN-poison unallocated buffers
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VeC 41]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 99]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 131]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 117]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 90]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 97]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 97]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 99]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 101]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 103]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VEc 3]: fib: dump by src not only contributing routes
  | `47106 <https:////gerrit.fd.io/r/c/vpp/+/47106>`_ [VEc 4]: vnet: rewrite nodes to check available headroom

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [vEC 0]: misc: surs patch to test CI infra
  | `47289 <https:////gerrit.fd.io/r/c/vpp/+/47289>`_ [vEC 6]: tests: add temporary core backtrace crash diagnostic
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 74]: docs: Get the VPP Source

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 110]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 111]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 110]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 168]: flowprobe: count based sampling support

**Vratko Polak** <vrpolak@cisco.com>:

  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VeC 45]: buffers: make natural layout always default
  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 157]: sfdp_services: add basic support for time-wait

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 130]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 159]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 159]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 160]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 161]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 166]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 122]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [Vec 34]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [Vec 34]: ip6-nd: support RDNSS option in IPv6 RA

**juhua yin** <ameliayin1990@gmail.com>:

  | `46828 <https:////gerrit.fd.io/r/c/vpp/+/46828>`_ [Vec 41]: dpdk: fix change mac address of the member failed

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 176]: vlib: fix '\' command input will causes memory out of bounds

**marek zavodsky** <mazavods@gmail.com>:

  | `47316 <https:////gerrit.fd.io/r/c/vpp/+/47316>`_ [VEc 0]: http: h1 - handling of big request/response header section

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [vEC 28]: cnat: add scope_id to session key
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 71]: vlib: re-base the timing wheel when arming an empty wheel

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 12]: vcl: fix crash when closing listener with pending accepts
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 172]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 174]: tls: fix picotls partial record handling

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [A 180]: dpdk: tracing improvements

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
authors          149
maintainers      100
committers       1
abandoned        1
================ ===

