# Databricks notebook source
dbutils.fs.mkdirs("dbfs:/databricks/scripts/")

# COMMAND ----------

dbutils.fs.ls

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts"))

# COMMAND ----------

dbutils.fs.put("/databricks/scripts/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts/postgresql-install.sh"))

# COMMAND ----------

# MAGIC %sh
# MAGIC #!/bin/bash
# MAGIC wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar

# COMMAND ----------

# MAGIC %sh

# COMMAND ----------

pwd

# COMMAND ----------

ls

# COMMAND ----------

display(dbutils.fs.ls("dbfs"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/scripts"))

# COMMAND ----------

# MAGIC %sh 
# MAGIC dbfs cp postgresql-install.sh dbfs:/databricks/scripts/postgresql-install.sh

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/init"))

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/init/neha-test")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/init/"))

# COMMAND ----------

dbutils.fs.put("dbfs:/databricks/init/neha-test/my-echo.sh" ,"""
#!/bin/bash

echo "hello all" >> /hello.txt
""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/init/neha-test"))

# COMMAND ----------

clusterName = "PostgreSQL"

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/databricks/init/%s/"%clusterName)

# COMMAND ----------

# MAGIC %sh
# MAGIC dbutils.fs.put("/databricks/init/PostgreSQL/postgresql-install.sh","""
# MAGIC #!/bin/bash
# MAGIC wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar
# MAGIC wget --quiet -O /mnt/jars/driver-daemon/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

dbutils.fs.put("/databricks/init/PostgreSQL/postgresql-install.sh","""
#!/bin/bash
wget --quiet -O /mnt/driver-daemon/jars/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar
wget --quiet -O /mnt/jars/driver-daemon/postgresql-42.2.2.jar https://repo1.maven.org/maven2/org/postgresql/postgresql/42.2.2/postgresql-42.2.2.jar""", True)

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks/init/%s/postgresql-install.sh"%clusterName))

# COMMAND ----------

1+1

# COMMAND ----------

1+1
