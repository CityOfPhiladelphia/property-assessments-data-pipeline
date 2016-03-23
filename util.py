def construct_layout(cols):
  layout_items = []
  current_position = 0

  for col in cols:
    # If any chars were skipped, add a pad byte
    if col['start'] != current_position:
      skip_chars = col['start'] - current_position
      layout_items.append('{0}x'.format(skip_chars))

    size = col['end'] - col['start']
    format_char = col.get('format', 's')

    # If skip property is True, use the pad format character
    if col.get('skip') == True: format_char = 'x'

    layout_items.append('{0}{1}'.format(size, format_char))

    current_position = col['end']

  return ' '.join(layout_items)

# Gets header names, excluding those being skipped
def get_active_header(cols):
  return [col['name'] for col in cols if col.get('skip') != True]

def clean_date(input):
  if are_all_chars(input, '0'): return ''
  elif input[-2:] == '00': return '{0}-{1}'.format(input[:4], input[4:6])
  else: return '{0}-{1}-{2}'.format(input[:4], input[4:6], input[6:])

def are_all_chars(input, char):
  return input == len(input) * char