{{- define "blog.name" -}}
downhill
{{- end -}}

{{- define "blog.labesl" -}}
app.name: {{ include "blog.name" . }}
app.instance: {{ .Release.Name }}
{{- end -}}