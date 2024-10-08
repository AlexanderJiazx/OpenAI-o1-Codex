# OpenAI o1 Codex

<img width="1105" alt="Screenshot 2024-09-18 at 12 15 00 AM" src="https://github.com/user-attachments/assets/b523f79b-8df2-4516-81e6-2a1afac0f6b0">

OpenAI o1 Codex is a simple interface for o1 models using OpenRouter API


---

**Install the dependencies**:
   
   Run the following command to install all necessary packages:

   ```bash
   pip install Flask MarkupSafe openai markdown
   ```

**Setup API key**

   [Get your OpenRouter API key](https://openrouter.ai/settings/keys)

   Set as system variables

   ```bash
export OPENROUTER_API_KEY='Your_API_KEY'
```




Run main.py


Enter http://localhost:912/ in browser


---

**Note:**

- The default model is set to `o1-mini`, but you can change it to others based on your preferences.
- To modify the output tone and format, adjust the `additional_prompt` variable.

---
