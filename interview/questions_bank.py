"""
Curated Offline Question Bank across technical and behavioral domains.
Used for zero-crash fallback when Gemini API is unavailable or offline.
"""

QUESTION_BANK = {
    "Python Developer": {
        "Junior": [
            "Explain the difference between a list and a tuple in Python, and when you would prefer using a tuple.",
            "How does Python's memory management work, and what is the role of the garbage collector?",
            "What are Python decorators, and how would you write a simple decorator to measure execution time?",
            "Explain the purpose of the `*args` and `**kwargs` syntax in Python functions.",
            "What is the difference between shallow copy and deep copy in Python?"
        ],
        "Mid-Level": [
            "Explain the Python Global Interpreter Lock (GIL) and its implications on multi-threading vs multi-processing.",
            "How do Python generators work internally, and what is the memory advantage of using `yield` over returning a list?",
            "Describe the method resolution order (MRO) in Python when dealing with multiple inheritance and C3 linearization.",
            "How would you optimize a Python application that is experiencing slow database I/O and CPU bottlenecks?",
            "Explain context managers and how you would implement one using both a class (`__enter__`, `__exit__`) and `contextlib`."
        ],
        "Senior": [
            "Design a distributed task queue system in Python (similar to Celery). How would you handle task acknowledgment, retries, and worker concurrency?",
            "Explain how Python's `asyncio` event loop works under the hood. How does cooperative multitasking differ from OS-level threading?",
            "How would you profile, diagnose, and fix a memory leak in a production FastAPI or Django service?",
            "Discuss metaprogramming in Python using metaclasses. When is it appropriate to use `__init_subclass__` instead of a full metaclass?",
            "How would you architect a Python microservices system to handle 50,000 requests per second with high availability and fault tolerance?"
        ]
    },
    "Machine Learning Engineer": {
        "Junior": [
            "Explain the bias-variance tradeoff and how it impacts model generalization.",
            "What is the difference between precision, recall, and F1-score? When would you optimize for recall over precision?",
            "Describe the concept of cross-validation and why it is crucial during model evaluation.",
            "What is overfitting in machine learning, and what are three distinct techniques to prevent it?",
            "Explain the difference between supervised, unsupervised, and reinforcement learning with real-world examples."
        ],
        "Mid-Level": [
            "How do Transformer architectures (self-attention mechanism) overcome the limitations of recurrent neural networks (RNNs)?",
            "Explain gradient descent optimization algorithms: how do Adam and RMSprop improve upon standard Stochastic Gradient Descent?",
            "How would you handle severe class imbalance in a fraud detection dataset containing 99.8% negative and 0.2% positive samples?",
            "Describe the steps to deploy a PyTorch or TensorFlow model as a low-latency inference endpoint in production.",
            "What is feature drift (data drift) vs concept drift, and how do you monitor and remediate them in MLOps pipelines?"
        ],
        "Senior": [
            "Architect an end-to-end real-time recommendation system serving 10M active users with sub-50ms latency. What are your candidate retrieval and ranking stages?",
            "How would you implement and fine-tune a Large Language Model (LLM) using LoRA / QLoRA under tight GPU memory constraints?",
            "Design a feature store architecture for real-time online inference and batch offline model training ensuring point-in-time correctness.",
            "How would you evaluate hallucination and safety in production generative AI pipelines using automated benchmarks and guardrails?",
            "Explain the mathematical intuition behind Quantization (INT8 / FP4) and KV-caching in LLM inference acceleration."
        ]
    },
    "Data Analyst": {
        "Junior": [
            "What is the difference between `WHERE` and `HAVING` clauses in SQL?",
            "Explain the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.",
            "How do you identify and handle missing or corrupted values in a Pandas DataFrame?",
            "What is the difference between mean, median, and mode, and which would you use for skewed income data?",
            "Explain what a correlation coefficient indicates and why correlation does not imply causation."
        ],
        "Mid-Level": [
            "Explain SQL window functions such as `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, and `LEAD()` with practical examples.",
            "How do you design an executive KPI dashboard in Tableau/PowerBI that balances high-level metrics with actionable drill-down capabilities?",
            "Describe how you would perform an A/B test analysis to determine if a new landing page conversion rate is statistically significant.",
            "How would you write an optimized SQL query to calculate customer cohort retention rates over a 12-month period?",
            "What data visualization pitfalls do you actively avoid when presenting technical metrics to non-technical stakeholders?"
        ],
        "Senior": [
            "How would you structure a modern data stack (ingestion, dbt modeling, data warehousing, BI) from scratch for a high-growth startup?",
            "Design a data governance framework ensuring data quality, lineage, and GDPR/CCPA compliance across cross-functional data pipelines.",
            "How do you handle metric discrepancies between marketing ad platform reports and internal transactional databases?",
            "Explain how you would conduct causal inference analysis when running a randomized controlled trial (A/B test) is not feasible.",
            "How do you mentor junior analysts to formulate hypothesis-driven business questions rather than just running ad-hoc queries?"
        ]
    },
    "Frontend Developer": {
        "Junior": [
            "What is the difference between `var`, `let`, and `const` in JavaScript, and how does hoisting affect them?",
            "Explain the concept of the Virtual DOM in React and how reconciliation works.",
            "How does CSS Flexbox differ from CSS Grid, and when should you choose one over the other?",
            "What are React hooks, and what are the rules governing their usage?",
            "Explain what responsive web design is and how media queries work."
        ],
        "Mid-Level": [
            "Explain the JavaScript Event Loop, microtask queue, and macrotask queue. In what order do `setTimeout` and `Promise.then` execute?",
            "How do you optimize core web vitals (LCP, FID/INP, CLS) on a content-heavy web application?",
            "Compare client-side rendering (CSR), server-side rendering (SSR), and static site generation (SSG) in Next.js.",
            "How would you manage shared state across complex component hierarchies? Compare React Context vs Redux/Zustand.",
            "How do you prevent unnecessary re-renders in React using `useMemo`, `useCallback`, and `React.memo`?"
        ],
        "Senior": [
            "Architect a scalable Micro-Frontend application for an enterprise suite. How do you handle routing, state sharing, and independent deployments?",
            "Design an accessible, WCAG 2.1 AA compliant Design System component library from scratch with themeable tokens.",
            "How do you implement offline-first capabilities using Service Workers, Cache API, and IndexedDB in Progressive Web Apps?",
            "How would you establish automated frontend testing combining unit tests (Jest/Vitest), component tests (Testing Library), and E2E (Playwright)?",
            "Explain how you would diagnose and eliminate JavaScript memory leaks caused by uncleaned event listeners and closures."
        ]
    },
    "Full Stack Developer": {
        "Junior": [
            "Explain how client-server architecture works from the moment a user types a URL into a browser.",
            "What is RESTful API design, and what are the primary HTTP methods and their standard status codes?",
            "What is the difference between SQL and NoSQL databases, and when would you select each?",
            "Explain Cross-Origin Resource Sharing (CORS) and how you resolve CORS errors between frontend and backend.",
            "How do you store passwords securely in a database?"
        ],
        "Mid-Level": [
            "How do JWT (JSON Web Tokens) work for authentication? Explain token expiration, refresh tokens, and CSRF vs XSS attack vectors.",
            "Design a database schema for an e-commerce platform handling users, products, orders, and inventory with ACID compliance.",
            "How do you implement rate limiting on API endpoints to defend against abuse and DDoS attacks?",
            "Describe the differences between WebSockets, Server-Sent Events (SSE), and long-polling for real-time bidirectional communication.",
            "How do you configure CI/CD pipelines using Docker containers to achieve automated testing and zero-downtime deployment?"
        ],
        "Senior": [
            "Design a URL shortening service (like Bitly) to handle 100M new URLs per month with low latency read access and 99.99% availability.",
            "How do you implement distributed caching using Redis or Memcached? How do you prevent cache stampede, cache penetration, and cache breakdown?",
            "Describe how you would transition a monolithic web application to microservices without interrupting ongoing business operations.",
            "How do you handle database sharding, read replicas, and write conflicts in high-throughput transactional systems?",
            "Architect an asynchronous event-driven system using message brokers (Kafka / RabbitMQ) with idempotency and dead-letter queues."
        ]
    },
    "HR & Behavioral": {
        "Junior": [
            "Tell me about yourself and what sparked your passion for technology and software engineering.",
            "Describe a challenging project you worked on recently. What obstacles did you encounter and how did you resolve them?",
            "How do you handle constructive criticism or code review feedback from teammates?",
            "Tell me about a time you had to learn a new programming language or tool quickly to finish a task.",
            "Where do you see your technical career developing over the next two to three years?"
        ],
        "Mid-Level": [
            "Describe a situation where you had a strong technical disagreement with a colleague or lead. How did you handle it and what was the outcome?",
            "Tell me about a time a production bug occurred on your watch. How did you triage, resolve, and post-mortem the incident?",
            "How do you prioritize competing deadlines and balance engineering excellence (refactoring) with business delivery speed?",
            "Describe a time you mentored a junior engineer or helped onboard a new team member effectively.",
            "Give an example of a situation where project requirements were ambiguous. How did you gain clarity and drive progress?"
        ],
        "Senior": [
            "How do you foster a culture of engineering quality, psychological safety, and continuous learning within your engineering team?",
            "Tell me about a time you had to influence senior leadership or product managers to invest in technical debt reduction over new features.",
            "Describe a situation where a critical initiative was failing or severely delayed. How did you step in to turn it around?",
            "How do you approach hiring, evaluating technical candidates, and building diverse, high-performing engineering teams?",
            "Discuss a major architectural decision you made that did not turn out as expected. What did you learn and how did you adapt?"
        ]
    }
}

def get_fallback_question(role: str, difficulty: str, question_idx: int) -> str:
    """Return a high-quality question from the fallback bank."""
    role_dict = QUESTION_BANK.get(role, QUESTION_BANK["Python Developer"])
    diff_list = role_dict.get(difficulty, role_dict.get("Mid-Level", []))
    idx = (question_idx - 1) % len(diff_list)
    return diff_list[idx]
