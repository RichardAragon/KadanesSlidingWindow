import collections
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class KadaneSlidingWindow:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.window = collections.deque()
        self.long_term_memory = []

    def add(self, elements):
        for element in elements:
            self.window.append(element)
            self.long_term_memory.append(element)
            if len(self.window) > self.maxlen:
                self.window.popleft()

    def get_context(self):
        return " ".join(self.window)

# Create a Kadane Sliding Window with a size of 1000 tokens
kadane_sliding_window = KadaneSlidingWindow(maxlen=1000)

# Initialize the Phi-1.5 model
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")

# Generate text with the Phi-1.5 model and the Kadane Sliding Window
prompt = "Once upon a time, there was a little girl named Alice who lived in a small village. One day, Alice was playing in the forest when she came across a strange rabbit hole. She followed the rabbit hole down into a wonderland..."

# Add the prompt to the sliding window before starting the loop
kadane_sliding_window.add(prompt.split())

generated_text = ""
while len(generated_text) < 100:
    context = kadane_sliding_window.get_context()

    # Ask the model a follow-up prompt
    follow_up_prompt = "After Alice fell down the rabbit hole, she..."
    context = follow_up_prompt + context

    # Encode the context using the tokenizer
    input_ids = tokenizer(context, return_tensors="pt").input_ids

    # Generate text using the model with the encoded context as input
    output_ids = model.generate(input_ids=input_ids, max_length=min(100, len(input_ids) + 75))

    # Decode the generated text using the tokenizer
    generated_text += tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Add the generated text to the sliding window
    kadane_sliding_window.add(generated_text.split())

# Print the generated text
print(generated_text)
