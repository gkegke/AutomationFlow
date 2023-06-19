

```code
test = "bob"
```

```markdown
# hi ${test}
```

```markdown="header2"
## header2
```

{? block 'header2' ?}

{#

  Console progress bar

#}

```text
# example 1 {{ yellow | name }}

{{ pause }}

```

```code
n = get_input()
print()
```

%% progress_bar | n %%

%% print_green | "Completed" %%

%% print_yellow | "done" %%

%% pause %%

```text="hi_message"
say hi
```

{? block 'hi_message' ?}

```code
print("start")

name = 'tim'
test1 = 12*35
test2 = int(12)

print("end")
```

```text
name = ${name}
test1 = ${test1}
```

```text="hi_message"
say hi
```

{? block hi_message ?}

```text="bye_message"
bye
```

```code="switch_a"
a = 'tom'
print(a)
```

{% if False %}

{? block 'hi_message' ?}

```text
fk you
```

{% elif True %}

{? block 'switch_a' ?}

```text
or not
```

   {% if True %}

```text
1234123413
```

   {% else %}
  
```text
ASDGASDGASDGASDG
```

   {% endif %}

{% else %}

```text
fk you
```

{% endif %}

%% pause %%

{? script 'script2.md' ?}

```text
# Example 3

hi ${name}. ${name} is a variable referenced by "${name}".
```

```text
I changed the name variable's value to ${name} in the external script.

hi

kjhlkjhlkj

test2: ${test2}
```

%% pause %%

%% print_yellow | '# Progress bar example' %%

## Starting new task in

%% countdown | 2 %%

%% print_green | 'started.' %%

{# Extra comment, maybe explaining what $n is meant to do #}

```code
n = get_input()
```

%% progress_bar | n %%

%% print_green | "Completed" %%

%% print_yellow | "Bye!" %%
