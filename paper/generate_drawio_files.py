import os

PAPER_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(PAPER_DIR, exist_ok=True)

# 1. FIG 1: V2X Ecosystem Draw.io XML
fig1_xml = """<mxfile host="app.diagrams.net" modified="2026-11-03T01:40:00.000Z" agent="Mozilla/5.0" version="24.0.0">
  <diagram id="v2x_ecosystem" name="V2X Architecture">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="700" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Outer boundary -->
        <mxCell id="bg" value="V2X Connected &amp; Autonomous Vehicular Ecosystem" style="swimlane;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=#BDC1C6;fontStyle=1;fontSize=14;fontColor=#202124;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1020" height="580" as="geometry"/>
        </mxCell>
        
        <!-- Central Host OBU Node -->
        <mxCell id="obu" value="&lt;b&gt;Host Connected Vehicle (OBU)&lt;/b&gt;&lt;hr/&gt;• On-Board Unit (OBU) Edge Processor&lt;br/&gt;• High-Rate Telemetry Ingestion&lt;br/&gt;• Real-Time KAN-GRU Threat Engine&lt;br/&gt;• Multi-Label Anomaly Classifier" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0FE;strokeColor=#1A73E8;strokeWidth=2;fontSize=12;fontColor=#174EA6;spacing=8;" vertex="1" parent="bg">
          <mxGeometry x="360" y="200" width="300" height="180" as="geometry"/>
        </mxCell>
        
        <!-- Top-Left: Peer Vehicle (V2V) -->
        <mxCell id="v2v" value="&lt;b&gt;Peer Vehicle (V2V)&lt;/b&gt;&lt;hr/&gt;• Basic Safety Messages (BSM)&lt;br/&gt;• Cooperative Awareness (CAM)&lt;br/&gt;• Cooperative Collision Warning&lt;br/&gt;• High-Speed Platooning Control" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F4EA;strokeColor=#1E8E3E;strokeWidth=2;fontSize=11;fontColor=#137333;spacing=6;" vertex="1" parent="bg">
          <mxGeometry x="50" y="70" width="240" height="140" as="geometry"/>
        </mxCell>
        
        <!-- Top-Right: Roadside Unit (V2I) -->
        <mxCell id="v2i" value="&lt;b&gt;Roadside Unit / RSU (V2I)&lt;/b&gt;&lt;hr/&gt;• Signal Phase &amp; Timing (SPAT)&lt;br/&gt;• Intersection Geometry (MAP)&lt;br/&gt;• Roadside Safety Alerts (RSA)&lt;br/&gt;• Intersection Collision Mitigation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF7E0;strokeColor=#F9AB00;strokeWidth=2;fontSize=11;fontColor=#B06000;spacing=6;" vertex="1" parent="bg">
          <mxGeometry x="730" y="70" width="240" height="140" as="geometry"/>
        </mxCell>
        
        <!-- Bottom-Left: Pedestrian (V2P) -->
        <mxCell id="v2p" value="&lt;b&gt;Vulnerable Road Users (V2P)&lt;/b&gt;&lt;hr/&gt;• Pedestrian Smartphone Telemetry&lt;br/&gt;• Cyclist Proximity Beacons&lt;br/&gt;• Crosswalk Protection Alerts&lt;br/&gt;• DSRC/C-V2X Direct Broadcast" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE8E6;strokeColor=#D93025;strokeWidth=2;fontSize=11;fontColor=#C5221F;spacing=6;" vertex="1" parent="bg">
          <mxGeometry x="50" y="370" width="240" height="140" as="geometry"/>
        </mxCell>
        
        <!-- Bottom-Right: Cloud / 5G (V2N) -->
        <mxCell id="v2n" value="&lt;b&gt;Cellular Base Station / Cloud (V2N)&lt;/b&gt;&lt;hr/&gt;• 5G NR-V2X gNodeB Infrastructure&lt;br/&gt;• Central Traffic Orchestrator&lt;br/&gt;• Fleet-Wide Threat Intelligence&lt;br/&gt;• Global Dynamic Map Distribution" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E8FD;strokeColor=#9334E6;strokeWidth=2;fontSize=11;fontColor=#7627BB;spacing=6;" vertex="1" parent="bg">
          <mxGeometry x="730" y="370" width="240" height="140" as="geometry"/>
        </mxCell>
        
        <!-- Connecting Arrows -->
        <mxCell id="arr_v2v" value="&lt;b&gt;V2V Direct Link&lt;/b&gt;&lt;br/&gt;(100 ms DSRC)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#1E8E3E;strokeWidth=2;fontColor=#1E8E3E;fontSize=10;" edge="1" parent="bg" source="v2v" target="obu">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arr_v2i" value="&lt;b&gt;V2I Link&lt;/b&gt;&lt;br/&gt;(5.9 GHz DSRC)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#F9AB00;strokeWidth=2;fontColor=#B06000;fontSize=10;" edge="1" parent="bg" source="v2i" target="obu">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arr_v2p" value="&lt;b&gt;V2P Safety Link&lt;/b&gt;&lt;br/&gt;(Direct Sidelink PC5)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.75;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#D93025;strokeWidth=2;fontColor=#C5221F;fontSize=10;" edge="1" parent="bg" source="v2p" target="obu">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="arr_v2n" value="&lt;b&gt;V2N 5G Link&lt;/b&gt;&lt;br/&gt;(Uu Cellular Interface)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.75;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#9334E6;strokeWidth=2;fontColor=#7627BB;fontSize=10;" edge="1" parent="bg" source="v2n" target="obu">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open(os.path.join(PAPER_DIR, "fig1_v2x_ecosystem.drawio"), "w") as f:
    f.write(fig1_xml)

# 2. FIG 2: Threat Taxonomy Draw.io XML
fig2_xml = """<mxfile host="app.diagrams.net" modified="2026-11-03T01:40:00.000Z" agent="Mozilla/5.0" version="24.0.0">
  <diagram id="threat_taxonomy" name="V2X Threat Taxonomy">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="700" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Root node -->
        <mxCell id="root" value="&lt;b&gt;V2X Cyber-Physical Security Threat Taxonomy&lt;/b&gt;&lt;br/&gt;(Multi-Label Anomaly Landscape)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1A73E8;strokeColor=#155724;fontColor=#ffffff;fontSize=13;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="350" y="30" width="400" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pillar 1: Authentication -->
        <mxCell id="p1" value="&lt;b&gt;Authentication&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0FE;strokeColor=#1A73E8;fontColor=#174EA6;fontSize=11;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="40" y="140" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="p1_desc" value="• &lt;b&gt;Sybil Attacks&lt;/b&gt;&lt;br/&gt;• Ghost Vehicle Injections&lt;br/&gt;• Masquerade Attacks&lt;br/&gt;• Rogue Cert Signatures" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1A73E8;fontColor=#202124;fontSize=10;align=left;spacing=8;" vertex="1" parent="1">
          <mxGeometry x="40" y="190" width="180" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Pillar 2: Availability -->
        <mxCell id="p2" value="&lt;b&gt;Availability&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF7E0;strokeColor=#F9AB00;fontColor=#B06000;fontSize=11;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="250" y="140" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="p2_desc" value="• &lt;b&gt;Spam Flooding Attacks&lt;/b&gt;&lt;br/&gt;• Channel Jamming (DSRC)&lt;br/&gt;• Non-Priority Packet Floods&lt;br/&gt;• Bandwidth Exhaustion" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#F9AB00;fontColor=#202124;fontSize=10;align=left;spacing=8;" vertex="1" parent="1">
          <mxGeometry x="250" y="190" width="180" height="100" as="geometry"/>
        </mxCell>

        <!-- Pillar 3: Confidentiality -->
        <mxCell id="p3" value="&lt;b&gt;Confidentiality&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE8E6;strokeColor=#D93025;fontColor=#C5221F;fontSize=11;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="460" y="140" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="p3_desc" value="• Radio Eavesdropping&lt;br/&gt;• Side-Channel Sniffing&lt;br/&gt;• Man-in-the-Middle (MitM)&lt;br/&gt;• Cleartext Telemetry Leaks" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#D93025;fontColor=#202124;fontSize=10;align=left;spacing=8;" vertex="1" parent="1">
          <mxGeometry x="460" y="190" width="180" height="100" as="geometry"/>
        </mxCell>

        <!-- Pillar 4: Integrity -->
        <mxCell id="p4" value="&lt;b&gt;Integrity&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F4EA;strokeColor=#1E8E3E;fontColor=#137333;fontSize=11;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="670" y="140" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="p4_desc" value="• &lt;b&gt;GPS / Location Tampering&lt;/b&gt;&lt;br/&gt;• &lt;b&gt;Replay Attacks&lt;/b&gt;&lt;br/&gt;• &lt;b&gt;False Information&lt;/b&gt;&lt;br/&gt;• Fictitious DENM Hazards" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1E8E3E;fontColor=#202124;fontSize=10;align=left;spacing=8;" vertex="1" parent="1">
          <mxGeometry x="670" y="190" width="180" height="100" as="geometry"/>
        </mxCell>

        <!-- Pillar 5: Privacy -->
        <mxCell id="p5" value="&lt;b&gt;Privacy&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E8FD;strokeColor=#9334E6;fontColor=#7627BB;fontSize=11;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="880" y="140" width="180" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="p5_desc" value="• Vehicular Tracking&lt;br/&gt;• Certificate De-anonymization&lt;br/&gt;• Location History Profiling&lt;br/&gt;• MAC Address Corroboration" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9334E6;fontColor=#202124;fontSize=10;align=left;spacing=8;" vertex="1" parent="1">
          <mxGeometry x="880" y="190" width="180" height="100" as="geometry"/>
        </mxCell>
        
        <!-- Branches from Root -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=1.5;" edge="1" parent="1" source="root" target="p1"/>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=1.5;" edge="1" parent="1" source="root" target="p2"/>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=1.5;" edge="1" parent="1" source="root" target="p3"/>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=1.5;" edge="1" parent="1" source="root" target="p4"/>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=1.5;" edge="1" parent="1" source="root" target="p5"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open(os.path.join(PAPER_DIR, "fig2_threat_taxonomy.drawio"), "w") as f:
    f.write(fig2_xml)

# 3. FIG 3: Process Flowchart Draw.io XML
fig3_xml = """<mxfile host="app.diagrams.net" modified="2026-11-03T01:40:00.000Z" agent="Mozilla/5.0" version="24.0.0">
  <diagram id="process_flowchart" name="Deep Learning Process Flow">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="700" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Step 1: Start & Input -->
        <mxCell id="s1" value="&lt;b&gt;START &amp; DATA INGESTION&lt;/b&gt;&lt;hr/&gt;• IEEE DataPort V2X Dataset&lt;br/&gt;• 6,000 Synthetic PDUs&lt;br/&gt;• Protocols: BSM, CAM, DENM,&lt;br/&gt;  SPAT, MAP, RSA&lt;br/&gt;• 5 Cyber-Threat Classes" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8EAED;strokeColor=#5F6368;strokeWidth=2;fontSize=10;fontColor=#202124;" vertex="1" parent="1">
          <mxGeometry x="30" y="100" width="180" height="160" as="geometry"/>
        </mxCell>
        
        <!-- Step 2: Preprocessing -->
        <mxCell id="s2" value="&lt;b&gt;TEXT PREPROCESSING&lt;/b&gt;&lt;hr/&gt;• Regex Key-Value Extraction&lt;br/&gt;• Alphanumeric Tokenizer&lt;br/&gt;• Ranked Vocab (|V|=1,500)&lt;br/&gt;• Post-Padding (L=50)&lt;br/&gt;• Multi-Label Binarizer (11-d)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0FE;strokeColor=#1A73E8;strokeWidth=2;fontSize=10;fontColor=#174EA6;" vertex="1" parent="1">
          <mxGeometry x="250" y="100" width="180" height="160" as="geometry"/>
        </mxCell>
        
        <!-- Step 3: DL Architectures -->
        <mxCell id="s3" value="&lt;b&gt;DEEP LEARNING SUITE&lt;/b&gt;&lt;hr/&gt;• &lt;b&gt;Proposed KAN-GRU&lt;/b&gt;&lt;br/&gt;• CNN-BRNN (Enhanced)&lt;br/&gt;• Standalone KAN Layer&lt;br/&gt;• Bidirectional GRU / BRNN&lt;br/&gt;• CNN-BLSTM / BLSTM" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF7E0;strokeColor=#F9AB00;strokeWidth=2;fontSize=10;fontColor=#B06000;" vertex="1" parent="1">
          <mxGeometry x="470" y="100" width="180" height="160" as="geometry"/>
        </mxCell>

        <!-- Step 4: Inference Engine -->
        <mxCell id="s4" value="&lt;b&gt;KAN-GRU INFERENCE&lt;/b&gt;&lt;hr/&gt;• Spline Edge Activations s(x)&lt;br/&gt;• 2-Layer BiGRU Temporal Gates&lt;br/&gt;• Attention Weight Pooling (α_t)&lt;br/&gt;• Dropout (p=0.20) + LayerNorm&lt;br/&gt;• Independent Sigmoids (τ=0.40)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6F4EA;strokeColor=#1E8E3E;strokeWidth=2;fontSize=10;fontColor=#137333;" vertex="1" parent="1">
          <mxGeometry x="690" y="100" width="180" height="160" as="geometry"/>
        </mxCell>

        <!-- Step 5: Decision & Metrics -->
        <mxCell id="s5" value="&lt;b&gt;METRIC VERIFICATION&lt;/b&gt;&lt;hr/&gt;• Accuracy: &lt;b&gt;97.80%&lt;/b&gt;&lt;br/&gt;• Precision: &lt;b&gt;99.45%&lt;/b&gt;&lt;br/&gt;• Recall: &lt;b&gt;96.80%&lt;/b&gt;&lt;br/&gt;• F1-Score: &lt;b&gt;98.10%&lt;/b&gt;&lt;br/&gt;• Latency: &lt;b&gt;7.82 ms/packet&lt;/b&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE8E6;strokeColor=#D93025;strokeWidth=2;fontSize=10;fontColor=#C5221F;" vertex="1" parent="1">
          <mxGeometry x="910" y="100" width="180" height="160" as="geometry"/>
        </mxCell>
        
        <!-- Flow Connectors -->
        <mxCell id="c1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="s1" target="s2"/>
        <mxCell id="c2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="s2" target="s3"/>
        <mxCell id="c3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="s3" target="s4"/>
        <mxCell id="c4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="s4" target="s5"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open(os.path.join(PAPER_DIR, "fig3_process_flowchart.drawio"), "w") as f:
    f.write(fig3_xml)

# 4. FIG 4: KAN-GRU Architecture Draw.io XML
fig4_xml = """<mxfile host="app.diagrams.net" modified="2026-11-03T01:40:00.000Z" agent="Mozilla/5.0" version="24.0.0">
  <diagram id="kangru_architecture" name="KAN-GRU Architecture">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="700" background="#ffffff">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Stage 1: Input -->
        <mxCell id="st1" value="&lt;b&gt;Input Vector x&lt;/b&gt;&lt;hr/&gt;x in Z^{B x 50}&lt;br/&gt;Post-Padded Tokens&lt;br/&gt;L=50, Batch B=32" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F0FE;strokeColor=#1A73E8;strokeWidth=2;fontSize=10;fontColor=#174EA6;" vertex="1" parent="1">
          <mxGeometry x="30" y="80" width="180" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Stage 2: Embedding -->
        <mxCell id="st2" value="&lt;b&gt;Dense Embedding E&lt;/b&gt;&lt;hr/&gt;E in R^{B x 50 x 128}&lt;br/&gt;Embedding Matrix W_emb&lt;br/&gt;Vocabulary |V|=1,500&lt;br/&gt;Continuous Manifold" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D2E3FC;strokeColor=#1A73E8;strokeWidth=2;fontSize=10;fontColor=#174EA6;" vertex="1" parent="1">
          <mxGeometry x="250" y="80" width="190" height="150" as="geometry"/>
        </mxCell>

        <!-- Stage 3: KAN Layer -->
        <mxCell id="st3" value="&lt;b&gt;KAN Spline Layer&lt;/b&gt;&lt;hr/&gt;X_KAN = W_b E + W_sp o SiLU(E)&lt;br/&gt;Learnable Univariate B-Splines&lt;br/&gt;Edge Activation Functions&lt;br/&gt;Non-Linear Boundary Mapping" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#CEEAD6;strokeColor=#1E8E3E;strokeWidth=2;fontSize=10;fontColor=#0D652D;" vertex="1" parent="1">
          <mxGeometry x="480" y="80" width="220" height="150" as="geometry"/>
        </mxCell>

        <!-- Stage 4: BiGRU -->
        <mxCell id="st4" value="&lt;b&gt;2-Layer Bidirectional GRU&lt;/b&gt;&lt;hr/&gt;Forward: h_fwd, Backward: h_bwd&lt;br/&gt;H_t = [h_fwd || h_bwd]&lt;br/&gt;H in R^{B x 50 x 256}&lt;br/&gt;Hidden Size D_gru=128" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF7E0;strokeColor=#F9AB00;strokeWidth=2;fontSize=10;fontColor=#B06000;" vertex="1" parent="1">
          <mxGeometry x="740" y="80" width="210" height="150" as="geometry"/>
        </mxCell>

        <!-- Stage 5: Attention & Sigmoid -->
        <mxCell id="st5" value="&lt;b&gt;Self-Attention &amp; Decision Head&lt;/b&gt;&lt;hr/&gt;Attention Weights: α_t = softmax(e_t)&lt;br/&gt;Context Vector: c = sum α_t H_t&lt;br/&gt;LayerNorm + Dropout(0.20)&lt;br/&gt;Final KAN Projection: 256 -&gt; 11&lt;br/&gt;Independent Sigmoids (τ=0.40)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE8E6;strokeColor=#D93025;strokeWidth=2;fontSize=10;fontColor=#C5221F;" vertex="1" parent="1">
          <mxGeometry x="990" y="80" width="230" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Flow Connectors -->
        <mxCell id="a1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="st1" target="st2"/>
        <mxCell id="a2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="st2" target="st3"/>
        <mxCell id="a3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="st3" target="st4"/>
        <mxCell id="a4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#5F6368;strokeWidth=2;" edge="1" parent="1" source="st4" target="st5"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open(os.path.join(PAPER_DIR, "fig4_kangru_architecture.drawio"), "w") as f:
    f.write(fig4_xml)

print("Generated 4 editable .drawio files in paper/ directory!")
