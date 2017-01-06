def to_logstash(arg, indent=4, oneline=False):
  if isinstance(arg, dict):
    lines = []
    for k,v in arg.iteritems():
      if isinstance(v, dict):
        fragment = '%s => { %s }' % (k, to_logstash(v, oneline=True))
      else:
        fragment = '%s => %s' % (k, to_logstash(v, oneline=True))
      lines.append(fragment)

    if oneline:
      prefix = ' '
    else:
      prefix = '\n' + (' ' * indent)
    out = prefix.join(lines)
  elif hasattr(arg, '__iter__'):
    out = '[ %s ]' % ', '.join([ to_logstash(i, oneline=True) for i in arg])
  else:
    out = arg

  return out


class FilterModule(object):
  def filters(self):
    return {'to_logstash': to_logstash}
