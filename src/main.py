from pathlib import Path
from assessment import JobProfileBotTool
from cover_letter import CoverLetterBotTool

# Main entry point
if __name__ == "__main__":

    # job_profile_name = "Product Owner"
    # job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    # JobProfileBotTool(job_profile_name, job_profile_text).run()
    # CoverLetterBotTool(job_profile_name).run()
    #
    # job_profile_name = "Data Science Expert - NLP Focus"
    # job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    # JobProfileBotTool(job_profile_name, job_profile_text).run()
    # CoverLetterBotTool(job_profile_name).run()
    #
    # job_profile_name = "Data Engineer"
    # job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    # JobProfileBotTool(job_profile_name, job_profile_text).run()
    # CoverLetterBotTool(job_profile_name).run()
    #
    # job_profile_name = "Python Cloud Developer"
    # job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    # JobProfileBotTool(job_profile_name, job_profile_text).run()
    # CoverLetterBotTool(job_profile_name).run()
    #
    # job_profile_name = "Business Analyst"
    # job_profile_text = Path(f"assets/docs/input/Landing/{job_profile_name}.md").read_text()
    # JobProfileBotTool(job_profile_name, job_profile_text).run()
    # CoverLetterBotTool(job_profile_name).run()

    job_profile_name = "Product Owner Special"
    job_profile_text = """Sehr geehrter Herr Dr. Divine,

    Für unseren Kunden aus dem öffentlichen Sektor suchen wir einen erfahrenen Produkt Owner und/oder Teamleiter (m/w/d) im Bereich Container Plattformen mit fundiertem technischem Verständnis in Openshift, Kubernetes und Azure, zur Aufgaben- und Ressourcenplanung, Teamkoordination und Konfliktmanagement. Voraussetzungen sind Erfahrungen im Public Sektor, Wohnsitz in Deutschland, Bereitschaft zu Sicherheitsüberprüfungen (SÜ2) und gelegentlichen Dienstreisen sowie fließende Deutschkenntnisse.

    Wäre ich mit dieser Anfrage richtig bei ihnen?

    Allgemeine Informationen zum Einsatz:
    Start:                   ASAP
    Laufzeit:             Dezember 2025 (Option auf Verlängerung möglich)
    Auslastung:        Vollzeit – 40h/Woche
    Einsatzort:         95% Remote / vereinzelte Einsätze in Berlin o. a Stadt in Deutschland möglich
    Vertragsart:       Freelance

    Aufgabenbereich

    Aufgabenplanung und Ressourcenplanung
    Strukturiertes Vorgehen bei der Umsetzung von Projektanforderungen
    Koordination des Teams und aller Stakeholder
    Verantwortung für die fachliche Ausrichtung und Priorisierung von Themen
    Organisation, Moderation und Protokollierung von Meetings wie Daily Stand-ups und Refinement-Sessions
    Nachhalten einer offenen Punkte Liste 
    Konfliktmanagement innerhalb des Teams und Schutz der Mitarbeiter vor ungeordneten Anforderungen
    Steuerung und Support bei der Konzeption und Umsetzung technischer Lösungen

    Erforderliche Kenntnisse:
    Vorerfahrung als Produkt Owner und/oder Teamleiter
    Fundiertes technisches Verständnis von Openshift, Kubernetes und Azure
    Selbstständige Arbeitsweise und Bereitschaft, sich aktiv in neue Themen einzuarbeiten
    Fähigkeit, technische Lösungen zu beurteilen und bei der Umsetzung zu unterstützen
    Public Sektor Erfahrung
    Bereitschaft zur Überprüfung SÜ2
    Wohnsitz Deutschland
    Bereitschaft zu Dienstreisen (ca. 3 Tage alle 2 Monate)
    Deutsch fließend in Sprache und Schrift

    Haben Sie Kapazitäten frei?

    Dann melden Sie sich mit Ihrem aktuellen CV, Stundensatzvorstellung und Verfügbarkeit.

    Gerne können Sie mir auch schon vorab eine kurze Selbsteinschätzung mitgeben.



    Ich melde mich bei Ihnen zurück, sollte Ihre Bewerbung in Frage kommen, um die Position zu besprechen, bevor ich Sie vorstelle.
    Ich freue mich auf Ihre Rückmeldung!

    Mit freundlichen Grüßen
    Dennis Jovanovic
    Senior Candidate Consultant
    Phone: +49 89 55197840
    E-Mail: d.jovanovic@sthree.com"""
    JobProfileBotTool(job_profile_name, job_profile_text).run()
    CoverLetterBotTool(job_profile_name).run()

