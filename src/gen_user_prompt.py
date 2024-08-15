def gen_user_prompt(document, intent="Summarize the following text", tone="legal professional", length="three bullet points", focus=None, target_audience="lawyers", emphasis="sections affecting the overall outcome upon edit", customization=None):

  user_prompt = f"""
  <div>
  <p>{intent}:</p> 
  
  <p>{document}.</p>
  </div>
  
  <div>
  <p>Consider parameters strictly as below:</p>
  <p><strong>Parameters</strong>:</p>
  <ul>
    <li><strong>Tone</strong>: {tone}</li>
    <li><strong>Length</strong>: {length}</li>
    <li><strong>Focus</strong>: {focus}</li>
    <li><strong>Target audience</strong>: {target_audience}</li>
    <li><strong>Contextual emphasis</strong>: {emphasis}</li>
    <li><strong>Additional Customization</strong>: {customization}</li>
  </ul>
  </div>
  """
  return user_prompt