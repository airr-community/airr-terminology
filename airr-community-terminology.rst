==========================
AIRR Community Terminology
==========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Definitions
===========

AIRR Community
--------------

*  Adaptive Immune Receptor Repertoire (AIRR) [restricted]_: A
   collection of vertebrate immune receptors whose loci typically
   undergo RAG-mediated rearrangement, i.e., immunoglobulins and T cell
   receptors.
*  AIRR Community (AIRR-C) [restricted]_: The Adaptive Immune Receptor
   Repertoire Community is a grassroots collaboration for developing and
   promoting best practices for generating, analyzing, curating, and
   sharing AIRR-seq data, see [DOI:10.3389/fimmu.2017.01418]. As of
   12/2017, AIRR-C became a Committee within The Antibody Society (TAbS)
   and is therefore also known as "The AIRR Community Committee within
   The Antibody Society".
*  AIRR Community Leadership (AIRR-C Leadership): The group of persons
   who serve as either members of the AIRR Community Executive SC and/or
   co-leads of any other AIRR Community WG or SC.
*  AIRR Community Meeting (AIRR-C Meeting): The official meeting of the
   AIRR Community at which the General Assembly convenes. These meetings
   are held approximately every 18 months.
*  AIRR Community Member (AIRR-C Member): An individual whose AIRR
   Community membership application has been approved and has not been
   terminated and who is not in arrears with his/her annual membership
   fee.
*  AIRR Community Standards (AIRR-C Standards) *(previously: AIRR
   Standards)* [restricted]_: The collection of all norms, including
   standards, guidelines, best practices, recommendations and
   definitions, which have been developed and published by the AIRR
   Community, in their respective current version.
*  AIRR Data Commons (ADC) [restricted]_: The network of data
   repositories, which make AIRR-seq data FAIR by implementing the ADC
   API, adhering to the MiAIRR metadata standard and provide data in an
   AIRR Format.
*  AIRR Data Commons Application Program Interface (ADC API)
   [restricted]_: The standard defining how AIRR-seq data located in a
   repository can be programmatically searched and retrieved.
*  AIRR Data Schema [restricted]_: The formal definition of all
   specified properties of an AIRR-seq study. This includes groupings of
   properties, relations between properties and the permissible
   representations of property values.
*  AIRR Formats *(previously: AIRR Data Representation)* [restricted]_:
   The collection of definitions of on-disk and/or in-transit
   representation of the entities specified in the AIRR Data Schema and
   in MiAIRR.
*  AIRR Sequencing (AIRR-seq): The experimental observation of an
   Adaptive Immune Receptor Repertoire by means of nucleic acid
   sequencing.
*  Interval: The period between two consecutive AIRR Community Meetings.
*  MiAIRR [restricted]_: The acronym for “Minimal Information about an
   Adaptive Immune Receptor Repertoire study”, the AIRR
   Community-defined set of properties on which information must or
   should be provided to allow for the meaningful interpretation of the
   data. MiAIRR was originally specified in [`DOI:10.1038/ni.3873`_] and
   continues to be further developed in AIRR Community Git repository
   [https://github.com/airr-community/airr-standards]. It should be
   noted that the current version of MiAIRR is a complete subset of the
   AIRR Data Schema definitions.
*  Sub-committee (SC): A formally established group within the AIRR
   Community to address continuous or repetitive duties of high
   organizational relevance to the AIRR Community. Sub-committees
   consist of one or more Co-Leaders and additional individuals, all of
   whom are required to be AIRR Community Members.
*  Working Group (WG): A formally established group within the AIRR
   Community, which has received a mandate from the General Assembly to
   work on a specified topic on behalf of the AIRR Community.
   Participation in working groups is open to all interested
   individuals, an AIRR Community membership is not required. Working
   groups are chaired by one or more (Co)-leaders, at least one of which
   is required to be an AIRR Community Member. Working groups focus on a
   set of specified goals and will be disbanded when these goals are
   accomplished.
*  Working Group Participant (WG Participant): An individual who
   regularly attends WG conference calls, contributes ideas or other
   information to the WG and takes part in the generation of working
   group products. Participant status is independent of AIRR Community
   Membership. The determination of which individuals of a WG are
   considered to be Participants is made by the WG (Co-)leads in
   consultation with other Participants of the WG. Subscription to a
   WG's mailing list is typically not a sufficient criterion to be
   considered as a Participant.


Biology
-------

*  Antibody (Ab): A soluble protein consisting of *n* Ig heavy / Ig
   light heterotetramers (with *n* typically being 1, 2 or 5, depending
   on the isotype) plus the optional J chain (IgM & IgA) and the
   secretory component (IgA).
*  B cell receptor (BCR): A protein complex on the cell surface
   encompassing Ig heavy / Ig light heterotetramers and the associated
   signal transduction components (e.g., Igα and Igβ).
*  Clonal expansion: The proliferation of an individual T or B cell that
   gives rise to a Clone.
*  Clonal lineage: See Clone.
*  Complementarity determining region (CDR): The complementarity
   determining regions of an Ig or TCR are the protein loops that are
   mainly responsible for the interaction with an antigen. There are
   three CDRs in total (CDR1-3) of which CDR3 is encoded by the junction
   of the V(D)J rearrangement.
*  Constant region (C region): The constant region of IG or TR genes.
   For IGH, multiple C regions exist, which encode different isotypes,
   e.g., IgD, IgG1, IgA2.
*  Framework region (FWR, FR): The framework regions of an Ig or TCR,
   which generally correspond to the beta strands forming the core of
   the variable domain.
*  Immunoglobulin (Ig, IG): Can refer to the locus, rearranged gene,
   transcript, polypeptide or as an umbrella term also to BCRs and
   antibodies. Note that while "Ig" is a general abbreviation, "IG"
   specifically refers to the nucleic acids that encode any of the
   Ig chains.
*  Public clone: A set of rearrangements from multiple individuals all
   using the same V and J genes and having high sequence identity in
   CDR3. Technically they are convergent rearrangements rather than a
   true clone. Suggestive of functional selection.
*  T cell receptor (TCR): A protein complex on the cell surface
   encompassing the TCRα/β or TCRγ/δ heterodimers and the CD3 signal
   transduction components.
*  TR: The nucleic acids that encode any of the TCR chains.
*  Unique molecular identifier (UMI): A stretch of random or semi-random
   nucleotides used to uniquely label each original molecule input into
   a PCR reaction. Sequences with the same UMI can be collapsed to allow
   sequencing error correction and quantification.
*  V(D)J: The genetic makeup of a rearranged IG or TR. All loci include
   variable (V) and joining (J) genes; in addition, the IGH, TRB, and
   TRD loci also include diversity (D) genes.


mixed (Bio/IT)
--------------

*  Clone: Multiple definitions:

   1. [biology] A group of B or T cells that are all descended from the
      same naive ancestal cell and carry the same rearrangements. In B
      cells, the Ig sequence may vary between members of a Clone due to
      somatic hypermutation. To indicate this fact, the term "clonal
      linage" is preferred by some researchers.
   2. [data] The informatic representation of the biological clone.

*  Repertoire: Multiple definitions:

   1. [biology] Currently undefined due to lack of consensus.
   2. [data] The informatic representation of the biological repertoire.

*  Rearrangement: Multiple definitions:

   1. [biology] The physical combination of V and J or V, D, and J genes
      into a complete IG or TR.
   2. [data] The representation of a biological rearrangement, which is
      obtained through sequencing and annotated with features, such as
      gene calls, from data processing.


Abbreviations
=============

IT-related
----------

*  API: Application Programming Interface
*  HTTP: Hypertext Transfer Protocol
*  JSON: JavaScript Object Notation
*  REST: Representational State Transfer
*  TSV: Tab Separated Values
*  URL: Universal Resource Locator
*  YAML: YAML Ain't Markup Language


other
------

*  CAIRR: CEDAR AIRR
*  CEDAR: Center for Expanded Data Annotation and Retrieval
*  FAIR: The acronym for "Findable, Accessible, Interoperable,
   Reusable", a set of principles to facilitate the reuse of research
   data, defined by Wilkinson et al. (2016).
*  TAbS: The Antibody Society is an international, non-profit
   association representing individuals and organizations involved in
   antibody-related research and development.


Footnotes
=========

.. [restricted] There is a small but important set of terms that either
   designate AIRR-C WG products or are obviously linked to the identity
   of the ai. Consistent use of these terms both within AIRR-C as well
   as to the larger community is important to facilitate clear and
   unambiguous communication. Therefore, the terms marked as
   *restricted* in this document, **shall** be used **if and only if**
   they reference an entity that matches the terms definition.
   Conversely,
   
   1. terms that are synonymous to restricted terms, or
   2. terms that are obvious derivatives of a restricted term, or
   3. changes to the meaning of a restricted term, including the
      narrowing or broadening of its meaning,
      
   **shall** be avoided. Authors that seek AIRR-C endorsement for any
   kind of document must confirm that they acknowledge and comply with
   these conditions. They can include a waiver for specific terms from
   the responsible WG/SC a priori. Specific complaints about potential
   non-compliance that arise during the endorsement process will be
   heard by Exec and will halt the endorsement process until Exec
   considers them to be resolved.



.. == external links ==

.. _`DOI:10.1038/ni.3873`: https://doi.org/10.1038/ni.3873
