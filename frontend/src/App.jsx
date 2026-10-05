
import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [incidents, setIncidents] = useState([]);
  const [agents, setAgents] = useState([]);
  const [timeline, setTimeline] = useState([]);
  const [lastUpdated, setLastUpdated] = useState("");
  const [metrics, setMetrics] = useState({
    revenue_saved: 0,
    engineer_hours_saved: 0,
    success_rate: 0,
  });

  const loadData = () => {
    axios.get("https://safeshift-ai-tmrz.onrender.com/incidents")
      .then((response) => {
        const sorted = [...response.data].reverse();
        setIncidents(sorted);
      })
      .catch((error) => console.error(error));

    axios
      .get("https://safeshift-ai-tmrz.onrender.com")
      .then((response) => setAgents(response.data))
      .catch((error) => console.error(error));

    axios
      .get("https://safeshift-ai-tmrz.onrender.com")
      .then((response) => setMetrics(response.data))
      .catch((error) => console.error(error));

    axios
      .get("https://safeshift-ai-tmrz.onrender.com")
      .then((response) => {
        const sortedTimeline = [...response.data].reverse();
        setTimeline(sortedTimeline);
      })
      .catch((error) => console.error(error));

    setLastUpdated(new Date().toLocaleTimeString());
  };

  useEffect(() => {
    loadData();

    const interval = setInterval(() => {
      loadData();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const approveIncident = async (incidentId) => {
    try {
      await axios.put(
        `https://safeshift-ai-tmrz.onrender.com/${incidentId}/approve`
      );

      loadData();
    } catch (error) {
      console.error(error);
    }
  };

  const generateDemoIncident = async () => {
    try {
      await axios.post(
        "https://safeshift-ai-tmrz.onrender.com"
      );

      loadData();
    } catch (error) {
      console.error(error);
    }
  };

  const totalIncidents = incidents.length;

  const approvedIncidents = incidents.filter(
    (incident) => incident.status === "APPROVED"
  ).length;

  const criticalIncidents = incidents.filter(
    (incident) => incident.severity === "critical"
  ).length;
  const latestIncident =
    incidents.length > 0
      ? incidents[0]
      : null;

  return (
    <div className="dashboard-container">

      <div className="header">

        <div>
          <h1 className="dashboard-title">
            🚀 SafeShift AI
                      </h1>

          <p className="dashboard-subtitle">
            Autonomous AI Incident Response Platform
          </p>

          <p style={{ color: "#94a3b8" }}>
            Last Updated: {lastUpdated}
          </p>
        </div>

        <button
          className="generate-btn"
          onClick={generateDemoIncident}
        >
          🚨 Generate Critical Incident
        </button>

      </div>

      <div className="executive-grid">

        <div className="executive-card">
          <div className="executive-label">
            💰 Revenue Protected
          </div>

          <div className="executive-value">
            $
            {metrics.revenue_saved.toLocaleString()}
          </div>
        </div>

        <div className="executive-card">
          <div className="executive-label">
            ⏱ Engineer Hours Saved
          </div>

          <div className="executive-value">
            {metrics.engineer_hours_saved}
          </div>
        </div>

        <div className="executive-card">
          <div className="executive-label">
            🤖 AI Success Rate
          </div>

          <div className="executive-value">
            {metrics.success_rate}%
          </div>
        </div>

      </div>
      <div className="stats-grid">

        <div className="stat-card">
          <div className="stat-label">
            Total Incidents
          </div>
          <div className="stat-value">
            {totalIncidents}
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-label">
            Critical Incidents
          </div>
          <div className="stat-value">
            {criticalIncidents}
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-label">
            Approved Fixes
          </div>
          <div className="stat-value">
            {approvedIncidents}
          </div>
        </div>
        <div className="executive-grid">

          <div className="executive-card">
            <div className="executive-label">
              ⚡ Mean Time To Resolution
            </div>

            <div className="executive-value">
              4 min
            </div>
          </div>

          <div className="executive-card">
            <div className="executive-label">
              🛡 Services Protected
            </div>

            <div className="executive-value">
              4
            </div>
          </div>

          <div className="executive-card">
            <div className="executive-label">
              📈 AI Decisions Executed
            </div>

            <div className="executive-value">
              {approvedIncidents}
            </div>
          </div>

        </div>

      </div>
      {incidents.length > 0 && (
        <div className="summary-card">

          <h2>🚨 Current Critical Incident</h2>

          <p>
            <strong>Service:</strong>{" "}
            {latestIncident?.service}
          </p>

          <p>
            <strong>Priority:</strong>{" "}
            {latestIncident?.priority}
          </p>

          <p>
            <strong>Users Affected:</strong>{" "}
            {latestIncident?.users_affected}
          </p>

          <p>
            <strong>Revenue Risk:</strong>{" "}
            {latestIncident?.revenue_risk}
          </p>

          <p>
            <strong>AI Recommendation:</strong>{" "}
            {latestIncident?.deployment_recommendation}
          </p>

          <p>
            <strong>Status:</strong>{" "}
            {latestIncident?.status}
          </p>

          <h2 className="section-heading">
            🚨 Active Incidents
          </h2>

          <div className="incident-grid">

            {incidents.length === 0 ? (
              <div className="incident-card">
                No incidents found.
              </div>
            ) : (
              incidents.slice(0, 3).map((incident) => (

                <div
                  key={incident.id}
                  className="incident-card"
                >
                  

                  <div className="service-title">
                    #{incident.id} • {incident.service}
                  </div>

                  <div className="badge-row">

                    <div
                      className={
                        incident.severity === "critical"
                          ? "badge critical"
                          : "badge pending"
                      }
                    >
                      {incident.severity.toUpperCase()}
                    </div>

                    <div
                      className={
                        incident.status === "APPROVED"
                          ? "badge approved"
                          : "badge pending"
                      }
                    >
                      {incident.status}
                    </div>

                  </div>

                  <div className="info-row">
                    <strong>Exception:</strong> {incident.exception}
                  </div>

                  <div className="info-row">
                    <strong>Endpoint:</strong> {incident.endpoint}
                  </div>

                  <div className="section-title">
                    🧠 AI Root Cause
                  </div>

                  <p>{incident.root_cause}</p>

                  <div className="section-title">
                    🛠 AI Fix Suggestion
                  </div>

                  <p>{incident.fix_suggestion}</p>

                  <div className="info-row">
                    <strong>📊 Severity Score:</strong>{" "}
                    {incident.severity_score}/10
                  </div>

                  <div className="info-row">
                    <strong>🔥 Priority:</strong>{" "}
                    {incident.priority}
                  </div>

                  <div className="info-row">
                    <strong>👥 Customer Impact:</strong>{" "}
                    {incident.customer_impact}
                  </div>

                  <div className="info-row">
                    <strong>👤 Users Affected:</strong>{" "}
                    {incident.users_affected}
                  </div>

                  <div className="info-row">
                    <strong>💰 Revenue Risk:</strong>{" "}
                    {incident.revenue_risk}
                  </div>

                  <div className="info-row">
                    <strong>💸 Downtime Cost:</strong>{" "}
                    {incident.downtime_cost}
                  </div>

                  <div className="info-row">
                    <strong>⚠ Escalation Risk:</strong>{" "}
                    {incident.escalation_risk}
                  </div>

                  <div className="info-row">
                    <strong>🤖 AI Confidence:</strong>{" "}
                    {Math.min(
                      99,
                      85 + incident.severity_score
                    )}
                    %
                  </div>

                  <div className="section-title">
                    ❌ Broken Code
                  </div>

                  <pre className="old-code">
                    {incident.old_code}
                  </pre>

                  <div className="section-title">
                    ✅ AI Generated Patch
                  </div>

                  <pre className="new-code">
                    {incident.new_code}
                  </pre>

                  <div className="section-title">
                    🛡 AI Risk Analysis
                  </div>

                  <div className="risk-container">

                    <div
                      className={`risk-badge ${incident.risk_level === "HIGH"
                          ? "risk-high"
                          : incident.risk_level === "MEDIUM"
                            ? "risk-medium"
                            : "risk-low"
                        }`}
                    >
                      Risk: {incident.risk_level}
                    </div>

                    <p>
                      <strong>Confidence:</strong>{" "}
                      {incident.confidence}%
                    </p>

                    <p>
                      <strong>Recommendation:</strong>{" "}
                      {incident.deployment_recommendation}
                    </p>

                  </div>
                  <div className="section-title">
                    🧠 AI Decision Explanation
                  </div>

                  <div className="reasoning-box">

                    <p>
                      <strong>Selected Fix:</strong>
                      {" "}
                      {incident.fix_suggestion}
                    </p>

                    <p>
                      <strong>Alternative Considered:</strong>
                      {" "}
                      Exception Handling
                    </p>

                    <p>
                      <strong>Reason Chosen:</strong>
                      {" "}
                      Lowest deployment risk with highest probability of recovery.
                    </p>

                  </div>

                  <div className="section-title">
                    🤖 Multi-Agent Reasoning
                  </div>
                  <div className="reasoning-box">

                    <div className="reasoning-item">
                      <strong>👀 Observation</strong>
                      <p>{incident.observation}</p>
                    </div>

                    <div className="reasoning-item">
                      <strong>🔎 Analysis</strong>
                      <p>{incident.analysis}</p>
                    </div>

                    <div className="reasoning-item">
                      <strong>💡 Hypothesis</strong>
                      <p>{incident.hypothesis}</p>
                    </div>

                    <div className="reasoning-item">
                      <strong>🎯 AI Confidence</strong>
                      <p>{incident.ai_confidence}</p>
                    </div>

                  </div>
                  <div className="agent-reasoning-container">

                    {incident.agent_activity?.map((agent, index) => (
                      <div
                        key={index}
                        className="agent-step"
                      >
                        <div className="agent-name">
                          {agent.agent}
                        </div>

                        <div className="agent-status">
                          {agent.status}
                        </div>

                        <div className="agent-output">
                          {agent.output}
                        </div>
                      </div>
                    ))}

                  </div>

                  <div className="section-title">
                    🤖 AI Recovery Plan
                  </div>

                  <ol>
                    {incident.recovery_plan?.map(
                      (step, index) => (
                        <li key={index}>{step}</li>
                      )
                    )}
                  </ol>

                  <div className="section-title">
                    🔍 Investigation Trail
                  </div>

                  <p>
                    ✓ Error Detected
                    <br />
                    ✓ Root Cause Identified
                    <br />
                    ✓ Fix Generated
                    <br />
                    ✓ Awaiting Approval
                  </p>
                  {incident.deployment_steps?.length > 0 && (
                    <>
                      <div className="section-title">
                        🚀 Deployment Simulation
                      </div>

                      <div className="deployment-container">

                        {incident.deployment_steps.map(
                          (step, index) => (
                            <div
                              key={index}
                              className="deployment-step"
                            >
                              ✅ {step.step} - {step.status}
                            </div>
                          )
                        )}

                      </div>
                    </>
                  )}

                  {incident.status === "APPROVED" ? (
                    <button
                      className="approve-btn"
                      disabled
                    >
                      ✅ Approved
                    </button>
                  ) : (
                    <button
                      className="approve-btn"
                      onClick={() =>
                        approveIncident(incident.id)
                      }
                    >
                      Approve Fix
                    </button>
                  )}

                </div>
              ))
            )}

          </div>

          <h2 className="section-heading">
            📚 Incident History
          </h2>

          <div className="history-container">

            {incidents.slice(3).map((incident) => (

              <div
                key={incident.id}
                className="history-row"
              >
                <strong>#{incident.id}</strong> • {incident.service}
                • {incident.exception}
                • {incident.status}
              </div>

            ))}

          </div>

          <h2 className="section-heading">
            🤖 Agent Activity
          </h2>

          <div className="agent-grid">

            {agents.map((agent, index) => (
              <div
                key={index}
                className="agent-card"
              >
                <h3>{agent.agent}</h3>

                <p>
                  Status:
                  <strong> {agent.status}</strong>
                </p>
              </div>
            ))}

          </div>

          <h2 className="section-heading">
            📅 Incident Timeline
          </h2>

          <div className="timeline-container">

            {timeline.map((item, index) => (
              <div
                key={index}
                className="timeline-item"
              >
                <div className="timeline-dot"></div>

                <div>
                  <strong>{item.time}</strong>
                  {" - "}
                  {item.event}
                </div>
              </div>
            ))}

          </div>

        </div>
      )}
      </div>
  );
}

      export default App;