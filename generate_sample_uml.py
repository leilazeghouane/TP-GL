# -*- coding: utf-8 -*-
"""
Generate the exact UML diagram matching the user's sample report:
- Blue for Builder (StudentAccount.Builder and StudentAccount)
- Green for Singleton (AccountRepository and AuditLogger)
- Orange for Prototype (AccountTemplate / Prototype)
- Top Main class
- Legend at top-left
"""

uml_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 440" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Tahoma, Arial, sans-serif;">
    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#2d3748"/>
        </marker>
        <marker id="dashArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#4a5568"/>
        </marker>
    </defs>

    <!-- Legend Box (Top Left) -->
    <rect x="235" y="10" width="65" height="52" fill="#ffffff" stroke="#2d3748" stroke-width="1"/>
    <rect x="235" y="10" width="65" height="13" fill="#edf2f7"/>
    <text x="267" y="19" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#2d3748">Légende</text>
    <rect x="237" y="24" width="61" height="12" fill="#bee3f8"/>
    <text x="267" y="33" text-anchor="middle" font-size="7" fill="#1a365d">Builder</text>
    <rect x="237" y="37" width="61" height="12" fill="#c6f6d5"/>
    <text x="267" y="46" text-anchor="middle" font-size="7" fill="#22543d">Singleton</text>
    <rect x="237" y="50" width="61" height="11" fill="#feebc8"/>
    <text x="267" y="58" text-anchor="middle" font-size="7" fill="#744210">Prototype</text>

    <!-- Main Class (Top Center) -->
    <rect x="315" y="15" width="115" height="36" fill="#ffffff" stroke="#2d3748" stroke-width="1.2"/>
    <text x="372" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="#1a202c">Main</text>
    <line x1="315" y1="31" x2="430" y2="31" stroke="#cbd5e0"/>
    <text x="320" y="44" font-size="7.5" font-family="monospace" fill="#2d3748">+ main(String[]): void</text>

    <!-- AccountTemplate (Orange Prototype Box - Left) -->
    <rect x="40" y="110" width="160" height="98" fill="#feebc8" stroke="#dd6b20" stroke-width="1.2"/>
    <text x="120" y="121" text-anchor="middle" font-size="7.5" fill="#744210">&lt;&lt;Prototype&gt;&gt;</text>
    <text x="120" y="132" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#744210">AccountTemplate</text>
    <line x1="40" y1="136" x2="200" y2="136" stroke="#fbd38d"/>
    <text x="45" y="146" font-size="7" font-family="monospace" fill="#2d3748">- level : String</text>
    <text x="45" y="156" font-size="7" font-family="monospace" fill="#2d3748">- major : String</text>
    <text x="45" y="166" font-size="7" font-family="monospace" fill="#2d3748">- scholarship : boolean</text>
    <text x="45" y="176" font-size="7" font-family="monospace" fill="#2d3748">- courses : List&lt;String&gt;</text>
    <line x1="40" y1="180" x2="200" y2="180" stroke="#fbd38d"/>
    <text x="45" y="191" font-size="7" font-family="monospace" fill="#744210">+ clone() : StudentAccount</text>
    <text x="45" y="202" font-size="6.8" font-family="monospace" fill="#744210">+ createAccount(id, name, email)</text>

    <!-- StudentAccount.Builder (Blue Box - Center Top) -->
    <rect x="305" y="85" width="155" height="150" fill="#bee3f8" stroke="#3182ce" stroke-width="1.2"/>
    <text x="382" y="96" text-anchor="middle" font-size="7.5" fill="#2b6cb0">&lt;&lt;Builder&gt;&gt;</text>
    <text x="382" y="107" text-anchor="middle" font-size="9" font-weight="bold" fill="#1a365d">StudentAccount.Builder</text>
    <line x1="305" y1="111" x2="460" y2="111" stroke="#90cdf4"/>
    <text x="310" y="120" font-size="6.8" font-family="monospace" fill="#2d3748">- id, fullName, email : String {obligatoires}</text>
    <text x="310" y="129" font-size="6.8" font-family="monospace" fill="#2d3748">- phone, level, major : String</text>
    <text x="310" y="138" font-size="6.8" font-family="monospace" fill="#2d3748">- scholarship : boolean</text>
    <text x="310" y="147" font-size="6.8" font-family="monospace" fill="#2d3748">- courses : List&lt;String&gt;</text>
    <line x1="305" y1="151" x2="460" y2="151" stroke="#90cdf4"/>
    <text x="310" y="160" font-size="6.8" font-family="monospace" fill="#2b6cb0">+ Builder(id, fullName, email)</text>
    <text x="310" y="170" font-size="6.8" font-family="monospace" fill="#2d3748">+ phone(String) : Builder</text>
    <text x="310" y="180" font-size="6.8" font-family="monospace" fill="#2d3748">+ level(String) : Builder</text>
    <text x="310" y="190" font-size="6.8" font-family="monospace" fill="#2d3748">+ major(String) : Builder</text>
    <text x="310" y="200" font-size="6.8" font-family="monospace" fill="#2d3748">+ scholarship(boolean) : Builder</text>
    <text x="310" y="210" font-size="6.8" font-family="monospace" fill="#2d3748">+ addCourse(String) : Builder</text>
    <text x="310" y="224" font-size="7" font-family="monospace" font-weight="bold" fill="#2b6cb0">+ build() : StudentAccount [validation]</text>

    <!-- StudentAccount (Blue Product Box - Center Bottom) -->
    <rect x="315" y="260" width="135" height="120" fill="#bee3f8" stroke="#3182ce" stroke-width="1.2"/>
    <text x="382" y="271" text-anchor="middle" font-size="7.5" fill="#2b6cb0">&lt;&lt;Product&gt;&gt;</text>
    <text x="382" y="282" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#1a365d">StudentAccount</text>
    <line x1="315" y1="286" x2="450" y2="286" stroke="#90cdf4"/>
    <text x="320" y="296" font-size="6.8" font-family="monospace" fill="#2d3748">- id : String {final}</text>
    <text x="320" y="306" font-size="6.8" font-family="monospace" fill="#2d3748">- fullName : String</text>
    <text x="320" y="316" font-size="6.8" font-family="monospace" fill="#2d3748">- email : String</text>
    <text x="320" y="326" font-size="6.8" font-family="monospace" fill="#2d3748">- phone : String = null</text>
    <text x="320" y="336" font-size="6.8" font-family="monospace" fill="#2d3748">- level : String = "L1"</text>
    <text x="320" y="346" font-size="6.8" font-family="monospace" fill="#2d3748">- scholarship : boolean = false</text>
    <text x="320" y="356" font-size="6.8" font-family="monospace" fill="#2d3748">- courses : List&lt;String&gt;</text>
    <line x1="315" y1="360" x2="450" y2="360" stroke="#90cdf4"/>
    <text x="320" y="371" font-size="6.8" font-family="monospace" fill="#2d3748">- StudentAccount(Builder) [private]</text>

    <!-- AccountRepository (Green Box - Bottom Left) -->
    <rect x="110" y="265" width="165" height="105" fill="#c6f6d5" stroke="#38a169" stroke-width="1.2"/>
    <text x="192" y="276" text-anchor="middle" font-size="7.5" fill="#22543d">&lt;&lt;Singleton&gt;&gt;</text>
    <text x="192" y="287" text-anchor="middle" font-size="9" font-weight="bold" fill="#22543d">AccountRepository</text>
    <line x1="110" y1="291" x2="275" y2="291" stroke="#9ae6b4"/>
    <text x="115" y="301" font-size="6.8" font-family="monospace" fill="#2d3748">- accounts : Map&lt;String, StudentAccount&gt;</text>
    <text x="115" y="311" font-size="6.8" font-family="monospace" fill="#2d3748">- Holder.INSTANCE : AccountRepository {static}</text>
    <line x1="110" y1="315" x2="275" y2="315" stroke="#9ae6b4"/>
    <text x="115" y="325" font-size="6.8" font-family="monospace" fill="#2d3748">- AccountRepository() [private]</text>
    <text x="115" y="336" font-size="6.8" font-family="monospace" fill="#22543d">+ getInstance() : AccountRepository {static}</text>
    <text x="115" y="347" font-size="6.8" font-family="monospace" fill="#2d3748">+ add(StudentAccount) : void</text>
    <text x="115" y="357" font-size="6.8" font-family="monospace" fill="#2d3748">+ findById(String) : Optional</text>
    <text x="115" y="367" font-size="6.8" font-family="monospace" fill="#2d3748">+ findAll() : List | count() : int</text>

    <!-- AuditLogger (Green Box - Bottom Right) -->
    <rect x="490" y="265" width="150" height="90" fill="#c6f6d5" stroke="#38a169" stroke-width="1.2"/>
    <text x="565" y="276" text-anchor="middle" font-size="7.5" fill="#22543d">&lt;&lt;Singleton&gt;&gt;</text>
    <text x="565" y="287" text-anchor="middle" font-size="9" font-weight="bold" fill="#22543d">AuditLogger</text>
    <line x1="490" y1="291" x2="640" y2="291" stroke="#9ae6b4"/>
    <text x="495" y="301" font-size="6.8" font-family="monospace" fill="#2d3748">- memoryLogs : List&lt;String&gt;</text>
    <text x="495" y="311" font-size="6.8" font-family="monospace" fill="#2d3748">- Holder.INSTANCE : AuditLogger {static}</text>
    <line x1="490" y1="315" x2="640" y2="315" stroke="#9ae6b4"/>
    <text x="495" y="325" font-size="6.8" font-family="monospace" fill="#2d3748">- AuditLogger() [private]</text>
    <text x="495" y="336" font-size="6.8" font-family="monospace" fill="#22543d">+ getInstance() : AuditLogger {static}</text>
    <text x="495" y="347" font-size="6.8" font-family="monospace" fill="#2d3748">+ log(String) : void</text>

    <!-- Connectors -->
    <!-- Main -> AccountTemplate -->
    <path d="M 325 51 L 180 110" stroke="#4a5568" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#dashArrow)"/>
    <text x="235" y="75" font-size="7" fill="#4a5568">utilise</text>

    <!-- Main -> Builder -->
    <path d="M 372 51 L 372 83" stroke="#4a5568" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#dashArrow)"/>
    <text x="376" y="70" font-size="7" fill="#4a5568">utilise</text>

    <!-- Main -> AuditLogger -->
    <path d="M 425 51 L 565 263" stroke="#4a5568" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#dashArrow)"/>

    <!-- AccountTemplate -> StudentAccount -->
    <path d="M 200 155 L 315 285" stroke="#dd6b20" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#dashArrow)"/>
    <text x="245" y="215" font-size="7" fill="#744210">createAccount() utilise</text>

    <!-- Builder -> StudentAccount -->
    <path d="M 382 235 L 382 258" stroke="#3182ce" stroke-width="1.2" marker-end="url(#arrow)"/>
    <text x="390" y="248" font-size="7" fill="#2b6cb0">&lt;&lt;create&gt;&gt; build()</text>

    <!-- AccountRepository -> StudentAccount -->
    <path d="M 275 315 L 313 315" stroke="#38a169" stroke-width="1.2" marker-end="url(#arrow)"/>
    <text x="290" y="310" font-size="7" fill="#22543d">0..*</text>
</svg>
"""

with open(r"c:\Users\PC\Desktop\Tp GL\docs\images\sample_uml_diagram.svg", "w", encoding="utf-8") as f:
    f.write(uml_svg)

print("Generated sample_uml_diagram.svg successfully!")
