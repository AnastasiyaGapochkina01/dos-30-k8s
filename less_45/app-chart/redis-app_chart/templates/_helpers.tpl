{{- define "app-labels" -}}
app.name: {{ .Chart.Name }}
{{ include "app-selector-labels" . }}
{{- if .Chart.AppVersion }}
app.version: {{ .Chart.AppVersion | quote }}
{{- end }}
{{- end }}

{{- define "app-selector-labels" -}}
app.instance: {{ .Release.Name }}
{{- end }}

